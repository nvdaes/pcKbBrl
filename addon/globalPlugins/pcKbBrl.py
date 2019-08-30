"""NVDA PC Keyboard Braille plugin
@author: James Teh <jamie@nvaccess.org>
@copyright: 2012-2014 NV Access Limited
@license: GNU General Public License version 2.0
"""

import globalPluginHandler
import winInputHook
import winUser
import api
import config
import ui
import inputCore
import brailleInput
import globalCommands
import wx
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

DOT1 = 1 << 0
DOT2 = 1 << 1
DOT3 = 1 << 2
DOT4 = 1 << 3
DOT5 = 1 << 4
DOT6 = 1 << 5
DOT7 = 1 << 6
DOT8 = 1 << 7

VKCODES_TO_DOTS = {
	70: DOT1, # f
	68: DOT2, # d
	83: DOT3, # s
	74: DOT4, # j
	75: DOT5, # k
	76: DOT6, # l
	65: DOT7, # a
	186: DOT8, # ;
	82: DOT1, # r
	69: DOT2, # e
	87: DOT3, # w
	85: DOT4, # u
	73: DOT5, # i
	79: DOT6, # o
	81: DOT7, # q
	80: DOT8, # p
	32: " ", # space,
}

VKCODES_TO_DOTS_ONE_HAND = {
	70: DOT1, # f
	68: DOT2, # d
	83: DOT3, # s
	74: DOT1, # j
	75: DOT2, # k
	76: DOT3, # l
	65: DOT7, # a
	186: DOT8, # ;
	82: DOT4, # r
	69: DOT5, # e
	87: DOT6, # w
	85: DOT4, # u
	73: DOT5, # i
	79: DOT6, # o
	81: DOT7, # q
	80: DOT8, # p
	32: " ", # space,
}

VKCODES_SEMICOLON = {
	3082: 192, # International Spanish
	2058: 192, # Latin Spanish
}

confspec = {
	"oneHandMode": "boolean(default=False)",
}

config.conf.spec["pcKbBrl"] = confspec

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_BRAILLE

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.isEnabled = False

	def terminate(self):
		self.disable()

	def getKeyboardLanguage(self):
		# Code borrowed from sayCurrentKeyboardLanguage add-on, by Abdel:
		# https://github.com/abdel792/sayCurrentKeyboardLanguage
		# Getting the handle of the foreground window.
		curWindow = winUser.getForegroundWindow()
		# Getting the threadID.
		threadID = winUser.getWindowThreadProcessID(curWindow)[1]
		# Getting the keyboard layout iD.
		klID = winUser.getKeyboardLayout(threadID)
		# Extract language ID from klID.
		lID = klID & (2**16 - 1)
		return lID

	def enable(self):
		if self.isEnabled:
			return
		self._trappedKeys = set()
		self._gesture = None
		self._keyboardLanguage = self.getKeyboardLanguage()
		self._oneHandMode = config.conf["pcKbBrl"]["oneHandMode"]
		self._shouldCopySemicolonKeyInfo = False
		# Monkey patch keyboard handling callbacks.
		# This is pretty evil, but we need low level keyboard handling.
		self._oldKeyDown = winInputHook.keyDownCallback
		winInputHook.keyDownCallback = self._keyDown
		self._oldKeyUp = winInputHook.keyUpCallback
		winInputHook.keyUpCallback = self._keyUp
		self.isEnabled = True

	def disable(self):
		if not self.isEnabled:
			return False
		winInputHook.keyDownCallback = self._oldKeyDown
		winInputHook.keyUpCallback = self._oldKeyUp
		self._gesture = None
		self._trappedKeys = None
		self._keyboardLanguage = None
		self._oneHandMode = None
		self._shouldCopySemicolonKeyInfo = False
		self.isEnabled = False

	def _keyDown(self, vkCode, scanCode, extended, injected):
		if vkCode == VKCODES_SEMICOLON.get(self._keyboardLanguage):
			vkCode = 186 # ;
		if not self._oneHandMode:
			dot = VKCODES_TO_DOTS.get(vkCode)
		else:
			if vkCode in (84, 89): # t, y
				self._gesture = None
				return False
			dot = VKCODES_TO_DOTS_ONE_HAND.get(vkCode)
		if dot is None and not (self._oneHandMode and vkCode in (71, 72)): # g, h
			if self._shouldCopySemicolonKeyInfo and api.copyToClip(
				u"Keyboard language: %d; vkCode: %s" %
					(self._keyboardLanguage,	vkCode)):
				# Translators: Reported when info about dot 8 is copied.
				ui.message(_("Info about dot 8 copied to clipboard."))
				self.disable()
			return self._oldKeyDown(vkCode, scanCode, extended, injected)
		self._trappedKeys.add(vkCode)
		if not self._gesture:
			self._gesture = brailleInput.BrailleInputGesture()
		if dot is " ": 
			self._gesture.space = True
		else:
			self._gesture.dots |= dot
		return False

	def _keyUp(self, vkCode, scanCode, extended, injected):
		if vkCode == VKCODES_SEMICOLON.get(self._keyboardLanguage):
			vkCode = 186 # ;
		if vkCode not in self._trappedKeys:
			return self._oldKeyUp(vkCode, scanCode, extended, injected)
		if self._oneHandMode and vkCode in (71, 72): # g, h
			self._trappedKeys.clear()
		if not self._oneHandMode or self._gesture.space:
			self._trappedKeys.discard(vkCode)
		if not self._trappedKeys:
			try:
				inputCore.manager.executeGesture(self._gesture)
			except inputCore.NoInputGestureAction:
				pass
			self._gesture = None
		return False

	def script_toggleInput(self, gesture):
		if self.isEnabled:
			self.disable()
			# Translators: Reported when braille input from the PC keyboard is disabled.
			ui.message(_("Braille input from PC keyboard disabled"))
		else:
			self.enable()
			# Translators: Reported when braille input from the PC keyboard is enabled.
			ui.message(_("Braille input from PC keyboard enabled"))
	# Translators: Describes a command.
	script_toggleInput.__doc__ = _("Toggles braille input from the PC keyboard.")

	def script_activateCopySemicolonKeyInfo(self, gesture):
		self.enable()
		self._shouldCopySemicolonKeyInfo = True
		# Translators: Reported when should copy info for semicolon key.
		ui.message(_("Press the key at right to l to copy info for supporting dot 8 in your keyboard language."))
	# Translators: Describes a command.
	script_activateCopySemicolonKeyInfo.__doc__ = _("Allows to copy info about dot 8.")

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
	script_settings.category = globalCommands.SCRCAT_CONFIG
	# Translators: Describes a command.
	script_settings.__doc__ = _("Shows the %s settings." % ADDON_SUMMARY)
	
	__gestures = {
		"kb:NVDA+z": "toggleInput",
		"kb:NVDA+X": "activateCopySemicolonKeyInfo",
	}

class AddonSettingsPanel(SettingsPanel):

	title = ADDON_SUMMARY

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.oneHandModeCheckBox = sHelper.addItem(wx.CheckBox(self, label= _("Type using one hand")))
		self.oneHandModeCheckBox.SetValue(config.conf["pcKbBrl"]["oneHandMode"])

	def postInit(self):
		self.oneHandModeCheckBox.SetFocus()

	def onSave(self):
		config.conf["pcKbBrl"]["oneHandMode"] = self.oneHandModeCheckBox.GetValue()

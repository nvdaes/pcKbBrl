# -*- coding: UTF-8 -*-

"""NVDA PC Keyboard Braille plugin
@author: James Teh <jamie@nvaccess.org>
@copyright: 2012-2022 NV Access Limited, Noelia Ruiz Martínez
@license: GNU General Public License version 2.0
"""

import wx

import globalPluginHandler
import winInputHook
import winUser
import core
import config
import ui
import speech
import inputCore
import keyboardHandler
import brailleInput
import globalCommands
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
from scriptHandler import script
import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
TIMEOUT = 1000

DOT1 = 1 << 0
DOT2 = 1 << 1
DOT3 = 1 << 2
DOT4 = 1 << 3
DOT5 = 1 << 4
DOT6 = 1 << 5
DOT7 = 1 << 6
DOT8 = 1 << 7

VKCODES_TO_DOTS = {
	70: DOT1,  # f
	68: DOT2,  # d
	83: DOT3,  # s
	74: DOT4,  # j
	75: DOT5,  # k
	76: DOT6,  # l
	65: DOT7,  # a
	186: DOT8,  # ;
	82: DOT1,  # r
	69: DOT2,  # e
	87: DOT3,  # w
	85: DOT4,  # u
	73: DOT5,  # i
	79: DOT6,  # o
	81: DOT7,  # q
	80: DOT8,  # p
	32: " ",  # space,
}

VKCODES_TO_DOTS_ONE_HAND = {
	70: DOT1,  # f
	68: DOT2,  # d
	83: DOT3,  # s
	74: DOT1,  # j
	75: DOT2,  # k
	76: DOT3,  # l
	65: DOT7,  # a
	186: DOT7,  # ;
	82: DOT4,  # r
	69: DOT5,  # e
	87: DOT6,  # w
	85: DOT4,  # u
	73: DOT5,  # i
	79: DOT6,  # o
	81: DOT8,  # q
	80: DOT8,  # p
	32: " ",  # space,
}

VKCODES = {
	1031: {  # de
		89: None,  # y (original key)
		90: 89,  # y
		192: 186,  # ;
	},
	3082: {  # es
		192: 186,  # ;
	},
	2058: {  # es_MX
		192: 186,  # ;
	},
	1036: {  # fr
		65: 81,  # q
		77: 186,  # ;
		81: 65,  # a
		87: None,  # w (original key)
		90: 87,  # w
	},
	1040: {  # it
		192: 186,  # ;
	},
	2070: {  # pt_PT
		192: 186,  # ;
	},
}

confspec = {
	"oneHandMode": "boolean(default=False)",
	"speakDot": "boolean(default=False)",
	"useTimeout": "boolean(default=False)",
	"confirmKeys": "string(default=gh)",
	"cancelKeys": "string(default=ty)"
}

config.conf.spec["pcKbBrl"] = confspec

entries = {
	"globalCommands.GlobalCommands": {
		"kb:upArrow": "bk:space+dot1",
		"kb:downArrow": "bk:space+dot4",
		"kb:leftArrow": "bk:space+dot3",
		"kb:rightArrow": "bk:space+dot6",
		"kb:control+leftArrow": "bk:space+dot2",
		"kb:control+rightArrow": "bk:space+dot5",
		"kb:home": "bk:space+dot1+dot3",
		"kb:end": "bk:space+dot4+dot6",
		"kb:control+home": "bk:space+dot1+dot2+dot3",
		"kb:control+end": "bk:space+dot4+dot5+dot6",
		"reportCurrentLine": "bk:space+dot1+dot4"
	}
}

inputCore.manager.userGestureMap.update(entries)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_BRAILLE

	def __init__(self):
		super().__init__()
		self.isEnabled = False
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def handleConfigProfileSwitch(self):
		self._oneHandMode = config.conf["pcKbBrl"]["oneHandMode"]
		self._speakDot = config.conf["pcKbBrl"]["speakDot"]
		self._confirmCodes = self.getConfirmCodes()
		self._cancelCodes = self.getCancelCodes()
		self._confirmGesture = keyboardHandler.KeyboardInputGesture.fromName(config.conf["pcKbBrl"]["confirmKeys"][0])

	def terminate(self):
		self.disable()
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

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

	def getConfirmCodes(self):
		confirmKeys = config.conf["pcKbBrl"]["confirmKeys"]
		confirmCodes = []
		keys = []
		for key in confirmKeys:
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if self._keyboardLanguage in VKCODES.keys() and code in VKCODES[self._keyboardLanguage].keys():
				code = VKCODES[self._keyboardLanguage][code]
			dot = VKCODES_TO_DOTS_ONE_HAND.get(code)
			if dot is None:
				confirmCodes.append(code)
				keys.append(key.lower())
		if not len(keys):
			config.conf["pcKbBrl"]["confirmKeys"] = "gh"
			confirmCodes = [71, 72]
		else:
			keysSet = set(keys)
			config.conf["pcKbBrl"]["confirmKeys"] = "".join(keysSet)
		return set(confirmCodes)

	def getCancelCodes(self):
		cancelKeys = config.conf["pcKbBrl"]["cancelKeys"]
		confirmKeys = config.conf["pcKbBrl"]["confirmKeys"]
		cancelCodes = []
		keys = []
		for key in cancelKeys:
			if key in confirmKeys:  # Confirm keys have priority
				continue
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if self._keyboardLanguage in VKCODES.keys() and code in VKCODES[self._keyboardLanguage].keys():
				code = VKCODES[self._keyboardLanguage][code]
			dot = VKCODES_TO_DOTS_ONE_HAND.get(code)
			if dot is None:
				cancelCodes.append(code)
				keys.append(key.lower())
		if not len(keys):
			config.conf["pcKbBrl"]["cancelKeys"] = "ty"
			cancelCodes = [84, 89]
		else:
			keysSet = set(keys)
			config.conf["pcKbBrl"]["cancelKeys"] = "".join(keysSet)
		return set(cancelCodes)

	def enable(self):
		if self.isEnabled:
			return
		self._trappedKeys = set()
		self._gesture = None
		self._keyboardLanguage = self.getKeyboardLanguage()
		self._oneHandMode = config.conf["pcKbBrl"]["oneHandMode"]
		self._speakDot = config.conf["pcKbBrl"]["speakDot"]
		self._confirmCodes = self.getConfirmCodes()
		self._cancelCodes = self.getCancelCodes()
		self._confirmGesture = keyboardHandler.KeyboardInputGesture.fromName(
			config.conf["pcKbBrl"]["confirmKeys"][0]
		)
		self._dot = None
		# Monkey patch keyboard handling callbacks.
		# This is pretty evil, but we need low level keyboard handling.
		self._oldKeyDown = winInputHook.keyDownCallback
		winInputHook.keyDownCallback = self._keyDown
		self._oldKeyUp = winInputHook.keyUpCallback
		winInputHook.keyUpCallback = self._keyUp
		config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
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
		self._speakDot = None
		self._confirmCodes = None
		self._cancelCodes = None
		self._confirmGesture = None
		self._dot = None
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		self.isEnabled = False

	def _keyDown(self, vkCode, scanCode, extended, injected):
		if self._keyboardLanguage in VKCODES.keys() and vkCode in VKCODES[self._keyboardLanguage].keys():
			vkCode = VKCODES[self._keyboardLanguage][vkCode]
		if vkCode is None:
			return False
		if not self._oneHandMode:
			self._dot = VKCODES_TO_DOTS.get(vkCode)
		else:
			if vkCode in self._cancelCodes:
				self._gesture = None
				return False
			self._dot = VKCODES_TO_DOTS_ONE_HAND.get(vkCode)
		if self._dot is None and not (self._oneHandMode and vkCode in self._confirmCodes):
			return self._oldKeyDown(vkCode, scanCode, extended, injected)
		self._trappedKeys.add(vkCode)
		if not self._gesture:
			self._gesture = brailleInput.BrailleInputGesture()
		if self._dot is not None:
			if self._dot == " ":
				self._gesture.space = True
			else:
				self._gesture.dots |= self._dot
		return False

	def _keyUp(self, vkCode, scanCode, extended, injected):
		if self._keyboardLanguage in VKCODES.keys() and vkCode in VKCODES[self._keyboardLanguage].keys():
			vkCode = VKCODES[self._keyboardLanguage][vkCode]
		if vkCode not in self._trappedKeys:
			return self._oldKeyUp(vkCode, scanCode, extended, injected)
		if self._oneHandMode:
			if vkCode in self._confirmCodes:
				self._trappedKeys.clear()
			elif config.conf["pcKbBrl"]["useTimeout"]:
				self._typeCallLater = core.callLater(TIMEOUT, self._confirmGesture.send)
		if not self._oneHandMode or self._gesture.space:
			self._trappedKeys.discard(vkCode)
		if not self._trappedKeys:
			try:
				inputCore.manager.executeGesture(self._gesture)
			except (inputCore.NoInputGestureAction, IndexError):
				pass
			self._gesture = None
		else:
			if (
				self._oneHandMode and self._speakDot
				and isinstance(self._dot, int)
			):
				brailleInput.speakDots(self._dot)
		return False

	@script(
		# Translators: Describes a command.
		description=_("Toggles braille input from the PC keyboard."),
		gesture="kb:NVDA+0"
	)
	def script_toggleInput(self, gesture):
		if self.isEnabled:
			self.disable()
			# Translators: Reported when braille input from the PC keyboard is disabled.
			message = _("Braille input from PC keyboard disabled")
		else:
			self.enable()
			# Translators: Reported when braille input from the PC keyboard is enabled.
			message = _("Braille input from PC keyboard enabled")
		ui.message(message, speechPriority=speech.priorities.Spri.NOW)

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: Describes a command.
		description=_("Shows the %s settings.") % ADDON_SUMMARY,
		category=globalCommands.SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_SUMMARY

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.oneHandModeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Type using one hand")))
		self.oneHandModeCheckBox.SetValue(config.conf["pcKbBrl"]["oneHandMode"])
		# Translators: label of a dialog.
		self.speakDotCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Speak dot when typing with one hand")))
		self.speakDotCheckBox.SetValue(config.conf["pcKbBrl"]["speakDot"])
		# Translators: label of a dialog.
		self.useTimeoutCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("Send dots &automatically when typing with one hand")))
		self.useTimeoutCheckBox.SetValue(config.conf["pcKbBrl"]["useTimeout"])

		# Translators: label of a dialog.
		confirmKeysLabel = _("Type the characters to con&firm when writing with one hand.")
		self.confirmKeysEdit = sHelper.addLabeledControl(confirmKeysLabel, wx.TextCtrl)
		try:
			self.confirmKeysEdit.SetValue(config.conf["pcKbBrl"]["confirmKeys"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		cancelKeysLabel = _("Type the characters to cance&l when writing with one hand.")
		self.cancelKeysEdit = sHelper.addLabeledControl(cancelKeysLabel, wx.TextCtrl)
		try:
			self.cancelKeysEdit.SetValue(config.conf["pcKbBrl"]["cancelKeys"])
		except KeyError:
			pass

	def postInit(self):
		self.oneHandModeCheckBox.SetFocus()

	def onSave(self):
		config.conf["pcKbBrl"]["oneHandMode"] = self.oneHandModeCheckBox.GetValue()
		config.conf["pcKbBrl"]["speakDot"] = self.speakDotCheckBox.GetValue()
		config.conf["pcKbBrl"]["useTimeout"] = self.useTimeoutCheckBox.GetValue()
		if self.confirmKeysEdit.GetValue():
			config.conf["pcKbBrl"]["confirmKeys"] = self.confirmKeysEdit.GetValue()
		if self.cancelKeysEdit.GetValue():
			config.conf["pcKbBrl"]["cancelKeys"] = self.cancelKeysEdit.GetValue()

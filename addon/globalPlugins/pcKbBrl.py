# -*- coding: UTF-8 -*-

"""NVDA PC Keyboard Braille plugin
@author: James Teh <jamie@nvaccess.org>
@copyright: 2012-2022 NV Access Limited, Noelia Ruiz Martínez
@license: GNU General Public License version 2.0
"""

import wx
import itertools
from dataclasses import dataclass

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
from gui import SettingsPanel, NVDASettingsDialog, guiHelper, nvdaControls
from scriptHandler import script
from logHandler import log
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
	"timeout": "integer(default=0)",
	"confirmKeys": "string(default=gh)",
	"cancelKeys": "string(default=ty)",
	"dot1": 'string(default="")',
	"dot2": 'string(default="")',
	"dot3": 'string(default="")',
	"dot4": 'string(default="")',
	"dot5": 'string(default="")',
	"dot6": 'string(default="")',
	"dot7": 'string(default="")',
	"dot8": 'string(default="")',
	"nullKeys": 'string(default="")'
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


@dataclass
class Dot:
	number: int = 0

	def getOutput(self):
		possibleOutputs = (DOT1, DOT2, DOT3, DOT4, DOT5, DOT6, DOT7, DOT8)
		number = self.number
		return possibleOutputs[number - 1]

	def getDotCodes(self):
		number = self.number
		dotKeys = config.conf["pcKbBrl"][f"dot{number}"]
		keyboardLanguage = GlobalPlugin.getKeyboardLanguage()
		dotCodes = []
		for key in dotKeys:
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if keyboardLanguage in VKCODES.keys() and code in VKCODES[keyboardLanguage].keys():
				code = VKCODES[keyboardLanguage][code]
			dotCodes.append(code)
		return set(dotCodes)


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
		self._confirmGesture = keyboardHandler.KeyboardInputGesture.fromName(
			config.conf["pcKbBrl"]["confirmKeys"][0]
		)

	def terminate(self):
		self.disable()
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	@staticmethod
	def getKeyboardLanguage():
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
		for key in confirmKeys:
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if self._keyboardLanguage in VKCODES.keys() and code in VKCODES[self._keyboardLanguage].keys():
				code = VKCODES[self._keyboardLanguage][code]
			confirmCodes.append(code)
		return set(confirmCodes)

	def getCancelCodes(self):
		cancelKeys = config.conf["pcKbBrl"]["cancelKeys"]
		confirmKeys = config.conf["pcKbBrl"]["confirmKeys"]
		cancelCodes = []
		for key in cancelKeys:
			if key in confirmKeys:  # Confirm keys have priority
				continue
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if self._keyboardLanguage in VKCODES.keys() and code in VKCODES[self._keyboardLanguage].keys():
				code = VKCODES[self._keyboardLanguage][code]
			cancelCodes.append(code)
		return set(cancelCodes)

	def getNullKeyCodes(self):
		nullKeys = config.conf["pcKbBrl"]["nullKeys"]
		nullKeyCodes = []
		for key in nullKeys:
			gesture = keyboardHandler.KeyboardInputGesture.fromName(key.lower())
			code = gesture.vkCode
			if self._keyboardLanguage in VKCODES.keys() and code in VKCODES[self._keyboardLanguage].keys():
				code = VKCODES[self._keyboardLanguage][code]
			nullKeyCodes.append(code)
		return set(nullKeyCodes)

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
		self._nullKeyCodes = self.getNullKeyCodes()
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
		self._nullKeyCodes = None
		self._dot = None
		config.post_configProfileSwitch.unregister(self.handleConfigProfileSwitch)
		self.isEnabled = False

	def _keyDown(self, vkCode, scanCode, extended, injected):  # NOQA: C901
		if self._keyboardLanguage in VKCODES.keys() and vkCode in VKCODES[self._keyboardLanguage].keys():
			vkCode = VKCODES[self._keyboardLanguage][vkCode]
		if vkCode is None or vkCode in self._nullKeyCodes:
			return False
		if not self._oneHandMode:
			self._dot = VKCODES_TO_DOTS.get(vkCode)
		else:
			if vkCode in self._cancelCodes:
				self._gesture = None
				return False
			if vkCode in Dot(1).getDotCodes():
				self._dot = Dot(1).getOutput()
			elif vkCode in Dot(2).getDotCodes():
				self._dot = Dot(2).getOutput()
			elif vkCode in Dot(3).getDotCodes():
				self._dot = Dot(3).getOutput()
			elif vkCode in Dot(4).getDotCodes():
				self._dot = Dot(4).getOutput()
			elif vkCode in Dot(5).getDotCodes():
				self._dot = Dot(5).getOutput()
			elif vkCode in Dot(6).getDotCodes():
				self._dot = Dot(6).getOutput()
			elif vkCode in Dot(7).getDotCodes():
				self._dot = Dot(7).getOutput()
			elif vkCode in Dot(8).getDotCodes():
				self._dot = Dot(8).getOutput()
			else:
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
			elif config.conf["pcKbBrl"]["timeout"]:
				timeout = config.conf["pcKbBrl"]["timeout"]
				self._typeCallLater = core.callLater(timeout, self._confirmGesture.send)
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

	def makeSettings(self, settingsSizer):  # NOQA: C901
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.oneHandModeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Type using one hand")))
		self.oneHandModeCheckBox.SetValue(config.conf["pcKbBrl"]["oneHandMode"])
		# Translators: label of a dialog.
		self.speakDotCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Speak dot when typing with one hand")))
		self.speakDotCheckBox.SetValue(config.conf["pcKbBrl"]["speakDot"])
		# Translators: label of a dialog.
		label = _("&Timeout to send dots when writing with one hand (in ms)")
		self.timeoutSpinControl = sHelper.addLabeledControl(
			label,
			nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=2000,
			initial=config.conf["pcKbBrl"]["timeout"]
		)
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
		# Translators: label of a dialog.
		dot1KeysLabel = _("Characters for dot&1 when writing with one hand:")
		self.dot1KeysEdit = sHelper.addLabeledControl(dot1KeysLabel, wx.TextCtrl)
		self.dot1KeysEdit.SetValue(config.conf["pcKbBrl"]["dot1"])
		# Translators: label of a dialog.
		dot2KeysLabel = _("Type the characters for dot2 when writing with one hand.")
		self.dot2KeysEdit = sHelper.addLabeledControl(dot2KeysLabel, wx.TextCtrl)
		try:
			self.dot2KeysEdit.SetValue(config.conf["pcKbBrl"]["dot2"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot3KeysLabel = _("Type the characters for dot3 when writing with one hand.")
		self.dot3KeysEdit = sHelper.addLabeledControl(dot3KeysLabel, wx.TextCtrl)
		try:
			self.dot3KeysEdit.SetValue(config.conf["pcKbBrl"]["dot3"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot4KeysLabel = _("Type the characters for dot4 when writing with one hand.")
		self.dot4KeysEdit = sHelper.addLabeledControl(dot4KeysLabel, wx.TextCtrl)
		try:
			self.dot4KeysEdit.SetValue(config.conf["pcKbBrl"]["dot4"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot5KeysLabel = _("Type the characters for dot5 when writing with one hand.")
		self.dot5KeysEdit = sHelper.addLabeledControl(dot5KeysLabel, wx.TextCtrl)
		try:
			self.dot5KeysEdit.SetValue(config.conf["pcKbBrl"]["dot5"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot6KeysLabel = _("Type the characters for dot6 when writing with one hand.")
		self.dot6KeysEdit = sHelper.addLabeledControl(dot6KeysLabel, wx.TextCtrl)
		try:
			self.dot6KeysEdit.SetValue(config.conf["pcKbBrl"]["dot6"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot7KeysLabel = _("Type the characters for dot7 when writing with one hand.")
		self.dot7KeysEdit = sHelper.addLabeledControl(dot7KeysLabel, wx.TextCtrl)
		try:
			self.dot7KeysEdit.SetValue(config.conf["pcKbBrl"]["dot7"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		dot8KeysLabel = _("Type the characters for dot8 when writing with one hand.")
		self.dot8KeysEdit = sHelper.addLabeledControl(dot8KeysLabel, wx.TextCtrl)
		try:
			self.dot8KeysEdit.SetValue(config.conf["pcKbBrl"]["dot8"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		nullKeysLabel = _("Type the characters to be &ignored when typing in braille.")
		self.nullKeysEdit = sHelper.addLabeledControl(nullKeysLabel, wx.TextCtrl)
		try:
			self.nullKeysEdit.SetValue(config.conf["pcKbBrl"]["nullKeys"])
		except KeyError:
			pass
		# Translators: label of a dialog.
		self.restoreDefaultsButton = sHelper.addItem(wx.Button(self, label=_("&Restore defaults")))
		self.restoreDefaultsButton.Bind(wx.EVT_BUTTON, self.onRestoreDefaults)

	def postInit(self):
		self.oneHandModeCheckBox.SetFocus()

	def onRestoreDefaults(self, evt):
		self.oneHandModeCheckBox.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'oneHandMode']).default)
		self.speakDotCheckBox.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'speakDot']).default)
		self.timeoutSpinControl.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'timeout']).default)
		self.confirmKeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'confirmKeys']).default)
		self.cancelKeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'cancelKeys']).default)
		self.dot1KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot1']).default)
		self.dot2KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot2']).default)
		self.dot3KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot3']).default)
		self.dot4KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot4']).default)
		self.dot5KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot5']).default)
		self.dot6KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot6']).default)
		self.dot7KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot7']).default)
		self.dot8KeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'dot8']).default)
		self.nullKeysEdit.SetValue(config.conf.getConfigValidation(['pcKbBrl', 'nullKeys']).default)

	def isValid(self):
		configuredKeys = list(itertools.chain(
			self.confirmKeysEdit.GetValue(), self.cancelKeysEdit.GetValue(),
			self.dot1KeysEdit.GetValue(), self.dot2KeysEdit.GetValue(), self.dot3KeysEdit.GetValue(), self.dot4KeysEdit.GetValue(),
			self.dot5KeysEdit.GetValue(), self.dot6KeysEdit.GetValue(), self.dot7KeysEdit.GetValue(), self.dot8KeysEdit.GetValue(),
			self.nullKeysEdit.GetValue()
		))
		for key in configuredKeys:
			if key == "":
				configuredKeys.remove(key)
		if len(configuredKeys) != len(set(configuredKeys)):
			log.debugWarning("pcKbBrl: repeated keys have been set")
			gui.messageBox(
				# Translators: Message to report wrong configuration.
				_("Configured keys for pcKbBrl shouldn't be repeated."),
				# Translators: Title of message box
				_("Error"), wx.OK|wx.ICON_ERROR,self)
			return False
		return super(AddonSettingsPanel, self).isValid()

	def onSave(self):
		config.conf["pcKbBrl"]["oneHandMode"] = self.oneHandModeCheckBox.GetValue()
		config.conf["pcKbBrl"]["speakDot"] = self.speakDotCheckBox.GetValue()
		config.conf["pcKbBrl"]["timeout"] = self.timeoutSpinControl.GetValue()
		if self.confirmKeysEdit.GetValue():
			config.conf["pcKbBrl"]["confirmKeys"] = self.confirmKeysEdit.GetValue()
		else:
			config.conf["pcKbBrl"]["confirmKeys"] = "gh"
		if self.cancelKeysEdit.GetValue():
			config.conf["pcKbBrl"]["cancelKeys"] = self.cancelKeysEdit.GetValue()
		else:
			config.conf["pcKbBrl"]["cancelKeys"] = "ty"
		config.conf["pcKbBrl"]["dot1"] = self.dot1KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot2"] = self.dot2KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot3"] = self.dot3KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot4"] = self.dot4KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot5"] = self.dot5KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot5"] = self.dot5KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot6"] = self.dot6KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot7"] = self.dot7KeysEdit.GetValue()
		config.conf["pcKbBrl"]["dot8"] = self.dot8KeysEdit.GetValue()
		config.conf["pcKbBrl"]["nullKeys"] = self.nullKeysEdit.GetValue()

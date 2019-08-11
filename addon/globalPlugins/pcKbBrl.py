"""NVDA PC Keyboard Braille plugin
@author: James Teh <jamie@nvaccess.org>
@copyright: 2012-2014 NV Access Limited
@license: GNU General Public License version 2.0
"""

import globalPluginHandler
import winInputHook
import ui
import inputCore
import brailleInput
import globalCommands
import addonHandler

addonHandler.initTranslation()

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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_BRAILLE

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.isEnabled = False

	def terminate(self):
		self.disable()

	def enable(self):
		if self.isEnabled:
			return
		self._trappedKeys = set()
		self._gesture = None
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
		self.isEnabled = False

	def _keyDown(self, vkCode, scanCode, extended, injected):
		dot = VKCODES_TO_DOTS.get(vkCode)
		if dot is None:
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
		if vkCode not in self._trappedKeys:
			return self._oldKeyUp(vkCode, scanCode, extended, injected)
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

	__gestures = {
		"kb:NVDA+z": "toggleInput",
	}

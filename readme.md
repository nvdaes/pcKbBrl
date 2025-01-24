# PC Keyboard Braille Input for NVDA

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* License: GNU General Public License version 2.0

This NVDA add-on allows braille to be entered via the PC keyboard.
Currently, the following keyboard layouts are supported:

* English QWERTY keyboard.
* French (France).
* German (Germany).
* Italian (Italy).
* Persian.
* Portuguese (Portugal).
* Spanish (Spain and Mexico).
* Turkish.

## How to configure

The add-on can be configured from its category in the NVDA's settings dialog, under NVDA's menu, Preferences submenu. A gesture for opening the add-on settings panel can be assigned from Input gestures dialog, configuration category.

Check the corresponding checkbox if you want to type using only one hand, or ensure it's not checked if you prefer to type using the standard mode (two hands).

You can also select if NVDA should speak a single typed dot (using )the feature of "one hand mode").

If you want dots to be sent automatically when typing with one hand, use the spin control to set a timeout greater than 0.

In addition, you can set the characters to send, clear and compose dots when typing with one hand, as well as characters to be ignored in one hand or standard mode.

It's also possible to restore defaults in the add-on settings panel.

## How to Use

1. Press NVDA+0 to enable braille input. This gesture can be changed from Input gestures dialog, Braille category.
2. Type braille by pressing keys together on the PC keyboard as if it were a braille keyboard.
	* If you want to enter text using two hands, use the following keys if you work with a QWERTY English keyboard, or the keys located at the corresponding positions in other layouts:
		* f, d and s for dots 1, 2 and 3 respectively.
		* j, k and l for dots 4, 5 and 6 respectively.
		* Use the keys a and ; (semi-colon) for dots 7 and 8, respectively.
		* You can also use the keys on the row above; i.e. q, w, e, r, u, i, o and p.
	* If you want to type text using one hand, you can compose characters pressing keys simultaneously or in several keystrokes, adding the dots corresponding to the desired character. Press g or h to type the character when you have added all its dots. If you make a mistake building a character, you can clear the dots before typing it by pressing t or y. The keys used in QWERTY English keyboard are the following:
		* Left hand: f, d, s, r, e, w, a, q for dots 1, 2, 3, 4, 5, 6, 7 and 8.
		* Right hand: j, k, l, u, i, o, ; (semicolon), p for dots 1, 2, 3, 4, 5, 6, 7 and 8.
3. You can press most other keys as normal, including space, backspace, enter and function keys. Take care about not pressing alt+shift, since changing the keyboard layout may affect the entered dots.
4. Press space bar in combination with braille dots to move the system cursor (or report the current line), just if you were using a braille display. For example, space+dot1 to emulate upArrow, space+dot4+dot5+dot6 to emulate control+end, space+dot1+dot4 to report the current line, etc.
5. Press NVDA+0 to disable braille input.

## Important Notes

This add-on uses NVDA's in-built braille input support.
Therefore, the input table used is that specified in NVDA's Braille Settings dialog.

Some keyboards, particularly laptop keyboards, cannot handle certain combinations of keys being pressed.
When this happens, certain keys are simply ignored.
Unfortunately, there is nothing that can be done to fix this, as the keys are simply never received by Windows or NVDA.
In some cases, using the upper row of keys with either or both hands might help, as your keyboard may allow these keys.

## Changes for 44.0.0

* Added kannada.cti table.

## Changes for 28.0.0

* Changed default values for One hand mode.

## Changes for 2023.02.23

* Added ability to configure keys used to type dots in one hand mode.
* Now you can configure keys that should be ignored when typing in braille.
* A restore to defaults button has been added to the add-on settings panel.
* Compatible with NVDA 2023.1.

## Changes for 2022.1

* Added ability to configure keys to send and clear dots when writing with one hand. Also, it's possible to set a timeout to send dots automatically, without pressing confirmation keys.

## Changes for 2021.1

* NVDA won't try to speak dots when One hand mode is not active or if space has been pressed.
* Compatible with NVDA 2021.1.

## Changes for 2020.1

* You can press space bar in combination with braille dots to emulate gestures, similar to commands available in braille displays.
* Added an option to speak single dots typed in one hand mode.

## Contributors

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

# PC Keyboard Braille Input for NVDA

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2019 NV Access Limited, Noelia Ruiz Martínez
* License: GNU General Public License version 2.0
* Download: [version 2019.1][1]

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

The add-on is compatible with NVDA 2019.3. If you need to use an older version, download [version 2014.1][2]

## How to configure

The add-on can be configured from its category in the NVDA's settings dialog, under NVDA's menu, Preferences submenu. A gesture for opening the add-on settings panel can be assigned from Input gestures dialog, configuration category.

Check the corresponding checkbox if you want to type using only one hand, or ensure it's not checked if you prefer to type using the standard mode (two hands).

## How to Use

1. Press NVDA+0 to enable braille input. This gesture can be changed from Input gestures dialog, Braille category.
2. Type braille by pressing keys together on the PC keyboard as if it were a braille keyboard.
	* If you want to enter text using two hands, use the following keys if you work with a QWERTY English keyboard, or the keys located at the corresponding positions in other layouts:
		* f, d and s for dots 1, 2 and 3 respectively.
		* j, k and l for dots 4, 5 and 6 respectively.
		* Use the keys a and ; (semi-colon) for dots 7 and 8, respectively.
		* You can also use the keys on the row above; i.e. q, w, e, r, u, i, o and p.
	* If you want to type text using one hand, you can compose characters pressing keys simultaneously or in several keystrokes, adding the dots corresponding to the desired character. Press g or h to type the character when you have added all its dots. If you make a mistake building a character, you can clear the dots before typing it by pressing t or y. The keysused in QWERTY English keyboard are the following.
			* Left hand: f, d, s, r, e, w, a, q  for dots 1, 2, 3, 4, 5, 6, 7 and 8.
			* Right hand: j, k, l, u, i, o, ; (semicolon), p for dots 1, 2, 3, 4, 5, 6, 7 and 8.
3. You can press most other keys as normal, including space, backspace, enter and function keys. Take care about not pressing alt+shift, since changing the keyboard layout may affect the entered dots.
4. Press NVDA+0 to disable braille input.

## Important Notes

This add-on uses NVDA's in-built braille input support.
Therefore, the input table used is that specified in NVDA's Braille Settings dialog.

Some keyboards, particularly laptop keyboards, cannot handle certain combinations of keys being pressed.
When this happens, certain keys are simply ignored.
Unfortunately, there is nothing that can be done to fix this, as the keys are simply never received by Windows or NVDA.
In some cases, using the upper row of keys with either or both hands might help, as your keyboard may allow these keys.

## Contributors

* James Teh
* Noelia Ruiz Martínez
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot


[1]: https://addons.nvda-project.org/files/get.php?file=pckbbrl

[2]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-o

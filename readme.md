[[!meta title="PC Keyboard Braille Input for NVDA"]]

* Author: NV Access Limited
* Copyright: 2012-2014 NV Access Limited
* License: GNU General Public License version 2.0
* Download: [version 2014.1][1]

This NVDA add-on allows braille to be entered via the PC keyboard.
Currently, only the English QWERTY keyboard layout is supported.

## How to Use

1. Press NVDA+z to enable braille input.
2. Type braille by pressing keys together on the PC keyboard as if it were a braille keyboard.
	* Use the keys s, d and f for dots 1, 2 and 3 respectively.
	* Use the keys j, k and l for dots 4, 5 and 6 respectively.
	* Use the keys a and ; (semi-colon) for dots 7 and 8, respectively.
	* You can also use the keys on the row above; i.e. q, w, e, r, u, i, o and p.
3. You can press most other keys as normal, including space, backspace, enter and function keys.
4. Press NVDA+z to disable braille input.

## Important Notes

This add-on uses NVDA's in-built braille input support.
Therefore, the input table used is that specified in NVDA's Braille Settings dialog.
NVDA only supports computer braille input at present, so this limitation also applies to this add-on.

Some keyboards, particularly laptop keyboards, cannot handle certain combinations of keys being pressed.
When this happens, certain keys are simply ignored.
Unfortunately, there is nothing that can be done to fix this, as the keys are simply never received by Windows or NVDA.
In some cases, using the upper row of keys with either or both hands might help, as your keyboard may allow these keys.

## Contributors

* James Teh

[[!tag dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=pckbbrl

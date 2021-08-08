# Braille-Eingabe via PC-Tastatur #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2019 NV Access Limited, Noelia Ruiz Martínez
* Lizenz: GNU Allgemeine Öffentliche Lizenz Version 2.0
* [stabile Version][1] herunterladen (kompatibel mit NVDA 2019.3 oder neuer)
* [Testversion][2] herunterladen (kompatibel mit NVDA 2019.3 oder neuer)
* [Version 2014.1][3] (kompatibel mit NVDA 2017.3 bis 2019.2)

Diese NVDA-Erweiterung ermöglicht die Eingabe von Braille über die
PC-Tastatur. Momentan werden folgende Tastaturschemen unterstützt:

* Englisch QWERTY-Tastatur.
* Französisch (Frankreich).
* Deutsch (Deutschland).
* Italienisch (Italien)
* Persisch.
* Portugiesisch (Portugal).
* Spanisch (Spanien und Mexiko).
* Türkisch.

## Einstellungsmöglichkeiten

Die Erweiterung kann über die Kategorie im NVDA-Einstellungs-Dialog
konfiguriert werden, welchen Sie im NVDA-Menü und Optionen finden. Eine
Geste, um die Erweiterungs-Einstellungen zu öffnen, können sie im Dialog
Tastenbefehle in der Kategorie Konfiguration festlegen.

Aktivieren sie das zugehörige Kontrollkästchen, sofern Sie nur mit einer
Hand schreiben wollen oder lassen Sie es deaktiviert, wenn Sie normal (also
mit 2 Händen) schreiben wollen.

Sie können auch festlegen, ob NVDA einen einzelnen bestimmten Punkt sprechen
soll, der im Einhandmodus eingegeben wird.

## Verwendung

1. Drücken Sie NVDA+0, um die Braille-Eingabe zu aktivieren. Die Geste
   können Sie im Dialog Tastenbefehle in der Kategorie Braille ändern.
2. Tippen Sie Braille auf der PC-Tastatur indem Sie Tasten zusammen drücken,
   wie Sie es auf einer Braille-Tastatur machen.

	* Wenn Sie Text mit beiden Händen eingeben, verwenden Sie die folgenden
	  Tasten auf einer englischen QWERTY-Tastatur oder die Tasten an der
	  entsprechenden Stelle bei anderen Layouts:

		* f, d und s jeweils für die Punkte 1, 2 und 3.
		* j, k und l jeweils für die Punkte 4, 5 und 6 respectively.
		* Verwenden Sie die Tasten a und ö entsprechend für die Punkte 7 und 8.
		* Sie können auch die Tasten eine Reihe darüber verwenden; z. B. q, w, e,
		  r, u, i, o und p.

	* Wenn Sie Text mit einer Hand schreiben wollen, können Sie Zeichen
	  zusammensetzen, in dem Sie Tasten gleichzeitig drücken oder mit mehreren
	  Tastenanschlägen eingeben, in dem Sie die entsprechenden Punkte dem
	  gewünschten Zeichen hinzufügen. Drücken Sie anschließend g oder h, um das
	  Zeichen zu schreiben, wenn Sie alle Punkte hinzugefügt haben. Sollten Sie
	  einen Fehler beim zusammensetzen eines Zeichens machen, lassen Sie
	  mittels t oder z die gesetzten Punkte wieder los. Folgende Tasten werden
	  auf einer  Englischen QWERTY-Tastatur verwendet:

		* Linke Hand: f, d, s, r, e, w, a, q für die Punkte 1, 2, 3, 4, 5, 6, 7
		  und 8.
		* Rechte Hand: j, k, l, u, i, o, ö und, p für die Punkte 1, 2, 3, 4, 5, 6,
		  7 und 8.

3. Sie könnnen die meisten Tasten (wie Leertaste, F-Tasten, Eingabe,
   Rücktaste sowie die Pfeiltasten) gewohnt betätigen. Beachten Sie, dass
   die Tastenkombination Alt+Umschalt das verwendete Tastaturlayout
   wechselt, sodass Sie möglicherweise beim Schreiben andere Zeichen
   erhalten.
4. Drücken Sie die Leertaste in Kombination mit Braillepunkten, um den
   Systemcursor zu bewegen (oder die aktuelle Zeile anzusagen), so, wie wenn
   Sie  eine Braillezeile verwenden. Beispiel: Drücken Sie Leertaste+Punkt1,
   um Pfeil nach oben zu emulieren, Leertaste+Punkt4+Punkt5+Punkt6 um
   Steuerung+Ende zu emulieren, Leertaste+Punkt1+Punkt4 um die aktuelle
   Zeile anzusagen, usw.
5. Drücken Sie NVDA+0, um die Braille-Eingabe auszuschalten..

## Wichtige Anmerkungen

Die Erweiterung verwendet die Einstellung "Braille-Eingabetabelle" aus den
Braille-Einstellungen.

Einige Laptop-Tastaturen können nicht mit gedrückten Tastenkombinationen
umgehen.

## Änderungen für 2020.1

* Sie können die Leertaste in Kombination mit Braillepunkten drücken, um
  Gesten zu emulieren, ähnlich den Befehlen, die in Braille-Displays
  verfügbar sind.
* Es wurde eine Option hinzugefügt, um einzelne Punkte zu sprechen, die im
  Einhandmodus eingegeben wurden.

## Mitwirkende

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pckbbrl

[2]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-o

# Braille-Eingabe via PC-Tastatur #

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Lizenz: GNU Allgemeine Öffentliche Lizenz Version 2.0

Diese NVDA-Erweiterung ermöglicht die Eingabe von Braille über die
PC-Tastatur. Momentan werden folgende Tastaturschemata unterstützt:

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

Wenn Sie möchten, dass beim Tippen mit einer Hand automatisch Punkte
gesendet werden, verwenden Sie den Regler, um eine Zeitüberschreitung größer
als 0 einzustellen.

Außerdem können Sie einstellen, welche Zeichen beim einhändigen Tippen
gesendet, gelöscht und mit Punkten versehen werden sollen, und welche
Zeichen im Einhand- oder Standardmodus ignoriert werden sollen.

Es ist auch möglich, die Standard-Einstellungen in den Einstellungen der
NVDA-Erweiterung wiederherzustellen.

## Verwendung

1. Drücken Sie NVDA+0, um die Braille-Eingabe zu aktivieren. Die Geste
   können Sie im Dialog Tastenbefehle in der Kategorie Braille ändern.
2. Tippen Sie Braille auf der PC-Tastatur indem Sie Tasten zusammen drücken,
   wie Sie es auf einer Braille-Tastatur machen.

	* Wenn Sie Text mit beiden Händen eingeben, verwenden Sie die folgenden
	  Tasten auf einer deutschen QWERTZ-Tastatur oder die Tasten an der
	  entsprechenden Stelle bei anderen Schemata:

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

## Changes for 44.0.0

* Added kannada.cti table.

## Änderungen in 28.0.0

* Die Standardwerte für den Ein-Hand-Modus wurden geändert.

## Änderungen in 2023.02.23

* Es wurde die Möglichkeit hinzugefügt, Tasten zu konfigurieren, die für die
  Eingabe von Punkten im Einhandmodus verwendet werden.
* Jetzt können Sie Tasten konfigurieren, die bei der Braille-Eingabe
  ignoriert werden sollen.
* Eine Schaltfläche zum Wiederherstellen der Standardeinstellungen wurde zum
  Einstellungsfenster der NVDA-Erweiterung hinzugefügt.
* Kompatibel mit NVDA 2023.1.

## Änderungen in 2022.1

* Es besteht jetzt die Möglichkeit, Tasten zum Senden und Löschen von
  Punkten beim Schreiben mit einer Hand zu konfigurieren. Es ist auch
  möglich, eine Zeitüberschreitung einzustellen, um Punkte automatisch zu
  senden, ohne Bestätigung die Tasten zu drücken.

## Änderungen in 2021.1

* NVDA liest keine Punkte vor, wenn der Einhandmodus nicht aktiv ist oder
  wenn die Leertaste gedrückt wurde.
* Kompatibel mit NVDA 2021.1.

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


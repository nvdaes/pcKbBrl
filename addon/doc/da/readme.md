# Indtast punkt med PC-tastatur og NVDA #

* Forfatter: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2022 NV Access Limited, Noelia Ruiz Martínez
* Licens: GNU General Public License version 2.0
* Download: [stabil version][1] (kompatibel med NVDA 2019.3 eller nyere)
* Download: [udviklingsversion][2] (kompatibel med NVDA 2019.3 eller nyere)
* [version 2014.1] [3] (kompatibel med NVDA 2017.3 til 2019.2)

Denne NVDA-tilføjelse gør det muligt at indtaste punktskrift via
pc-tastaturet. I øjeblikket understøttes følgende tastaturlayouter:

* Engelsk QWERTY -tastatur.
* Fransk (Frankrig).
* Tysk (Tyskland).
* Italiensk (Italien).
* Persisk.
* Portugisisk (Portugal).
* Spansk (Spanien og Mexico).
* Tyrkisk.

## Sådan konfigureres tilføjelsen

Tilføjelsen kan konfigureres fra den tilsvarende kategori i NVDAs
indstillinger. En tastaturkommando kan ligeledes tildeles denne tilføjelse
under "Håndter kommandoer" i NVDA-menuen ved at vælge punktet "Opsætning".

Marker det tilsvarende afkrydsningsfelt, hvis du kun vil skrive med én hånd,
eller sørg for, at det ikke er markeret, hvis du foretrækker at skrive med
standardtilstand (to hænder).

Du kan også vælge, om NVDA skal oplæse hvert enkelt indtastede punkt (ved
hjælp af funktionen "enhåndstilstand").

## Sådan bruges tilføjelsen

1. Tryk på NVDA+0 for at aktivere punktskrift. Denne kommando kan ændres fra
   dialogboksen Håndter kommandoer, punktskriftskategori.
2. Skriv punktskrift ved at trykke tasterne på pc -tastaturet, som var det
   et punktskriftstastatur.

	* Hvis du vil indtaste tekst med to hænder, skal du bruge følgende taster,
	  hvis du arbejder med et QWERTY engelsk tastatur eller tasterne placeret
	  på de tilsvarende positioner i andre layout:

		* f, d og s for henholdsvis punkt 1, 2 og 3.
		* j, k og l for henholdsvis punkterne 4, 5 og 6.
		* Brug tasterne a og æ for henholdsvis punkterne 7 og 8.
		* Du kan også bruge tasterne på rækken ovenfor,  dvs. q, w, e, r, u, i, o
		  og p.

	* Hvis du vil skrive tekst med én hånd, kan du komponere tegn ved at trykke
	  på tasterne samtidigt eller i flere tastetryk og tilføje de punkter, der
	  svarer til det ønskede tegn. Tryk på g eller h for at skrive tegnet, når
	  du har skrevet alle dets punkter. Hvis du laver en fejl under
	  indtastningen af punkterne for det ønskede tegn, kan du slette punkterne,
	  før du skriver det ved at trykke på t eller y. De taster, der bruges på
	  QWERTY engelsk tastatur, er følgende:

		* Venstre hånd: f, d, s, r, e, w, a, q for punkterne 1, 2, 3, 4, 5, 6, 7
		  og 8.
		* Højre hånd: j, k, l, u, i, o,æ, p for punkterne 1, 2, 3, 4, 5, 6, 7 og
		  8.

3. Du kan trykke på de fleste andre taster som normalt, herunder mellemrum,
   backspace, enter og funktionstaster. Pas på ikke at trykke på alt+shift,
   da ændring af tastaturlayoutet kan påvirke de indtastningen af
   punktskrift.
4. Tryk på mellemrumstasten i kombination med punkter for at flytte
   systemmarkøren (eller rapportere den aktuelle linje), som hvis du brugte
   et punktdisplay. For eksempel mellemrum+punkt1 for at emulere pil op,
   mellemrum+punkt4+punkt5+punkt6 for at emulere Ctrl+end,
   mellemrum+punkt1+punkt4 for at rapportere den aktuelle linje osv.
5. Tryk på NVDA+0 for at deaktivere punktindtastning.

## Vigtige bemærkninger:

Denne tilføjelse bruger NVDAs indbyggede punktskrift. Derfor er den anvendte
indtastningstabel den, der er angivet i NVDAs punktindstillinger.

Nogle tastaturer, især bærbare tastaturer, kan ikke håndtere bestemte
kombinationer af taster, der trykkes ned. Når dette sker, ignoreres visse
nøgler simpelthen. Desværre er der ikke noget, der kan gøres for at løse
dette, da tasterne simpelthen aldrig modtages af Windows eller NVDA. I nogle
tilfælde kan det være en hjælp at bruge den øverste række af taster med én
eller begge hænder, da dit tastatur muligvis tillader disse taster.

## Changes for 2021.1

* NVDA won't try to speak dots when One hand mode is not active or if space
  has been pressed.
* Compatible with NVDA 2021.1.

## Ændringer for 2020.1

* Du kan trykke på mellemrumstasten i kombination med punktskriftspunkter
  for at efterligne bevægelser, der ligner kommandoer, der er tilgængelige
  på punktdisplays.
* Tilføjet en mulighed for at tale enkelte punkter skrevet i
  enhåndstilstand.

## Bidragsydere

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


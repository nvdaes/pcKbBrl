# PC Keyboard Braille Input for NVDA #

* Autorzy: NV Access Limited, Noelia Ruiz Martínez
* Wszelkie prawa zastrzeżone: 2012-2019 NV Access Limited, Noelia Ruiz
  Martínez
* Licencja: GNU General Public License version 2.0
* Pobierz: [Wersja stabilna][1] (compatible with NVDA 2019.3 or later)
* Pobierz: [Wersja rozwojowa][2] (compatible with NVDA 2019.3 or later)
* [Wersja 2014.1][3] (zgodna z NVDA 2017.3 do 2019.2)

Ten dodatek umożliwia wprowadzanie brajla za pomocą klawiatury
komputera. Obecnie wspierane są następujące układy klawiatury:

* Angielska klawiatura qwerty.
* Francuzki (Francja).
* Niemiecki (Niemcy).
* Włoski (Włochy).
* Perski
* Portugalski (Portugalia).
* Hiszpański (Hiszpania i Meksyk).
* Turecki.

## Jak ustawić

Dodatek można ustawić z poziomu odpowiedniej kategorii w ustawieniach NVDA
(menu główne NVDA, menu rozwijane Ustawienia). Polecenie, które otwiera
panel ustawień dodatku, można przypisać z poziomu Zdarzeń Wejścia, kategoria
ustawień.

Aby pisać jedną ręką, zaznacz odpowiednie pole wyboru. Jeśli wolisz pisać w
trybie standardowym, czyli oburącz, upewnij się, że nie jest ono zaznaczone.

W trybie jednej ręki można też określić, czy NVDA ma wymawiać każdy
wpisywany punkt.

## Jak używać

1. Naciśnij NVDA+0 aby włączyć wprowadzanie brajla. To polecenie można
   zmienić z poziomu Zdarzeń Wejścia, kategoria brajla.
2. Wprowadzaj brajl naciskając jednocześnie klawisze na klawiaturze
   komputera, jakgdyby była to klawiatura brajlowska.

	* Aby pisać oburącz, użyj następujących klawiszy dla angielskiej klawiatury
	  QWERTY lub odpowiadających im pozycją klawiszy w innych układach:

		* f, d oraz s dla punktów 1, 2 i 3.
		* j, k oraz l dla punktów 4, 5 i 6.
		* A i ; (średnik) dla punktów 7 i 8.
		* Można też używać klawiszy umieszczonych o rząd wyżej, np. q, w, e, r, u,
		  i, o oraz p.

	* Aby pisać jedną ręką, można układać znaki naciskając klawisze
	  jednocześnie lub każdy oddzielnie. Pojedynczo dodaje się punkty, z
	  których składa się rządany znak. Następnie należy nacisnąć g lub h aby
	  wpisać cały znak po dodaniu wszystkich jego punktów. W razie pomyłki
	  podczas układania znaku, można wyczyścić niewłaściwe punkty przed
	  wprowadzeniem całego znaku naciskając t lub y. Dla angielskiej klawiatury
	  QWERTY używane są następujące klawisze:

		* Lewa ręka: f, d, s, r, e, w, a, q dla punktów 1, 2, 3, 4, 5, 6, 7 i 8.
		* Prawa ręka: j, k, l, u, i, o, ; (średnik), p dla punktów 1, 2, 3, 4, 5,
		  6, 7 i 8.

3. Większość pozostałych klawiszy, takich jak spacja, backspace, enter lub
   klawisze funkcyjne działa bez zmian. Należy jednak uważać, aby nie
   wcisnąć polecenia alt+shift, ponieważ zmiana układu klawiatury może mieć
   wpływ na wprowadzane punkty.
4. Naciskaj spację wraz z poszczególnymi punktami brajla, aby przemieszczać
   kursor systemowy lub odczytać bieżącą linię, tak jak przy użyciu monitora
   brajlowskiego. Na przykład, spacja+punkt1 emuluje strzałkę w górę,
   spacja+punkt4+punkt5+punkt6 emuluje control+end, spacja+punkt1+punkt4
   odczytuje bieżącą linię, ITD.
5. Aby wyłączyć wprowadzanie brajla, naciśnij NVDA+0.

## Ważne uwagi

Dodatek używa wbudowanego w NVDA wsparcia wprowadzania brajla. Dlatego
domyślną tablicą wejścia jest ta, którą użytkownik wybrał w ustawieniach
brajla NVDA.

Niektóre klawiatury, szczególnie klawiatury laptopów, nie obsługują
niektórych kombinacji klawiszy naciśniętych jednocześnie.  Jeśli to się
zdarzy, niektóre klawisze są po prostu ignorowane.  Niestety nie da się nic
zrobić, aby to naprawić, ponieważ te klawisze nigdy nie trafiają do Windows
czy NVDA.  W niektórych przypadkach może pomóc użycie górnego rzędu klawiszy
jedną lub obiema rękami, ponieważ twoja klawiatura może zezwalać na te
klawisze.

## Zmiany dla wersji NVDA 2020.1

* Można naciskać spację z poszczególnymi punktami brajla, aby emulować
  polecenia podobne do tych, które są dostępne w monitorach brajlowskich.
* Dodano możliwość wymawiania pojedynczych punktów wprowadzanych w trybie
  jednej ręki.

## Współpracownicy

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


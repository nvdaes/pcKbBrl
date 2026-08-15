# Brajev unos sa tastature računara za NVDA #

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licenca: GNU General Public License verzija 2.0

Ovaj NVDA dodatak dozvoljava brajev unos korišćenjem tastature
računara. Trenutno, sledeći rasporedi tastature su podržani:

* Engleska Qwerty tastatura.
* Francuski (Francuska ).
* Nemački (Nemačka ).
* Italijanski (Italija ).
* Persijski.
* Portugalski (Portugal ).
* Španski (Španija i Meksiko ).
* Turski.

## Kako podesiti

Dodatak se može podesiti iz kategorije njegovih podešavanja u dijalogu sa
NVDA podešavanjima, iz NVDA menija, podmeni opcije. Prečica za otvaranje
njegovog panela sa podešavanjima se takođe može podesiti iz dijaloga ulazne
komande, kategorija podešavanja.

Označite odgovarajuće izborno polje ako želite da pišete jednom rukom, ili
se uverite da nije označeno ako želite da pišete na standardan način
(korišćenjem obe ruke ).

Možete takođe da označite da li će NVDA izgovarati svaku otkucanu tačkicu
(ako se koristi opcija "pisanja jednom rukom ").

If you want dots to be sent automatically when typing with one hand, use the
spin control to set a timeout greater than 0.

In addition, you can set the characters to send, clear and compose dots when
typing with one hand, as well as characters to be ignored in one hand or
standard mode.

It's also possible to restore defaults in the add-on settings panel.

## Kako koristiti

1. Pritisnite NVDA plus 0 da biste omogućili brajev unos. Ova prečica se
   može promeniti u dijalogu ulazne komande, kategorija brajev.
2. Pišite brajev unos pritiskanjem tastera na tastaturi računara zajedno kao
   da je brajeva tastatura.

	* Ako želite da pišete tekst sa dve ruke, koristite sledeće tastere ako
	  koristite Englesku Qwerty tastaturu, ili tastere koji se nalaze na
	  odgovarajućim pozicijama na drugim tastaturama:

		* f, d i s za tačkice 1, 2 i 3.
		* j, k i l za tačkice 4, 5 i 6.
		* Koristite tastere a i ; (tačkazarez) za tačkice 7 i 8.
		* Možete takođe da koristite tastere na redu iznad ; q, w, e, r, u, i, o i
		  p.

	* Ako želite da pišete tekst jednom rukom, možete da pišete tekst
	  upisivanjem tačkica jednu po jednu ili u isto vreme, dok se ne dodaju sve
	  tačkice za odgovarajući znak. Pritisnite G ili H da upišete znak nakon
	  što ste dodali sve njegove tačkice. Ako pogrešite pri dodavanju tačkica,
	  možete obrisati tačkice pre upisivanja tasterima T ili Y. Tasteri koji se
	  koriste na Engleskoj Qwerty tastaturi su sledeći:

		* Leva ruka: f, d, s, r, e, w, a, q za tačkice 1, 2, 3, 4, 5, 6, 7 i 8.
		* Desna ruka: j, k, l, u, i, o, ; (tačkazarez ), p za tačkice 1, 2, 3, 4,
		  5, 6, 7 i 8.

3. Možete koristiti većinu drugih tastera na njihov standardan način, što
   uključuje razmak, tastere za brisanje, enter i funkcijske
   tastere. Obratite pažnju da ne pritiskate kombinaciju alt plus šift,
   budući da menjanje rasporeda tastature može uticati na upisane tačkice.
4. Pritisnite razmak zajedno sa brajevim tačkicama da pomerate sistemski
   kursor (ili saznate trenutni red ), kao da koristite brajev red. Na
   primer, razmak plus tačkica 1 da emulirate strelicu gore, razmak plus
   tačkica 1 +tačkica 5 +tačkica 6 da emulirate kombinaciju kontrol plus
   end, razmak plus tačkica 1 +tačkica 4 da biste saznali trenutni red, i
   slično.
5. Pritisnite NVDA plus 0 da onemogućite brajev unos.

## Važne napomene

Ovaj  dodatak koristi ugrađenu NVDA podršku za brajev unos. S toga, tabela
za unos je ona koja se odredi u NVDA dijalogu brajevih podešavanja.

Neke tastature, posebno laptop tastature, ne mogu da izvrše kombinacije
pritiskanja određenih tastera.  Kada se ovo desi, određeni tasteri se
jednostavno ignorišu.  Nažalost, ništa se ne može uraditi da se ovo ispravi,
budući da tastere ne prima ni Windows ni NVDA.  U nekim slučajevima,
korišćenjem gornjeg reda tastera sa jednom ili obe ruke može pomoći, budući
da će vaša tastatura možda dozvoliti ove tastere.

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

* Added ability to configure keys to send and clear dots when writing with
  one hand. Also, it's possible to set a timeout to send dots automatically,
  without pressing confirmation keys.

## Changes for 2021.1

* NVDA won't try to speak dots when One hand mode is not active or if space
  has been pressed.
* Compatible with NVDA 2021.1.

## Promene u 2020.1

* Možete pritisnuti razmak zajedno sa brajevim tačkicama za emuliranje
  prečica, slično komandama dostupnim na brajevom redu.
* Dodata opcija za izgovor pojedinačnih tačkica upisanih u režimu pisanja
  jednom rukom.

## Saradnici

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]


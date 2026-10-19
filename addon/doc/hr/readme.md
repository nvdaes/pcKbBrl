# Brajični unos PC tipkovnicom za NVDA (PC Keyboard Braille Input for NVDA) #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licenca: GNU opća javna licenca verzija 2.0

Ovaj dodatak dozvoljava brajični unos pomoću PC tipkovnice. Trenutačno se
podržavaju sljedeće tipkovnice:

* Engleska QWERTY tipkovnica.
* Francuska (Francuska).
* Njemačka (Njemačka).
* Talijanska (Italija).
* Perzijska.
* Portugalska (Portugal).
* Španjolska (Španjolska i Meksiko).
* Turska.

## Kako podesiti

Dodatak se može podesiti u njegovoj kategoriji u dijaloškom okviru NVDA
postavki, u NVDA izborniku, u podizborniku Postavke. Gesta za otvaranje
ploče postavki dodatka se može dodijeliti u dijaloškom okviru Ulazne geste,
u kategoriji konfiguracije.

Označi odgovarajući potvrdni okvir, ako želiš tipkati samo jednom rukom ili
ga odznači, ako radije koristiš standardni način (s dvije ruke).

Moguće je odabrati, hoće li NVDA izgovarati jednu utipkanu točku (koristeći
funkciju „jednoručni modus”).

Ako želiš da se točkice šalju automatski kad tipkaš jednom rukom, koristi
kontrolu za postavljanje vremenskog ograničenja većeg od 0.

Osim toga, možeš postaviti znakove za slanje, brisanje i sastavljanje
točkica prilikom jednoručnog tipkanja kao i znakove koji se zanemaruju
prilikom jednoručnog ili standardnog tipkanja.

Također je moguće obnoviti standardne vrijednosti u ploči postavki dodataka.

## Kako koristiti

1. Pritisni NVDA+0 za aktiviranje brajičnog unosa. Ova se gesta može
   promijeniti u dijaloškom okviru Ulazne geste, u kategoriji Brajica.
2. Tipkaj brajicu istovremenim pritiskanjem tipki na PC tipkovnici, kao da
   se radi o brajičnoj tipkovnici.

	* Ako želiš upisati tekst s dvije ruke, koristi sljedeće tipke, ako radiš s
	  engleskom QWERTY tipkovnicom ili tipke koje se nalaze na odgovarajućim
	  položajima u drugim rasporedima:

		* f d s za točkice 1 2 3.
		* j k l za točkice 4 5 6.
		* Koristi tipke a ; za točkice 7 8.
		* Možeš koristiti i tipke u gornjem redu: q w e r u i o p.

	* Ako tekst želiš tipkati jednom rukom, možeš sastaviti znakove
	  istovremenim pritiskanjem tipki ili pritiskanjem tipki pojedinačno,
	  dodajući točkice koje odgovaraju željenom znaku. Pritisni g ili h za
	  tipkanje znaka kad su dodane sve točkice. Ako pogriješiš prilikom
	  sastavljanja znaka, točkice možeš ukloniti prije nego što se utipkaju,
	  pritiskom tipke t ili y. Tipke koje se koriste na engleskoj QWERTY
	  tipkovnici su:

		* Lijeva ruka: f d s r e w a q za točkice 1 2 3 4 5 6 7 8.
		* Desna ruka: j k l u i o ; p za točkice 1 2 3 4 5 6 7 8.

3. Možeš pritisnuti većinu ostalih tipki kao i obično, uključujući
   razmaknicu, backspace, enter i funkcijske tipke. Pazi da ne pritisneš
   alt+šift, jer promjena rasporeda tipkovnice može utjecati na utipkane
   točkice.
4. Pritisni razmaknicu u kombinaciji s brajevim točkicama za pomicanje
   sustavskog pokazivača (ili prijavi trenutačni redak), kao da koristiš
   brajični prikaz. Na primjer, razmak+točkica1 za oponašanje strelice gore,
   razmak+točkica4+točkica5+točkica6 za oponašanje kontrol+kraj,
   razmak+točkica1+točkica4 za izvještavanje o trenutaćnom retku itd.
5. Pritisni NVDA+0 za deaktiviranje brajičnog unosa.

## Važne napomene

Ovaj dodatak koristi u NVDA čitaču ugrađenu podršku za brajični unos. Stoga
se koristi ulazna brajična tablica, koja je definirana u dijaloškom okviru
postavki za brajicu.

Neke tipkovnice, osobito tipkovnice prijenosnih računala ne dozvoljavaju
određene tipkovničke kombinacije. U tim slučajevima se pojedine tipke
jednostavno zanemaruju. Nažalost, ovaj problem nije moguće riješiti, jer se
tipke jednostavno ne prepoznaju od strane Windowsa ili NVDA čitača. U nekim
slučajevima pomaže korištenje tipki gornjeg reda, ovisno o mogućnostima
tipkovnice.

## Changes for 44.0.0

* Added kannada.cti table.

## Promjene za 28.0.0

* Promijenjene su standardne vrijednosti za jednoručni način rada.

## Promjene za 2023.02.23

* Dodana je mogućnost konfiguriranja tipki za jednoručno tipkanje točkica.
* Sada možeš konfigurirati tipke koje se zanemaruju prilikom tipkanja
  brajičnih znakova.
* U ploču postavki dodataka je dodan gumb za obnavljanje standardnih
  postavki.
* Kompatibilno s NVDA čitačem 2023.1.

## Promjene za 2022.1

* Dodana je mogućnost konfiguriranja tipki za slanje i brisanje točaka
  prilikom pisanja jednom rukom. Također, moguće je postaviti vremensko
  ograničenje za automatsko slanje točaka, bez pritiskanja tipki za potvrdu.

## Promjene za 2021.1

* NVDA neće pokušati izgovoriti točke kad način rada jednom rukom nije
  aktivan ili ako je pritisnuta razmaknica.
* Kompatibilno s NVDA čitačem 2021.1.

## Promjene za 2020.1

* Pritisni razmaknicu zajedno s brajevim točkama za oponašanje gesta, slično
  naredbama dostupnim na brajevim erkanima.
* Dodana je mogućnost izgovaranja pojedinačnih točkica utipkanih u
  jednoručnom modusu.

## Doprinositelji

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]


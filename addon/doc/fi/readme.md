# Pistekirjoituksen syöttäminen tietokoneen näppäimistöllä #

* Tekijät: NV Access Limited, Noelia Ruiz Martínez
* Tekijänoikeus: 2012-2022 NV Access Limited, Noelia Ruiz Martínez
* Lisenssi: GNU General Public License versio 2.0
* Lataa: [vakaa versio][1] (yhteensopiva NVDA 2019.3:n ja uudempien kanssa)
* Lataa: [kehitysversio][2] (yhteensopiva NVDA 2019.3:n ja uudempien kanssa)
* [versio 2014.1][3] (yhteensopiva NVDA 2017.3:sta 2019.2:een)

Tämän lisäosan avulla voidaan kirjoittaa pistekirjoitusta tietokoneen
näppäimistöä käyttäen.  Tällä hetkellä tuetaan seuraavia
näppäimistöasetteluja:

* Englanninkielinen QWERTY-näppäimistö.
* Ranska (Ranska).
* Saksa (Saksa).
* Italia (Italia).
* Persia.
* Portugali (Portugali).
* Espanja (Espanja ja Meksiko).
* Turkki.

## Asetusten määrittäminen

Lisäosan asetukset voidaan määrittää omasta kategoriastaan NVDA:n
asetusvalintaikkunassa (NVDA-valikko -> Asetukset-alivalikko). Lisäosan
asetuspaneelin avaamiseen on mahdollista määrittää näppäinkomento
Näppäinkomennot-valintaikkunan Asetukset-kategoriasta.

Mikäli haluat kirjoittaa yksikätisesti, valitse sitä vastaava valintaruutu,
tai varmista, ettei se ole valittuna, mikäli kirjoitat mieluummin
standarditilassa (molemmilla käsillä).

Voit myös valita, puhuuko NVDA yksittäisen syötetyn pisteen (yksikätistä
tilaa käyttäen).

Jos haluat, että pisteet lähetetään automaattisesti yhdellä kädellä
kirjoitettaessa, aseta kiertosäätimellä aikakatkaisuksi suurempi kuin 0.

Lisäksi voit määrittää pisteitä lähettävät ja poistavat merkit yhdellä
kädellä kirjoitettaessa.

## Käyttö

1. Ota pistekirjoituksen syöttö käyttöön painamalla NVDA+0. Tätä
   näppäinkomentoa on mahdollista muuttaa Näppäinkomennot-valintaikkunan
   Pistekirjoitus-kategoriasta.
2. Kirjoita pistekirjoitusta painamalla samanaikaisesti useita näppäimiä
   tietokoneen näppäimistöltä, ikään kuin se olisi
   pistekirjoitusnäppäimistö.

	* Mikäli haluat kirjoittaa tekstiä molemmilla käsillä, käytä seuraavia
	  näppäimiä, jos  käytät englantilaista QWERTY-näppäimistöä tai muiden
	  asettelujen vastaavissa kohdissa sijaitsevia näppäimiä:

		* f, d ja s pisteille 1, 2 ja 3.
		* j, k ja l pisteille 4, 5 ja 6.
		* Käytä näppäimiä a ja ; (puolipiste) pisteille 7 ja 8.
		* Voit myös käyttää niiden ylöpuolella olevan rivin näppäimiä, ts. q, w,
		  e, r, u, i, o ja p.

	* Mikäli haluat kirjoittaa tekstiä yksikätisesti, voit syöttää merkit joko
	  painamalla näppäimiä samanaikaisesti tai useilla painalluksilla, lisäten
	  haluttua merkkiä vastaavat pisteet. Kirjoita merkki painamalla g tai h,
	  kun olet lisännyt kaikki sen pisteet. Mikäli teet virheen merkkiä
	  muodostaessasi, voit tyhjentää pisteet syöttämättä merkkiä painamalla t
	  tai y. Englanninkielisessä QWERTY-näppäimistössä käytetään seuraavia
	  näppäimiä:

		* Vasen käsi: f, d, s, r, e, w, a, q pisteille 1, 2, 3, 4, 5, 6, 7 ja 8.
		* Oikea käsi: j, k, l, u, i, o, ; (puolipiste), p pisteille 1, 2, 3, 4, 5,
		  6, 7 ja 8.

3. Useimpia muita näppäimiä voit painaa normaalisti, mukaan lukien Väli,
   Askelpalautin, Enter sekä funktionäppäimet. Pidä huoli, ettet paina
   Alt+Vaihto-näppäinyhdistelmää, koska näppäimistöasettelun vaihtaminen voi
   vaikuttaa syötettyihin pisteisiin.
4. Siirrä järjestelmäkohdistinta (tai puhu nykyinen rivi) painamalla
   Väli-näppäintä yhdessä pistekirjoituspisteiden kanssa, aivan kuten
   pistenäyttöä käyttäessäsi. Esim. väli+piste 1 jäljittelee ylänuolta,
   väli+piste 4+piste 5+piste 6 Ctrl+End-näppäimiä, väli+piste 1+piste 4
   puhuu nykyisen rivin jne.
5. Poista pistekirjoituksen syöttö käytöstä painamalla NVDA+0.

## Tärkeitä huomautuksia

Tämä lisäosa käyttää NVDA:n sisäänrakennettua pistekirjoituksen syötön
tukea.  Tämän vuoksi syöttötaulukkona käytetään NVDA:n Pistenäytön asetukset
-valintaikkunassa määritettyä taulukkoa.  NVDA tukee tällä hetkellä vain
tietokonemerkistöä, joten rajoitus koskee myös tätä lisäosaa.

Jotkin näppäimistöt, erityisesti kannettavien,, eivät pysty käsittelemään
määrättyjen yhdistelmien painamista.  Kun tätä tapahtuu, näppäinpainallukset
yksinkertaisesti ohitetaan.  Valitettavasti tämän asian korjaamiseksi ei ole
tehtävissä mitään, koska Windows tai NVDA ei yksinkertaisesti ota vastaan
näitä näppäinpainalluksia.  Ylärivin näppäinten käyttäminen jommallakummalla
tai molemmilla käsillä saattaa joissain tapauksissa auttaa , koska
näppäimistö saattaa sallia näiden näppäinten painamisen.


## Muutokset versiossa 2022.1
* Lisätty mahdollisuus pisteitä lähettävien ja poistavien näppäinten
  määrittämiseen yhdellä kädellä kirjoitettaessa. Lisäksi on mahdollista
  määrittää aikakatkaisu, jonka kuluttua pisteet lähetetään automaattisesti
  ilman vahvistusnäppäinten painamista.

## Muutokset versiossa 2021.1

* NVDA ei yritä puhua pisteitä, kun yksikätinen tila ei ole käytössä tai
  mikäli välilyöntiä on painettu.
* Yhteensopiva NVDA 2021.1:n kanssa.

## Muutokset versiossa 2020.1

* Voit jäljitellä näppäinkomentoja samoin kuin pistenäyttöjen komentoja
  painamalla Väli-näppäintä yhdessä pistekirjoituspisteiden kanssa.
* Lisätty asetus yksittäisten pisteiden puhumiselle yksikätisessä tilassa.

## Avustajat

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

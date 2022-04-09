# PC Keyboard Braille Input for NVDA #

* Autori: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2022 NV Access Limited, Noelia Ruiz Martínez
* Licenza: GNU General Public License versione 2.0
* Scarica: [versione stabile][1] (compatibile con NVDA 2019.3 o versioni
  successive)
* [versione in sviluppo][2] (compatibile con NVDA 2019.3 o versioni
  successive)
* [versione 2014.1][3] (compatibile con NVDA da 2017.3 a 2019.2)

Questo componente aggiuntivo per NVDA permette di inserire caratteri braille
utilizzando la tastiera del pc. Al momento, sono supportati i seguenti
layout tastiera:

* Tastiera inglese QWERTY.
* Francese (Francia).
* Tedesca (Germania).
* Italiana (Italia).
* Persiana.
* Portoghese (Portogallo).
* Spagnola (Spagna e  Messico).
* Turca.

## Come configurarlo

L'add-on può essere configurato dalla sua categoria nella finestra
Impostazioni di NVDA, nel menù di NVDA, sottomenù Preferenze. Dalla finestra
Gesti e Tasti di Immissione di NVDA, categoria Configurazione, è possibile
assegnare un tasto per aprire la finestra delle impostazioni dell'add-on.

Attivate la casella di controllo corrispondente se volete digitare
utilizzando una sola mano, o assicuratevi che non sia attivata se preferite
digitare utilizzando la modalità standard (due mani).

Potete anche scegliere se NVDA deve vocalizzare ogni singolo punto digitato
quando utilizzate la modalità a una mano.

## Come si usa

1. Premete NVDA+0 per attivare l'input Braille. Questo tasto può essere
   modificato dalla finestra Gesti e Tasti di Immissione, categoria Braille.
2. Scrivete in Braille premendo i tasti insieme sulla tastiera del pc, come
   se fosse una dattilobraille.

	* Se volete inserire il testo utilizzando due mani, usate i seguenti tasti
	  se lavorate con una tastiera inglese QWERTY, oppure i tasti che si
	  trovano nella posizione corrispondente in altri layout:

		* f, d ed s per i punti 1, 2 e 3 rispettivamente.
		* j, k ed l per i punti 4, 5 e 6 rispettivamente.
		* Usate i tasti a e punto e virgola (o accentata in Italia) per i punti 7
		  ed 8 rispettivamente.
		* Potete anche usare i tasti posti nella riga superiore; ad esempio q, w,
		  e, r, u, i, o e p.

	* Se volete digitare del testo utilizzando una mano, potete comporre i
	  caratteri premendo i tasti contemporaneamente o in diversi sottogruppi,
	  aggiungendo i punti corrispondenti ai caratteri desiderati. Premete g o h
	  per inserire il carattere quando avete aggiunto tutti i suoi punti. Se
	  fate un errore mentre costruite un carattere, potete cancellarne i punti
	  prima di digitarlo premendo t o y. I tasti utilizzati nella tastiera
	  inglese QWERTY sono i seguenti:

		* Mano sinistra: f, d, s, r, e, w, a, q per i punti 1, 2, 3, 4, 5, 6, 7 e
		  8.
		* Mano destra: j, k, l, u, i, o, punto e virgola (o accentata in Italia),
		  p per i punti 1, 2, 3, 4, 5, 6, 7 e 8.

3. Potete premere la maggior parte degli altri tasti come al solito, inclusi
   spazio, backspace, invio e i tasti funzione. Fate attenzione a non
   premere alt+shift, perché la modifica del layout tastiera può influire
   sui punti inseriti.
4. Premete la barra spaziatrice insieme ai punti Braille per spostare il
   cursore (o leggere la riga corrente), come se utilizzaste un display
   Braille. Per esempio, spazio+punto1 per simulare la freccia su,
   spazio+punti456 per simulare control+end, spazio+punti14 per leggere la
   riga corrente, ecc.
5. Premete NVDA+0 per disattivare l'input Braille.

## Note importanti

Questo componente aggiuntivo utilizza il supporto interno di NVDA per
l'input Braille. Pertanto, la tabella di input utilizzata è quella
specificata nella finestra di dialogo di NVDA Impostazioni Braille. NVDA
supporta solo il computer braille in ingresso al momento, quindi questa
limitazione si applica anche a questo add-on.

Alcune tastiere, in particolare le tastiere dei portatili, non possono
gestire determinate combinazioni di tasti. Quando questo accade, alcuni
tasti sono semplicemente ignorati. Purtroppo, non c'è nulla che si possa
fare per risolvere questo problema, in quanto i tasti semplicemente non
vengono mai ricevuti da Windows o NVDA. In alcuni casi, utilizzare i tasti
della riga superiore con una o entrambe le mani potrebbe aiutare, perché la
vostra tastiera potrebbe gestirli.

## Changes for 2021.1

* NVDA won't try to speak dots when One hand mode is not active or if space
  has been pressed.
* Compatible with NVDA 2021.1.

## Novità nella versione 2020.1

* Potete premere la barra spaziatrice insieme ai punti Braille per simulare
  alcune combinazione di tasti, in analogia con i comandi disponibili sui
  display Braille.
* Aggiunta un'opzione per vocalizzare i singoli punti digitati in modalità a
  una mano.

## Collaboratori

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


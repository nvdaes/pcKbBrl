# PC Keyboard Braille Input for NVDA #

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* License: GNU General Public License version 2.0

Este complemento de NVDA permite a entrada de braille a través do teclado do
PC.  Actualmente, sopórtanse as seguintes distribucións de teclado:

* Teclado inglés QWERTY.
* Francés (Francia).
* Alemán (Alemaña).
* Italiano (Italia).
* Persa.
* Portugués (Portugal).
* Español (España e México).
* Turco.

## Como configuralo

O complemento pódese configurar dende a súa categoría no diálogo de opcións
de NVDA, baixo o menú de NVDA; submenú Preferencias. Pódese asignar un xesto
para abrir o panel de opcións do complemento dende o diálogo Xestos de
entrada, categoría configuración.

Marca a caixa de verificación correspondente se desexas escribir utilizando
só unha man, ou asegúrate de que non está marcada se desexas escribir
utilizando o modo estándar (dúas mans).

Tamén podes seleccionar se NVDA debe falar un só punto escrito (usando a
característica "modo de unha soa man").

Se queres que os puntos se envíen automaticamente ó escribir cunha soa man,
utiliza o control rotatorio para configurar un tempo de espera maior que 0.

Ademais, podes configurar os caracteres para enviar, limpar e compoñer os
puntos ó escribir cunha soa man, así como os caracteres a ignorar no modo
dunha man ou no modo estándar.

Tamén é posible restaurar as predeterminadas no panel de opcións do
complemento.

## Como se Usa

1. Preme NVDA+0 para activar a entrada braille. Este xesto pódese cambiar
   dende o diálogo Xestos de entrada, categoría braille.
2. Escribe braille premendo á vez as teclas no teclado do PC como se fose un
   teclado braille.

	* Se desexas introducir texto utilizando dúas mans, utiliza as seguintes
	  teclas se traballas cun teclado QWERTY inglés, ou as teclas ubicadas nas
	  posicións correspondentes noutras linguas:

		* f, d e s para os puntos 1, 2 e 3 respectivamente.
		* j, k e l para os puntos 4, 5 e 6 respectivamente.
		* Utiliza as teclas a e ; (punto e coma) para os puntos 7 e 8,
		  respectivamente. Nun teclado español no lugar do punto e coma atópase a
		  ñ.
		* Tamén podes utilizar as teclas na fila de enriba; p.ex. q, w, e, r, u,
		  i, o e p.

	* Se queres escribir texto utilizando unha man, podes compoñer caracteres
	  premendo as teclas simultaneamente ou en varios atallos de teclado,
	  engadindo os puntos correspondentes co carácter desexado:

		* Man esquerda: f, d, s, r, e, w, a, q para os puntos 1, 2, 3, 4, 5, 6, 7
		  e 8.
		* Man dereita: j, k, l, u, i, o, ; (punto e coma, ñ en teclado español), p
		  para os puntos 1, 2, 3, 4, 5, 6, 7 e 8.

3. Podes premer a maioría do resto de teclas con normalidade, incluíndo
   espacio, retroceso, intro e teclas de función. Ten coidado con non premer
   alt+shift, pois cambiar a distribución de teclado podería afectar aos
   puntos introducidos.
4. Preme a barra espaciadora en combinación cos puntos para mover o cursor
   do sistema (ou anunciar a liña actual), simplemente como se estiveses
   utilizando unha pantalla braille. Por exemplo, espazo+punto1 para emular
   frechaArriba, espazo+dot4+dot5+dot6 para emular control+fin,
   espazo+punto1+punto4 para anunciar a liña actual, etc.
5. Preme NVDA+0 para desactivar a entrada braille.

## Notas Importantes

Este complemento usa o Soporte incorporado para a entrada do Braille de
NVDA.  Polo tanto, a táboa de entrada utilizada é a especificada na caixa de
diálogo Opcións de Braille do NVDA.

Algúns teclados, en particular os teclados portátiles, non poden manexar
certas combinacións de teclas a premer. Cando esto aconteza, certas teclas
son simplemente ignoradas. Por desgracia, non hai nada que se poida facer
para solucionar este problema, xa que as teclas simplemente nunca foron
recibidas por Windows ou NVDA. Nalgúns casos, o uso da fila superior de
teclas cunha ou ambas mans pode axudar, así como que o teu teclado pode
permitir estas teclas.

## Changes for 44.0.0

* Added kannada.cti table.

## Cambios para 2022.1

* Changed default values for One hand mode.

## Changes for 2023.02.23

* Engadida a posibilidade de configurar as teclas utilizadas para escribir
  puntos no modo dunha soa man.
* Agora podes configurar teclas que se ignorarán ó escribir en braille.
* Engadiuse un botón para restaurar ás predeterminadas ó panel de opcións do
  complemento.
* Compatible con NVDA 2023.1.

## Cambios para 2022.1

* Engadida a posibilidade de configurar as teclas para enviar e limpar
  puntos ó escribir cunha soa man. Tamén é posible configurar un tempo de
  espera para enviar os puntos automaticamente, sen premer teclas de
  confirmación.

## Cambios para 2021.1

* NVDA non tentará falar os puntos cando o modo dunha soa man non estea
  activo ou se se premeu espazo.
* Compatible con NVDA 2021.1.

## Cambios para 2020.1

* Podes premer a barra espaciadora en combinación cos puntos braille para
  emular xestos, de forma similar a ordes dispoñibles en pantallas braille.
* Engadida unha opción para falar puntos individuais introducidos no modo de
  unha soa man.

## Colaboradores

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]


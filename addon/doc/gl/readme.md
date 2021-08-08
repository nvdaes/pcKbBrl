# PC Keyboard Braille Input for NVDA #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2019 NV Access Limited, Noelia Ruiz Martínez
* License: GNU General Public License version 2.0
* Descargar: [versión estable][1] (compatible con NVDA 2019.3 ou posterior)
* Descargar: [versión de desenvolvemento][2] (compatible con NVDA 2019.3 ou
  posterior)
* [versión 2014.1][3] (compatible con NVDA 2017.3 a 2019.2)

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

[1]: https://addons.nvda-project.org/files/get.php?file=pckbbrl

[2]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pckbbrl-o

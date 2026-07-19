# PC Keyboard Braille Input for NVDA #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licencia: GNU General Public License versión 2.0

Este complemento para NVDA permite introducir braille a través del teclado
del PC.  Actualmente se soportan los siguientes teclado:

* Teclado QWERTY inglés.
* Francés (Francia).
* Alemán (Alemania).
* Italiano (Italia).
* Persa.
* Portugués (Portugal).
* Español (España y México).
* Turco.

## Cómo se configura

El complemento puede configurarse desde su categoría correspondiente del
diálogo de opciones de NVDA yendo al menú NVDA, submenú preferencias. Se
puede asignar un gesto para abrir el panel de opciones de este complemento
desde el diálogo Gestos de entrada, categoría configuración.

Marca la casilla correspondiente si quieres escribir con una sola mano, o
asegúrate de que no está marcada si prefieres escribir usando el modo
estándar (dos manos).

También puedes seleccionar si NVDA debería verbalizar un único punto
tecleado (utilizando la función de "modo de una mano").

Si quieres que se envíen los puntos automáticamente al escribir con una
mano, usa el control giratorio para configurar un tiempo de espera superior
a 0.

Además, puedes configurar los caracteres para enviar, redactar o borrar
puntos al escribir con una mano, así como los caracteres que se ignorarán en
los modos de una mano o estándar.

También es posible restaurar los valores por defecto en el panel de opciones
del complemento.

## Cómo se Utiliza

1. Pulsa NVDA+0 para activar la entrada Braille. Se puede modificar este
   gesto desde el diálogo Gestos de entrada, categoría Braille.
2. Escribe en Braille pulsando las teclas a la vez en el teclado del PC como
   si fuera un teclado Braille.

	* Si quieres introducir texto usando ambas manos, utiliza estas teclas si
	  trabajas con un teclado QWERTY inglés, o las teclas situadas en las
	  posiciones correspondientes en otras distribuciones:

		* f, d y s para los puntos 1, 2 y 3, respectivamente.
		* j, k y l para los puntos 4, 5 y 6, respectivamente.
		* Usa las teclas a y ; (punto y coma) para los puntos 7 y 8,
		  respectivamente.
		* También puedes emplear las teclas de la fila superior; es decir: q, w,
		  e, r, u, i, o y p.

	* Si quieres escribir texto con una sola mano, puedes componer los
	  caracteres pulsando las teclas simultáneamente o en varias pulsaciones,
	  añadiendo los puntos correspondientes al carácter deseado. Pulsa g o h
	  para escribir el carácter cuando hayas añadido todos sus puntos. Si
	  cometes un error construyendo un carácter, puedes eliminar sus puntos
	  antes de escribirlo pulsando t o y. Las teclas usadas en el teclado
	  inglés son las siguientes:

		* Mano izquierda: f, d, s, r, e, w, a, q para los puntos 1, 2, 3, 4, 5, 6,
		  7 y 8.
		* Mano derecha: j, k, l, u, i, o, ; (punto y coma), p para los puntos 1,
		  2, 3, 4, 5, 6, 7 y 8.

3. Puedes pulsar la mayoría de las otras teclas como siempre, incluyendo la
   barra espaciadora, intro, retroceso y las teclas de función. Ten cuidado
   al pulsar alt+shift, ya que cambiar la distribución del teclado puede
   afectar a los puntos introducidos.
4. Pulsa la barra espaciadora en combinación con puntos Braille para mover
   el cursor del sistema (o anunciar la línea actual), como si estuvieras
   usando una pantalla Braille. Por ejemplo, espacio+punto 1 para emular
   flecha arriba, espacio+puntos 4, 5 y 6 para emular control+fin,
   espacio+puntos 1 y 4 para anunciar la línea actual, etc.
5. Pulsa NVDA+0 para desactivar la entrada braille.

## Notas Importantes

Este complemento utiliza el soporte de entrada de Braille de NVDA
incorporado.  Por lo tanto, la tabla de entrada utilizada es la especificada
en el cuadro de diálogo Opciones de Braille de NVDA.

Algunos teclados, en particular los teclados portátiles, no pueden manejar
ciertas combinaciones de teclas pulsadas.  Cuando esto suceda, ciertas
teclas son simplemente ignoradas.  Por desgracia, no hay nada que se pueda
hacer para solucionar este problema, ya que las teclas simplemente nunca son
recibidas por Windows o NVDA.  En algunos casos, utilizando la fila superior
de teclas con una o ambas manos puede ayudar, ya que el teclado puede
permitir estas teclas.

## Cambios para 44.0.0

* Se añade la tabla kannada.cti.

## Cambios para 28.0.0

* Se cambian los valores predeterminados para el modo de una mano.

## Cambios para 2023.02.23

* Se ha añadido la posibilidad de configurar las teclas usadas para escribir
  puntos en el modo de una mano.
* Ahora se pueden configurar las teclas que deberían ignorarse al escribir
  en braille.
* Se ha añadido un botón que restaura los valores por defecto al panel de
  opciones del complemento.
* Compatible con NVDA 2023.1.

## Cambios para 2022.1

* Se ha añadido la posibilidad de configurar teclas para enviar y borrar
  puntos al escribir con una mano. También es posible configurar un tiempo
  de espera para enviar los puntos automáticamente, sin pulsar teclas de
  confirmación.

## Cambios para 2021.1

* NVDA no intentará verbalizar puntos cuando el modo de una sola mano no
  esté activo o si se ha pulsado la barra espaciadora.
* Compatible con NVDA 2021.1.

## Cambios para 2020.1

* Se puede pulsar la barra espaciadora en combinación con los puntos Braille
  para emular gestos, similar a las órdenes disponibles en pantallas
  Braille.
* Se ha añadido una opción para verbalizar puntos únicos tecleados en el
  modo de una mano.

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


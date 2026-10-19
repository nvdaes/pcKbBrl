# PC Keyboard Braille Input for NVDA #

* Author: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licença: GNU General Public License version 2.0

Este extra para o NVDA permite a entrada de braille através do teclado do
PC.  Actualmente, são suportados os seguintes layouts de teclado:

* Teclado QWERTY inglês.
* Francês (França).
* Alemão (Alemanha).
* Italiano (Itália).
* Persa.
* Português (Portugal).
* Espanhol (Espanha e México).
* Turco.

## Como configurar

O extra pode ser configurado a partir da sua categoria no diálogo de
configurações do NVDA, no menu do NVDA, submenu Preferências. Um atalho para
abrir o painel de configurações do extra pode ser atribuído a partir do
diálogo definir comandos, categoria de configuração.

Marque a caixa de verificação correspondente se quiser digitar usando apenas
uma mão, ou certifique-se de que não está verificada se preferir digitar
usando o modo padrão (duas mãos).

Também pode seleccionar se o NVDA deve falar um único ponto datilografado
(usando )a funcionalidade de "modo de uma mão").

If you want dots to be sent automatically when typing with one hand, use the
spin control to set a timeout greater than 0.

In addition, you can set the characters to send, clear and compose dots when
typing with one hand, as well as characters to be ignored in one hand or
standard mode.

It's also possible to restore defaults in the add-on settings panel.

## Como usar:

1. pressione NVDA+0 para permitir a entrada em braille. Este gesto pode ser
   alterado a partir do diálogo de definir comandos, na categoria Braille.
2. Escrever braile ao pressionar as teclas do teclado do PC como se fosse um
   teclado braille.

	* Se quiser introduzir texto usando as duas mãos, use as seguintes teclas
	  se trabalhar com um teclado QWERTY ingleês, ou as teclas localizadas nas
	  posições correspondentes noutros teclados:

		* f, d e s para os pontos 1, 2 e 3 respectivamente.
		* j, k e l para os pontos 4, 5 e 6 respectivamente.
		* Utilizar as teclas a e ç (c com sedilha) para os pontos 7 e 8,
		  respectivamente.
		* Também pode utilizar as teclas na fila acima; isto é, q, w, e, r, u, i,
		  o e p.

	* Se quiser digitar texto com uma mão, pode compor caracteres premindo
	  teclas simultaneamente ou em várias teclas, adicionando os pontos
	  correspondentes ao caracter pretendido. Prima g ou h para digitar o
	  caracter quando tiver adicionado todos os seus pontos. Se cometer um erro
	  ao construir um carácter, pode apagar os pontos antes de o escrever
	  premindo t ou y. As teclas utilizadas no teclado QWERTY English são as
	  seguintes:

		* Mão esquerda: f, d, s, r, e, w, a, q para os pontos 1, 2, 3, 4, 5, 6, 7
		  e 8.
		* Mão direita: j, k, l, u, i, o, ç (c com sedilha), p para os pontos 1, 2,
		  3, 4, 5, 6, 7 e 8.

3. Pode premir a maioria das outras teclas como normal, incluindo as teclas
   de espaço, backspace, enter e função. Tenha cuidado em não premir
   alt+shift, uma vez que alterar a disposição do teclado pode afectar os
   pontos introduzidos.
4. Pressione a barra de espaço em combinação com pontos braille para mover o
   cursor do sistema (ou reportar a linha actual), apenas se estiver a
   utilizar uma linha braille. Por exemplo, espaço+ponto 1 para emular
   setaAcima, espaço+ponto4+ponto5+ponto6 para emular control+end,
   espaço+ponto1+ponto4 para ler a linha actual, etc.
5. Prima NVDA+0 para desactivar a entrada em braille.

## Notas importantes:

Este extra utiliza o suporte de entrada braille do NVDA.  Por conseguinte, a
tabela de entrada utilizada é a especificada no diálogo de configurações de
Braille do NVDA.

Alguns teclados, especialmente os teclados de laptop, não conseguem lidar
com certas combinações de teclas sendo pressionadas. Quando isso acontece,
certas teclas simplesmente são ignoradas. Infelizmente, não há nada que
possa ser feito para corrigir isso, pois as teclas simplesmente nunca são
recebidas pelo Windows ou NVDA. Em alguns casos, usar a linha superior de
teclas com uma ou ambas as mãos pode ajudar, pois o seu teclado pode
permitir essas teclas.

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

## Alterações para 2020.1

* Pode pressionar a barra de espaço em combinação com pontos braille para
  emular comandos, semelhantes aos comandos disponíveis nas linhas braille.
* adicionada uma opção para falar pontos individuais escritos num modo de
  uma mão.

## Colaboradores:

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]


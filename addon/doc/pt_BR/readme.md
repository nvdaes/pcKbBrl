# Inserção de Braille com o Teclado do PC para NVDA (PC Keyboard Braille Input for NVDA) #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licença: Licença Pública Geral GNU — General Public License — versão 2.0
* Baixar: [versão estável][1] (compatível com NVDA 2019.3 ou posteriores)
* Download: [beta version][2] (compatible with NVDA 2019.3 or later)
* [versão 2014.1][3] (compatível com NVDA 2017.3 a 2019.2)

Este complemento para NVDA possibilita que braille seja digitado através do
teclado do PC. No momento, os seguintes leiautes (esquemas) de teclado são
suportados:

* Teclado QWERTY Inglês.
* Francês (França).
* Alemão (Alemanha).
* Italiano (Itália).
* Persa.
* Português (Portugal).
* Espanhol (Espanha e México).
* Turco.

## Como configurar

O complemento pode ser configurado a partir de sua categoria na caixa de
diálogo de configurações do NVDA, no menu do NVDA, submenu Preferências. Um
comando (gesto) para abrir o painel de configurações do complemento pode ser
atribuído no diálogo Definir comandos, categoria de configuração.

Marque a caixa de seleção correspondente se desejar digitar usando apenas
uma mão, ou certifique-se que não está marcada se preferir digitar no modo
padrão (duas mãos).

Também pode selecionar se o NVDA deve falar um único ponto digitado (usando
o recurso de "modo de uma mão").

If you want dots to be sent automatically when typing with one hand, use the
spin control to set a timeout greater than 0.

In addition, you can set the characters to send, clear and compose dots when
typing with one hand, as well as characters to be ignored in one hand or
standard mode.

It's also possible to restore defaults in the add-on settings panel.

## Como Usar

1. Pressione NVDA+0 para habilitar a inserção de braille. Esse comando pode
   ser alterado no diálogo Definir comandos, categoria Braille.
2. Digite braille pressionando as teclas juntas no teclado do PC como se
   fosse um teclado braille.

	* Se deseja digitar texto usando as duas mãos, use as seguintes teclas se
	  trabalha com um teclado Inglês QWERTY ou as teclas localizadas nas
	  posições correspondentes em outros leiautes:

		* f, d e s para os pontos 1, 2 e 3 respectivamente.
		* j, k e l para os pontos 4, 5 e 6 respectivamente.
		* Use as teclas a e ; (ponto e vírgula no leiaute inglês internacional, ç
		  num teclado ABNT2) para os pontos 7 e 8, respectivamente.
		* Também pode usar as teclas na linha acima; ou seja, q, w, e, r, u, i, o
		  e p.

	* Se quiser digitar texto usando uma mão, você pode compor caracteres
	  pressionando as teclas simultaneamente ou em vários pressionamentos de
	  tecla, adicionando os pontos correspondentes ao caractere
	  desejado. Pressione g ou h para digitar o caractere quando você adicionar
	  todos os seus pontos. Se você cometer um erro ao criar um caractere,
	  poderá limpar os pontos antes de digitá-lo pressionando t ou y. As teclas
	  usadas no teclado Inglês QWERTY são as seguintes:

		* Mão esquerda: f, d, s, r, e, w, a, q para os pontos 1, 2, 3, 4, 5, 6, 7
		  e 8.
		* Mão direita: j, k, l, u, i, o, ; (ponto e vírgula — ç em teclado ABNT2),
		  p para os pontos 1, 2, 3, 4, 5, 6, 7 e 8.

3. Você pode pressionar a maioria das outras teclas normalmente, incluindo
   espaço, backspace, enter e teclas de função. Tome cuidado para não
   pressionar alt+shift, pois a alteração do leiaute do teclado pode afetar
   os pontos digitados.
4. Pressione a barra de espaço em combinação com os pontos braille para
   mover o cursor do sistema (ou relatar a linha atual), apenas se você
   estiver usando uma linha braille. Por exemplo, espaço+ponto1 para emular
   Seta pra cima, espaço+ponto4+ponto5+ponto6 para emular control+end,
   espaço+ponto1+ponto4 para relatar a linha atual, etc.
5. Pressione NVDA+0 para desabilitar a inserção de braille.

## Notas Importantes

Esse complemento usa o suporte embutido de inserção braille do NVDA. Assim,
a tabela de entrada usada é a especificada no diálogo Configurações de
braille do NVDA.

Alguns teclados, em particular os teclados de laptop, não conseguem
processar certas combinações de teclas quando pressionadas. Quando isso
ocorre, certas teclas são simplesmente ignoradas. Infelizmente, não há nada
que se possa fazer para corrigir isso, visto que as teclas simplesmente não
chegam a ser recebidas pelo Windows ou o NVDA. Nalguns casos, usar a
carreira de teclas de cima com uma ou as duas mãos pode ajudar, pois seu
teclado pode liberar essas teclas.


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

## Mudanças na 2020.1

* Você pode pressionar a barra de espaço em combinação com pontos braille
  para emular comandos — gestos —, semelhante aos comandos disponíveis em
  linhas braille.
* Adicionada a opção de falar pontos simples digitados no modo de uma mão.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=pcKbBrl

[2]: https://www.nvaccess.org/addonStore/legacy?file=pcKbBrl-beta

[3]: https://www.nvaccess.org/addonStore/legacy?file=pckbbrl-o

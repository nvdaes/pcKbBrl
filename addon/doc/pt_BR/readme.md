# Inserção de Braille com o Teclado do PC para NVDA — PC Keyboard Braille Input for NVDA #

* Autor: NV Access Limited, Noelia Ruiz Martínez
* Copyright: 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* Licença: Licença Pública Geral GNU — General Public License — versão 2.0

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
comando — gesto — para abrir o painel de configurações do complemento pode
ser atribuído no diálogo Definir comandos, categoria de configuração.

Marque a caixa de seleção correspondente se desejar digitar usando apenas
uma mão, ou certifique-se que não está marcada se preferir digitar no modo
padrão (duas mãos).

Também pode selecionar se o NVDA deve falar um único ponto digitado (usando
o recurso de "modo de uma mão").

Se você quiser que os pontos sejam enviados automaticamente ao digitar com
uma mão, use o controle de seletor numérico para definir um tempo limite
maior que 0.

Além disso, você pode definir os caracteres para enviar, limpar e compor
pontos ao digitar com uma mão, bem como caracteres a serem ignorados em uma
mão ou no modo padrão.

Também é possível restaurar os padrões no painel de configurações do
complemento.

## Como Usar

1. Pressione NVDA+0 para habilitar a inserção de braille. Esse comando —
   gesto — pode ser alterado no diálogo Definir comandos, categoria Braille.
2. Digite braille pressionando as teclas juntas no teclado do PC como se
   fosse um teclado braille.

	* Se deseja digitar texto usando as duas mãos, use as seguintes teclas se
	  trabalha com um teclado Inglês QWERTY ou as teclas localizadas nas
	  posições correspondentes em outros leiautes:

		* f, d e s para os pontos 1, 2 e 3 respectivamente.
		* j, k e l para os pontos 4, 5 e 6 respectivamente.
		* Use as teclas a e ; (ponto e vírgula no leiaute inglês internacional — ç
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

## Changes for 44.0.0

* Added kannada.cti table.

## Mudanças na 28.0.0

* Valores padrão mudados para o Modo de uma mão.

## Mudanças na 2023.02.23

* Adicionada a capacidade de configurar as teclas usadas para digitar pontos
  no modo de uma mão.
* Agora você pode configurar teclas que devem ser ignoradas ao digitar em
  braille.
* Um botão de restauração para padrões foi adicionado ao painel de
  configurações do complemento.
* Compatível com NVDA 2023.1.

## Mudanças na 2022.1

* Adicionada a capacidade de configurar teclas para enviar e limpar pontos
  ao escrever com uma mão. Além disso, é possível definir um tempo limite
  para enviar pontos automaticamente, sem pressionar as teclas de
  confirmação.

## Mudanças na 2021.1

* O NVDA não tentará falar pontos quando o modo de uma mão não estiver ativo
  ou se o espaço tiver sido pressionado.
* Compatível com NVDA 2021.1.

## Mudanças na 2020.1

* Você pode pressionar a barra de espaço em combinação com pontos braille
  para emular comandos — gestos —, semelhante aos comandos disponíveis em
  linhas braille.
* Adicionada uma opção para falar pontos avulsos digitados no modo de uma
  mão.

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


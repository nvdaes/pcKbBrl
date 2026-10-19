# PC Keyboard Braille Input pour NVDA #

* Auteur : NV Access Limited, Noelia Ruiz Martínez
* Copyright : 2012-2023 NV Access Limited, Noelia Ruiz Martínez
* License : GNU General Public License version 2.0

Cette extension NVDA permet de saisir le braille au moyen du clavier du
PC. Actuellement, les dispositions de clavier suivantes sont prises en
charge:

* Clavier QWERTY anglais.
* Français (France).
* Allemand (Allemagne).
* Italien (Italie).
* Persan.
* Portugais (Portugal).
* Espagnol (Espagne et Mexique).
* Turc.

## Comment le configurer

L'extension peut être configurée à partir de sa catégorie dans la boîte de
dialogue des paramètres de NVDA, sous le menu NVDA, sous-menu
Préférences. Un geste pour ouvrir le panneau des paramètres de l'extension
peut être attribué à partir de la boîte de dialogue Gestes de commandes,
catégorie Configuration.

Cochez la case correspondante si vous souhaitez taper à l'aide d'une seule
main ou assurez-vous qu'elle n'est pas cochée si vous préférez taper à
l'aide du mode standard (deux mains).

Vous pouvez également choisir si NVDA doit prononcer chaque point tapé
individuellement (lorsque vous utilisez la fonction «mode à une main»).

Si vous voulez que les points soient envoyés automatiquement lorsque vous
tapez d'une main, utilisez le contrôle giratoire pour définir un délai
supérieur à 0.

De plus, vous pouvez définir les caractères pour envoyer, effacer et
composer des points lors de la saisie à une main, ainsi que des caractères à
ignorer dans le mode à une main  ou standard.

Il est également possible de restaurer aux paramètres par défaut dans le
panneau de paramètres de l'extension.

## Comment l'utilisé

1. Appuyez sur NVDA+0 pour activer la saisie braille. Ce geste peut être
   modifié à partir de la boîte de dialogue Gestes de commandes, catégorie
   Braille.
2. Saisissez en braille en appuyant simultanément sur les touches du clavier
   du PC comme s'il s'agissait d'un clavier braille.

	* Si vous souhaitez saisir du texte à deux mains, utilisez les touches
	  suivantes si vous travaillez avec un clavier français AZERTY ou les
	  touches situées aux positions correspondantes dans d'autres dispositions:

		* f, d et s pour les points 1, 2 et 3 respectivement.
		* j, k et l pour les points 4, 5 et 6 respectivement.
		* Utilisez les touches q et m pour les points 7 et 8, respectivement.
		* Vous pouvez également utiliser les touches de la ligne au-dessus;
		  c'est-à-dire a, z, e, r, u, i, o et p.

	* Si vous souhaitez saisir du texte d'une seule main, vous pouvez composer
	  des caractères en appuyant sur les touches simultanément ou en plusieurs
	  appuis, en ajoutant les points correspondant au caractère
	  souhaité. Appuyez sur g ou h pour valider le caractère lorsque vous avez
	  ajouté tous ses points. Si vous faites une erreur en composant un
	  caractère, vous pouvez effacer les points avant de le valider en appuyant
	  sur t ou y. Les touches utilisées dans le clavier français AZERTY sont
	  les suivantes:

		* Main gauche: f, d, s, r, e, z, q, a pour les points 1, 2, 3, 4, 5, 6, 7
		  et 8.
		* Main droite: j, k, l, u, i, o, m, p pour les points 1, 2, 3, 4, 5, 6, 7
		  et 8.

3. Vous pouvez appuyer sur la plupart des autres touches comme d'habitude, y
   compris les touches espace, retour arrière, entrée et fonction. Veillez à
   ne pas appuyer sur alt+maj, car la modification de la disposition du
   clavier peut affecter les points entrés.
4. Appuyez sur la barre d'espace en combinaison avec des points braille pour
   déplacer le curseur système (ou annoncer la ligne courant), comme si vous
   utilisiez un afficheur braille. Par exemple, espace+point1 pour émuler
   flècheHaut, espace+point4+point5+point6 pour émuler contrôle+fin,
   espace+point1+point4 pour annoncer la ligne courante, etc.
5. Appuyez sur NVDA+0 pour désactiver la saisie braille.

## Remarques Importantes

Cette extension utilise le support de la saisie braille intégré dans
NVDA. Par conséquent, la table de saisie utilisée est celle spécifiée dans
la boîte de dialogue des Paramètres braille de NVDA.

Certains claviers, notamment des claviers de portables, ne peuvent pas gérer
certaines combinaisons de touches.  Lorsque cela se produit, certaines
touches sont simplement ignorés.  Malheureusement, rien ne peut être fait
pour résoudre ce problème, car les touches ne sont tout simplement jamais
reçus par Windows ou NVDA.  Dans certains cas, utiliser la rangée supérieure
des touches avec une ou deux mains pourrait aider, car le clavier peut
permettre ces touches.

## Changements de la version 44.0.0

* Ajout de la table kannada.cti.

## Changements de la version 28.0.0

* Valeurs par défaut modifiées pour le Mode à une main.

## Changements de la version 2023.02.23

* Ajout de la capacité à configurer les touches utilisées pour taper les
  points dans le mode à une main.
* Vous pouvez maintenant configurer les touches qui doivent être ignorées
  lors de la saisie braille.
* Un bouton pour restaurer aux paramètres par défaut a été ajouté au panneau
  de paramètres de l'extension.
* Compatible avec NVDA 2023.1.

## Changements de la version 2022.1

* Ajout de la capacité de configurer les touches pour envoyer et effacer les
  points lors de l'écriture à une main. Il est également possible de définir
  un délai d'expiration pour envoyer des points automatiquement, sans
  appuyer sur les touches  de confirmation.

## Changements de la version 2021.1

* NVDA n'essaiera pas d'énoncer des points lorsque le mode à une main n'est
  pas actif ou si un espace a été enfoncé.
* Compatible avec NVDA 2021.1.

## Changements de la version 2020.1

* Vous pouvez appuyer sur la barre d'espace en combinaison avec des points
  braille pour émuler des gestes de commande, de manière similaires aux
  commandes disponibles dans les afficheurs braille.
* Ajout d'une option pour prononcer les points individuellement tapés dans
  le mode à une main.

## Contributeurs

* James Teh
* Noelia.
* Mohammadreza Rashad
* Cagri Dogan
* Bernd Dorer
* Ângelo Abrantes
* Cyrille Bougot
* Abdel.

[[!tag dev stable]]


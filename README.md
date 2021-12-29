# PROJECT B.M.O
-----------------
### Sommaire
#### Fonctionnement du Github
#### Explication
#### Parties et separations des taches
#### Travail et complication
#### Conclusion
-----------------
#### Fonctionnement du Github
* le dossier :Programmes


-contient :tout les programmes de tout les uControlleur du project(corp et tête)

* le dossier :WEB/static


-contient :les fichier de l'interface homme-machine gerer par le server web Flask du raspberry

* le dossier :facial_reco


-contient :les fichiers qui concerne la reconnaisance facial gerer pas la raspberry

* le dossier :graph


-contient :Tout les graph(fonctionnement systeme ,shema electronique ,etc...)

* le dossier :pcb


-contient :Tout les fichier de la creation du pcb(gerber ,etc...)

* le dossier :CAO_3D


-contient :Tout les fichier 3D ,voir plus d'info dans le dossier 

-----------------
### Explication
Le project bmo est un project de robotique de l'université d'aix marseille consistant a l'imagination et la conception d'un robot de compagnie pouvant 
nous nous somme basé sur un cahier des charges que voici

![cahier des charges](https://user-images.githubusercontent.com/60515907/147596220-ec7e2801-bf3c-4beb-a03a-3017f1169fee.png)

Ce project comprend plusieur language de programmation qui sont : du python , du bash ,du C ,de l'html ,du css , du javascript

-----------------
### Parties et separations des taches

Nino Chef de projet ,responsable de l'intégrations des différents modules ,le developement de la partie interface homme machine,gestion des capteurs et la modélisation 3D

Dimitri responsable circuit imprimé

Bastien responsable module reconnaissance faciale

Matteo responsable design et conceptions

Maxime responsable de l’humanisation et intégrations des modules d’affichages visuel et sonore

-----------------
### Travail et complication
La première partie est de devoir mettre au clair comment resoudre chaque facette de ce project

#### la partie de la reconnaisance fascial necessite :
* une raspberry pi 
* une raspberry cam avec un fort FOV

#### la partie de l'affichage des emotions(visuel et auditive) necessite :
* 2 ecran oled i2c
* 1 buzzer / Haut-parleur

#### la partie de la tête amovible necessite :
* 1 connectique série pouvant s'adapter au futurs corp de facon simple

#### la partie de l'autonomie necessite :
* 1 batterie 
* 1 microcontrolleur qui nous donne l'autonomie de la batterie en temps réel
* un convertisseur boost 3v to 5v   3 ou 4 A

#### la partie de l'autonomie necessite :
* 1 batterie 
* 1 microcontrolleur qui nous donne l'autonomie de la batterie en temps réel

#### Nos idée(suivie de leurs solutions) pour pouvoir rendre ce project plus interessant sont:

#### crée une alimentation buck interne permettant de regler la puissance sonor du buzzer/haut parleur
##### Necessite :
* une sortie pwm d'un uControlleur
* un filtre qui garde la valeur moyenne

#### Faire un systeme d'asservicement electrique pour que la raspberry s'eteigne de facon propre 
qui execute `sudo shutdown -h now` lorsque la batterie principal est debranché du corp lors d'un changement de corp
##### Necessite :
* une entrer digital sur la raspberry
* des diodes
* un accus

Nos problemes:

-----------------
### Conclusion










Programme contient les programmes de :

l'arduino 
le script
le programme python global 























WEB contient le dossier static qui contient tout les fichiers 
en charge de la page web comme le css ,le javascript et l'html

# Markown-memento
Voici un petit fichier memento pour vous indiquer les principales syntaxes que vous pouvez utiliser en markdown.
Pour voir les détails de la syntaxe, cliquez que l'icone d'édition de ce fichier.

----------------

####Mettre un mot en italique

Voici un mot *en italique* 

Votre mot se trouve entre astérisques `*mon-mot*`

-----------------

####Mettre un mot en gras

Voici un mot __en gras__ ! 

Votre mot se trouve entre deux `__underscores__` 

-----------------

####Les titres

# Titre de niveau 1 
Pour un titre de niveau 1 (h1), il faut placer un `#titre` devant votre titre.

## Titre de niveau 2
Pour un titre de niveau 2 (h2), il faut cette fois deux `##titre` devant votre titre

Et ainsi de suite jusqu'au h6.

-----------------

####Aller à la ligne en fin de phrase

Pour faire un  
changement de ligne

Votre ligne doit se terminer par 2 `espaces` pour faire ce qu'on appelle un __retour-chariot__, c'est à dire aller à la ligne.

-----------------

####Faire une liste à puces

* Une puce
* Une autre puce
* Et encore une autre puce !

Il faut simplement placer un astérisque devant les éléments de votre liste.

`* Une puce`

`* Une autre puce`

`* Et encore une autre puce !`

######Pour faire une liste ordonnée : 

1. Et de un
2. Et de deux
3. Et de trois

`1. Et de un`
`2. Et de deux`
`3. Et de trois`

######Pour imbriquer une liste dans une autre :

* Une puce
* Une autre puce
    * Une sous-puce
    * Une autre sous-puce
* Et encore une autre puce !

`* Une puce`

`* Une autre puce`

    `* Une sous-puce`
    
    `* Une autre sous-puce`
    
`* Et encore une autre puce !`

1. Une puce
2. Une autre puce
    1. Une sous-puce
    2. Une autre sous-puce
3. Et encore une autre puce !

`1. Une puce`

`2. Une autre puce`

    `1. Une sous-puce`
    
    `2. Une autre sous-puce`
    
`3. Et encore une autre puce !`

-----------------

####Faire une citation

> Ceci est un texte cité. Vous pouvez répondre
> à cette citation en écrivant un paragraphe
> normal juste en-dessous !

Il vous suffit d'ajouter un `>` devant votre citation.

`> Ceci est un texte cité. Vous pouvez répondre à cette citation en écrivant un paragraphe normal juste en-dessous !`

-----------------

####Ecrire du code

#####Un code entier

Voici un code en C :

    int main()
    {
        printf("Hello world!\n");
        return 0;
    }
    
Il vous suffit d'écrire votre phrase de présentation comme n'importe quelle phrase et d'écrire votre code à la ligne.
    
`Voici un code en C :`

    int main()
    {
        printf("Hello world!\n");
        return 0;
    }

#####Juste un morceau de code

`<h1>Titre</h1>`

Il vous suffit d'entourer votre morceau de code avec deux accents graves.
Pour faire un accent grave, il vous suffit de faire `AltGr` + `7` sur votre clavier.

-----------------

####Mettre un lien

Rendez-vous sur [Simplonline](http://www.simplonline.com) !

Il vous faut le mot sur lequel vous souhaitez faire votre lien entre crochets [ ], puis votre lien entre parenthèses ( ).

`Rendez-vous sur [Simplonline](http://www.simplonline.com) !`

-----------------

####Intégrer une image

La syntaxe est la même que pour un lien, il suffit juste d'ajouter un point d'exclamation devant les crochets. 

Ce que vous mettez entre crochet est le texte alternatif de l'image, que nous vous conseillons fortement d'intégrer à chaque fois que vous mettez une image.

Important : ça ne marche qu'avec des url d'images prises sur le web.

`![Simplon.co](http://simplon.co/wp-content/uploads/2015/04/if-coder-keep-coding-else-learn-with-simplon-2-600x675.png)`

![Simplon.co](http://simplon.co/wp-content/uploads/2015/04/if-coder-keep-coding-else-learn-with-simplon-2-600x675.png)

-----------------

####Barre de séparation

Pour faire une barre de séparation il vous suffit d'écrire plusieurs `-` d'affilé. Plus vous en mettrez plus le trait sera épais.

`-----------------`


----------------
CACA
----------------


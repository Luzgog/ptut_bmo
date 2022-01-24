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

#### Nos idée(suivie de leurs solutions) pour pouvoir rendre ce project plus interessant sont:

#### crée une alimentation buck interne permettant de regler la puissance sonor du buzzer/haut parleur
##### Necessite :
* une sortie pwm d'un uControlleur
* un filtre qui garde la valeur moyenne

#### Faire un systeme d'asservicement electrique pour que la raspberry s'eteigne de facon propre 
qui execute `sudo shutdown -h now` lorsque la batterie principal est debranché du corp lors d'un changement de corp
##### Necessite :
* une entrée digital sur la raspberry
* un Automatic Battery Backup Switchover
* un accus
* 2 mos

Nos problemes:

-----------------
### Conclusion


----------------
a faire :

faire le systeme d'ampli audio(inshalla celui que j'ai acheter fonctionne bien)


faire la tête de bmo(nino)


finir le pcb(dimitri)


commander les composant pour le pcb(tous ensemble avec moulin)


faire la synthese vocal et la reconnaisance(dimitri)


preparer le compte rendu(mateo)


faire un systeme de memoire des paramètres(dimitri) 


faire le systeme de routeur wifi(raspap)(necessite la clé wifi)(--disponible--)


faire les yeux un peut plus epuré(maxime)


faire le qrcode pour ce connecter au routeur BMO(quelqu'un)


avancer dans la reconnaisance vocal(bastien)


----------------

matos qui manque :

1 clé wifi usb
1 disque dure(optionnel)
1 haut parleur
1 carte son audio et micro en usb

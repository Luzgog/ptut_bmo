#!/usr/bin/env python3
from PIL import Image
import ST7789
import time
import secrets

ecranD = ST7789.ST7789(
        height= 240, #hauteur de l'ecran
        rotation= 0, #rotation de 180 de l'ecran
        port=0, #jsp ce que c'est mais ballec
        cs=ST7789.BG_SPI_CS_FRONT, #choix de la broche esclave de l'ecran (ST7789.BG_SPI_CS_BACK = pin CE1)
        dc=9, #choix de la pin data control
        backlight=19, #choix de la pin du controle de l'eclairage
        spi_speed_hz=80 * 1000 * 1000, #vitesse du spi
        offset_left= 40, #decalage avec la gauche
        offset_top= 0 #decalage avec le top
)
ecranG = ST7789.ST7789(
        height= 240, #hauteur de l'ecran
        rotation= 180, #rotation de 180 de l'ecran
        port=0, #jsp ce que c'est mais ballec
        cs=ST7789.BG_SPI_CS_BACK, #choix de la broche esclave de l'ecran (ST7789.BG_SPI_CS_BACK = pin CE0)
        dc=9,#choix de la pin data control
        backlight=19,#choix de la pin du controle de l'eclairage
        spi_speed_hz=80 * 1000 * 1000, #vitesse du spi
        offset_left= 40, #decalage avec la gauche
        offset_top= 0 #decalage avec le top
)
    # Initialize display.

ecranD.begin() #on démare chaque ecran logicielement parlant
ecranG.begin() #on démare chaque ecran logicielement parlant

width = ecranD.width #on definie la largeur a partir des info des ecrans si dessus
height = ecranD.height #on definie la hauteur a partir des info des ecrans si dessus
# Load an image.

aleatoire = secrets.randbelow(9) 
imageD = Image.open("thumbs up/"+str(aleatoire)+".gif")#on met le gif dans la variable imageD
aleatoire = secrets.randbelow(9) 
imageG = Image.open("thumbs up/"+str(aleatoire)+".gif") #on met le gif dans la variable imageG

frameG = 0
frameD = 0


while True:
    try:
        print(frameG)
        print(frameD)
        imageG.seek(frameG) #on enregistre le nombre de frame dans le gif et on enregistre ce nombre dans frame
        imageD.seek(frameD) #on enregistre le nombre de frame dans le gif et on enregistre ce nombre dans frame
        
        ecranD.display(imageD.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
        ecranG.display(imageG.resize((width, height))) #on prend le gif et on le resize a la taille de l'ecran
        
        frameG += 1 #on avance d'une frame
        frameD += 1
        time.sleep(0.02)

    except EOFError: #quand on arrive a la fin du gif alors sa reset les frames pour retourner au debut du fichier
        frameD = 0
        frameG = 0
#probleme actuel 
    #obligé de faire marcher chaque oeuil dans un thread different
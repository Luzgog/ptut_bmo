#!/usr/bin/env python3
from PIL import Image
import ST7789
import time
import secrets

ecranD = ST7789.ST7789(
        height= 240, #hauteur de l'ecran
        rotation= 0, #rotation de 180 de l'ecran
        port=0,
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
        port=0,
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

emotion = {
        "content" : (Image.open("Oeil1.png"), Image.open("Oeil1.png")),
        "pas_content": (Image.open("pas_content_D.png"), Image.open("pas_content_G.png")),
        "dodo" : (Image.open("dodo_D.png"), Image.open("dodo_G.png")),
        "triste" : (Image.open("triste_D.png"), Image.open("triste_G.png")),
        "etourdi" : (Image.open("etourdi_D.png"), Image.open("etourdi_G.png"))
        }
imgeD, imageG = emotion["content"]
# Load d'un png
imageD = Image.open("Oeil1.png") #on met le png dans la variable imageD
imageG = Image.open("Oeil1.png") #on met le png dans la variable imageG

ecranD.display(imageD.resize((width, height))) #on prend l'image (png / gif) et on la resize a la taille de l'ecran
ecranG.display(imageG.resize((width, height))) #on prend l'image (png / gif) et on la resize a la taille de l'ecran

input()
#!/usr/bin/env python3
from PIL import Image
import ST7789
import time
import secrets

ecranD = ST7789.ST7789(
        height= 240,
        rotation= 0,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left= 40,
        offset_top= 0
)
ecranG = ST7789.ST7789(
        height= 240,
        rotation= 180,
        port=0,
        cs=ST7789.BG_SPI_CS_BACK,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left= 40,
        offset_top= 0
)
    # Initialize display.

ecranD.begin()
ecranG.begin()

width = ecranD.width
height = ecranD.height
# Load an image.

aleatoire = secrets.randbelow(9) 
imageD = Image.open("thumbs up/"+str(aleatoire)+".gif")
aleatoire = secrets.randbelow(9) 
imageG = Image.open("thumbs up/"+str(aleatoire)+".gif")

frame = 0


while True:
    try:
        imageG.seek(frame)
        imageD.seek(frame)
        ecranD.display(imageD.resize((width, height)))
        ecranG.display(imageG.resize((width, height)))
        frame += 1
        time.sleep(0.02)

    except EOFError:
        frame = 0

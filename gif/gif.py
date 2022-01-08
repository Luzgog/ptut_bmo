#!/usr/bin/env python3
from PIL import Image
import ST7789
import time

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
        port=1,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
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
imageD = Image.open("shutdown2.gif")
imageG = Image.open("shutdown.gif")

frame = 0

while True:
    try:
        image.seek(frame)
        ecranD.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.03)

    except EOFError:
        frame = 0

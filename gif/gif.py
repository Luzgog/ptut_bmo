#!/usr/bin/env python3
from PIL import Image
import ST7789
import time

disp = ST7789.ST7789(
        height=135 if display_type == "rect" else 240,
        rotation=0 if display_type == "rect" else 90,
        port=0,
        cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
        dc=9,
        backlight=19,               # 18 for back BG slot, 19 for front BG slot.
        spi_speed_hz=80 * 1000 * 1000,
        offset_left=0 if display_type == "square" else 40,
        offset_top=53 if display_type == "rect" else 0
)
    # Initialize display.
disp.begin()

width = disp.width
height = disp.height

# Load an image.
print('Loading gif: {}...'.format(image_file))
image = Image.open(image_file)

print('Drawing gif, press Ctrl+C to exit!')

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0

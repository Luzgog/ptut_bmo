from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image

serial = i2c(port=1, address=0x3C)

device = sh1106(serial)
device.clear() #on enleve l'image deja existant si il y en a
#tu as aussi hide  qui va eteindre ou mettre en low wonsommation la carte
img = Image.open("Oeil_2.png")

device.display(img.convert(device.mode))
input() #j'ai mit ca juste pour attendre, a la fin du programme ca enleve l'image automatiquement

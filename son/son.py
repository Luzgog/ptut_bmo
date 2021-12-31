import pygame
volume = 100
#le volume doit être en 0 et 1 plus d'info ici :
# https://www.pygame.org/docs/ref/music.html#pygame.mixer.music.set_volume
pygame.mixer.init()
pygame.mixer.music.load("myFile.wav")
pygame.mixer.music.set_volume(volume / 100)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
    

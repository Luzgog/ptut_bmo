import pygame
pygame.mixer.init()
test = pygame.mixer.Sound("myFile.wav")
pygame.mixer.Sound.set_volume(test, 1.0)
pygame.mixer.Sound.play(test)

while pygame.mixer.music.get_busy() == True:
    continue

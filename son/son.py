import pygame
volume = 100

pygame.mixer.init()
pygame.mixer.music.load("myFile.wav")
pygame.mixer.music.set_volume(volume / 100)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
    

import pygame

pygame.mixer.init()
my_sound = pygame.mixer.Sound('my_sound.wav')
my_sound.set_volume(1.0)
my_sound.play()



while pygame.mixer.music.get_busy() == True:
    continue

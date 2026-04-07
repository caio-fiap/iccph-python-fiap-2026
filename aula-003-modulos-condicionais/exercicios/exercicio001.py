# abrir e reproduzir um mp3
import pygame
import time

pygame.init()

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(2)

print("Audio maneirão")
# abrir e reproduzir um mp3
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('C:/Users/labsfiap/Documents/GitHub/iccph-python-fiap-2026/aula-003-modulos-condicionais/exercicios/audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print("Audio maneirão")
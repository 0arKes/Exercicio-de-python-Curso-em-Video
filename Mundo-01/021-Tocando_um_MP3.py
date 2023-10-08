import pygame
caminho = str(input('Digite o caminho até o arquivo MP3: '))
pygame.init()
pygame.mixer.music.load(caminho)
pygame.mixer.music.play()
input()
pygame.event.wait
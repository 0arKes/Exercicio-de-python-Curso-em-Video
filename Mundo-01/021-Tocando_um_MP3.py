"""
Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame
caminho = str(input('Digite o caminho até o arquivo MP3: '))
pygame.init()
pygame.mixer.music.load(caminho)
pygame.mixer.music.play()
input()
pygame.event.wait
# Enunciado: Tocando MP3
# Testando a biblioteca Pygame
#  Programa desenvolvido em Python 03
# Desenvolva um programa que abra e reproduza o aúdio de um arquivo mp3.

from turtle import  Screen
#  Load e Play do arquivo mp3 com pygame
import pygame

pygame.init() 
Screen = pygame.display.set_mode ((300, 300))
pygame.display.set_caption ('musica map3') 
pygame.mixer.music.load ('happy-mistake.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


    


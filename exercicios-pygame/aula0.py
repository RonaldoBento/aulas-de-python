# Enunciado: Aprendendo a Desenvolver Games com pygame
# Programa Desenvolvido em Python 03 com a biblioteca pygame

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

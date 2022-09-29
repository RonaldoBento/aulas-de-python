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
    pygame.draw.rect(screen, (255, 0, 0), (200, 300, 40, 50))
    pygame.draw.circle(screen, (0, 0, 255), (300, 260), 40)
    pygame.draw.line(screen, (255, 255, 0), (390, 0), (390, 600), 5)
    
    pygame.display.update()

    
    
    
    
    
    
    

    

             


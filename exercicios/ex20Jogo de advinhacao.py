#Jogo de Adivinhação
#programa desenvolvido em Python 03
'''Desenvolva um programa que faça o PC "Pensar" em um número inteiro entre 1 e 5 e peça para o usuário tentar adivinha qual foi o número escolhido pelo PC. O programa deverá escrever na tela se o usuário venceu ou perdeu!'''

print()
print('-='*30)
print(f'{" Jogo de Adivinhação":^60}')
print('-='*30)
print()

from random import randint
from time import sleep

# Cores ANSI escape sequence \033[m
print('>>> \033[1;32m Informe um número inteiro entre 1 e 5:\033[m ')
pc = randint(1,5)
player = int(input(' \033[1;33m Em que número o PC pensou?\033[m '))
print('>>> \033[1;36m PROCESSANDO...\033[m', end='')
sleep(1)
if player >= 1 and player <= 5:
    if player == pc:
        print(' \033[1;35m PARABÉNS!\033[mVocê conseguiu \033[1;32mVENCER\033[m o PC!')
    else:
        print(f' \033[1;31m PC GANHOU!\033[m Ele processou o número {pc} e não o {player}.')
else:
    print(' \033[1;31mERRO! Somente valores entre 1 e 5...\033[m')
    
print()
print('-='*30)
print(f'{"Programa Finalizado com Sucesso":^60}')
print('-='*30)




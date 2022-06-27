# Enunciado: Game Jokenpô (Pedra, Papel e Tesoura)
# Programa Desenvolvido em Python 03

print()
print('-='*40)
print(f'\033[1;35m{"Game Jokenpô":^80}\033[m')
print('-='*40)
print()

from random import randint
from time import sleep

itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2) # Aleatório entre os números 0 (PEDRA), 1 (PAPEL), 2 (TESOURA)
print('''\033[1;33m >>> Suas Opções são:
      [0] PEDRA
      [1] PAPEL 
      [2] TESOURA\033[m''')
player = int(input('\033[1;37m Qual é a sua Jogada?\033[m '))
print('\033[1;32m JO\033[m', end = "")
sleep(1)
print('\033[1;34mKEN\033[m', end = "")
sleep(1)
print('\033[1;35mPÔ\033[m')
print('-'*80)
print(f'\033[1;37m Computador jogou {itens[pc]}\033[m')
print(f'\033[1;37m Jogador jogou {itens[player]}\033[m')
print('-'*80)

if pc == 0: # Computador jogou PEDRA 
    if player == 0: # Jogador jogou PEDRA 
        print('\033[1;34m RESULTADO: EMPATE!\033[m ')
    elif player == 1: # Jogador jogou PAPEL
        print('\033[1;32m RESULTADO: VENCEU!\033[m')
    elif player == 2: # Jogador jogou TESOURA
        print('\033[1;33m RESULTADO: PERDEU!\033[m')
    else:
        print('\033[1;31m JOGADA INVÁLIDA!\033[m')

elif pc == 1: # Computador jogou PAPEL 
    if player == 1: # Jogador jogou PAPEL 
        print('\033[1;34m RESULTADO: EMPATE!\033[m ')
    elif player == 2: # Jogador jogou TESOURA
        print('\033[1;32m RESULTADO: VENCEU!\033[m')
    elif player == 0: # Jogador jogou PEDRA
        print('\033[1;33m RESULTADO: PERDEU!\033[m')
    else:
        print('\033[1;31m JOGADA INVÁLIDA!\033[m')

elif pc == 2: # Computador jogou TESOURA
    if player == 2: # Jogador jogou TESOURA
        print('\033[1;34m RESULTADO: EMPATE!\033[m ')
    elif player == 0: # Jogador jogou PEDRA
        print('\033[1;32m RESULTADO: VENCEU!\033[m')
    elif player == 1: # Jogador jogou PAPEL
        print('\033[1;33m RESULTADO: PERDEU!\033[m')
    else:
        print('\033[1;31m JOGADA INVÁLIDA!\033[m')

print()
print('-='*40) 
print(f'\033[1;31m{" GAME OVER ":^80}\033[m')
print('-='*40)
print()

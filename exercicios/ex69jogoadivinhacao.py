# Enunciado: Jogo de Adivinhação com direito a Palpites 
# Programa Desenvolvido em Python 03
'''Crie um programa (jogo) onde o computador vai "Pensar" em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar, ou seja, o programa termina se o jogador acertar.No final mostra quantos palpites foram necessários para vencer.'''

print()
print('-='*40)
print(f'\033[1;34m{"Jogo de Adivinhação":^80}\033[m')
print('-='*40)
print()

from random import randint
from time import sleep

computador = randint(0,10)

print('\033[1;36m O computador pensou em um número entre 0 e 10\n será que você consegue adivinhar qual foi ele?\033[m ')
print()
acertou = False
palpites = 0

while not acertou: # Enquanto não acertar
    jogador =int(input('\033[1;37m Qual é seu palpite?\033[m '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;33m O número é Maior... Tente novamente!\033[m')
        elif jogador > computador:
            print('\033[1;32m O número é Menor... Tente novamente!\033[m')
print()
sleep(1)
print(f'\033[1;37m Acertou com {palpites} tentativas.\033[m\033[1;35mPARABÊNS!\033[m')       

print()
print('-='*40)
print(f'\033[1;33m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


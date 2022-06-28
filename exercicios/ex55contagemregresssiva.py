# Enunciado: Contagem Regressiva 
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que mostre na tela uma contagem regressiva, indo de 20 até 0, com uma pausa de 1 segundo entre eles. '''

print()
print('-='*40)
print(f'\033[1;34m{"Contagem Regressiva":^80}\033[m')
print('-='*40)
print()

from time import sleep
for c in range(20, -1, -1):
    print(c, end = " ")
    sleep(1)
print('\033[1;33mTerminei de Contar!\033[m')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

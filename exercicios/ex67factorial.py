# Enunciado: Cálculo do Fatorial de um Número
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia um número inteiro qualquer e mostre na tela o seu Fatorial, por exemplo: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

print()
print('-='*40)
print(f'\033[1;32m{"Cálculo do Fatorial":^80}\033[m')
print('-='*40)
print()

from math import factorial
n = int(input('\033[1;37m Informe um número inteiro para calcular seu Fatorial:\033[m '))
f = factorial(n)
print(f'\033[1;33m O fatorial de {n} vale {f}.\033[m')
        
print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


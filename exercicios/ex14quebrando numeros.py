#enunciado: Quebrando um número
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia um número Real qualguer pelo teclado
e mostre na tela a sua parte inteira.'''

print()
print('-='*40)
print(f'{"Quebrando Números":^80}')
print('-='*40)
print()

#Com a biblioteca Math
from math import trunc #trunc = truncado

n = float(input(' Digite um número real qualquer: '))
print(f' O valor digitado foi {n} e sua parte inteira é {trunc(n)}')

print()
#Não precisa da biblioteca Math
n = float(input(' Digite outro número real qualquer: '))
print(f' O valor digitado foi {n} e sua parte inteira é {int(n)}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)



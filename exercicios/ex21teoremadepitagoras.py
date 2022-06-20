#Teorema de Pitágoras - Catetos e Hipotenusa
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o comprimento do catero oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da Hipotenusa.'''

print()
print('-='*40)
print(f'{"Teorema de Pitágoras":^80}')
print('-='*40)
print()

from math import hypot
co = float(input(' Informe o comprimento do cateto oposto: '))
ca = float(input(' Informe o comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print(f' A Hipotenusa vai medir {hi:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

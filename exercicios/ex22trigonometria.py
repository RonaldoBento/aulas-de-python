#Trigonometria (Seno, Cosseno e Tangente)
#Programa desenvolvido em Python 03
'''Trigonometria é parte da geometria plana que estuda a relação entre a medida dos lados e dos ângulos de um triângulo, seja ele retângulo, seja ele um triângulo qualquer. Desenvolva um programa que leia um ângulo qualguer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo.'''

print()
print('-='*40)
print(f'{"TRIGONOMETRIA":^80}')
print('-='*40)
print()

from math import radians, sin, cos, tan
a = float(input(' Informe um ângulo: '))
seno = sin(radians(a))
print(f' O ângulo de {a} tem seu SENO de {seno:.3f}')
cosseno = cos(radians(a))
print(f' O ângulo de {a} tem seu COSSENO de {cosseno:.3f}')
tangente = tan(radians(a))
print(f' O ângulo de {a} tem sua TANGENTE de {tangente:.3f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


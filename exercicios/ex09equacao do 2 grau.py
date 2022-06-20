#Enunciado: Equação do Segundo Grau
#Programa desenvolvido em Python 03 
'''Crie um programa que leia os valores e mostre na tela os resultados da Equação.'''

print()
print('-='*40)
print(f'{"Equação do 2º Grau":-^80}')
print('-='*40)
print()

from math import sqrt

#Solicitando os três valores da Equação (a, b, c)
a = int(input(' Informe o valor de a: '))
b = int(input(' Informe o valor de b: '))
c = int(input(' Informe o valor de c: '))

#Mostrando a Equação do 2º Grau
print(f' Sua equação é {a}X² + {b}X + {c} = 0')
#Mostrando o valor de Delta
delta = (b**2) - 4*a*c
print(f' O valor de Delta é {delta:.2f}')
if delta < 0:
    print(' Para Delta Negativo, não existe raízes no Reais.')
elif delta == 0:
    x1 = (-b + sqrt(delta)) / (2*a) 
    print(f' Para Delta Zero, temos duas raizes iguais a {x1}')
else:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(' Para Delta Positivo, temos raízes diferentes: ')
    print(f' X1 = {x1}')
    print(f' X2 = {x2}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


    
















        

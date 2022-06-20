#Enunciado: Calculando Desconto de 5%
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o preço de um produto e mostre
seu novo preço, com 5% de desconto.'''

print()
print('-='*40)
print(f'{"Calculando Desconto":^80}')
print('-='*40)
print()

p = float(input(' Informe o preço do produto: R$ '))
novo = p - (p * 5 / 100)
print(f' O produto que custava R$ {p:.2f}, na promoção com desconto \n de 5% vai custar R$ {novo:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

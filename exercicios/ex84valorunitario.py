# Enunciado: Valor Total a Ser Pago
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que, dados o valor unitário do produto e a quantidade comprada, exiba o valor a ser pago.''' 

print() 
print('-='*40)
print(f'\033[1;32m{"Valor Total a Ser Pago":^80}\033[m')
print('-='*40)
print()

p = float(input('\033[1;33m Informe o valor unitário do produto em R$ \033[m'))
qt = int(input('\033[1;36m Quanto do produto você vai levar? \033[m'))
valor = p * qt
print(f'\033[1;37m Cada produto custa R$ {p:.2f} e a quantidade comprada foi {qt}\n e o valor total ficou em R$ {valor:.2f}\033[m')

print() 
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

# Enunciado: Grupo da Maioridade
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
print()
print('-='*40)
print(f'\033[1;31m{"Grupo da Maioridade":^80}\033[m')
print('-='*40)
print()
from datetime import date
atual = date.today().year
maior = 0
menor = 0

for pessoa in range(1,8):
    nasc = int(input(f'\033[1;32m Em que ano a {pessoa}º nasceu?\033[m '))
    idade = atual - nasc
    if idade >= 21:
        maior = maior + 1 # maior += 1
    else:
        menor = menor + 1 # menor += 1
print()
print(f'\033[1;37m Ao todo tivemos {maior} pessoas maiores de idade.\n E também tivemos {menor} pessoas menores de idade.\033[m')

print()
print('-='*40)
print(f'\033[1;33m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

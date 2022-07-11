# Enunciado: Maior e Menor da Sequência
# Programa Desenvolvido em Python 03
'''Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido'''

print()
print('-='*40)
print(f'\033[1;32m{"Maior e Menor da Sequência":^80}\033[m')
print('-='*40)
print()

maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input(f'\033[1;33mInforme o peso em kg da {pessoa}º pessoa:\033[m '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print()
print(f'\033[1;36m O maior peso lido foi de {maior} kg.\033[m')
print(f'\033[1;35m O menor peso lido foi de {menor} kg.\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

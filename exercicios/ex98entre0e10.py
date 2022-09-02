# Enunciado: Quantos entre 0 e 10
# Programa Desenvolvido em Python 03
''' Desenvolva um programa que leita valores entre 0 e 10, mostre quantos valores      digitados entre 0 e 10 e a soma nesse intervalo do valores ímpares.'''

print() 
print('-='*40)
print(f'\033[1;32m{" Quantos entre 0 e 10":^80}\033[m')
print('-='*40)
print() 

total = 0
soma_impares = 0
for c in range(0,11):
    valor = int(input('\033[1;33m Digite um valor inteiro: '))
    if valor >= 0 and valor <= 10:
        total += 1
        if valor % 2 == 1:
            soma_impares += valor

print()
print(f'\033[1;37m Ao todo foram {total} valores entre 0 e 10.')
print(f' Nesse intervalo, a soma de impares foi de {soma_impares}.\033[m')
        
print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

# Enunciado: Somador de Números Pares
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia 6 valores inteiros e mostre a soma apenas daqueles valores que forem pares, os valores ímpares desconsidere-os.'''

print()
print('-='*40)
print(f'\033[1;33m{"Somador de Números Pares":^80}\033[m')
print('-='*40)
print()

soma = 0
contador = 0
for c in range(1,7):
    n = int(input(f'\033[1;32m Digite o {c}º valor inteiro:\033[m '))
    if n % 2 == 0:
        soma += n
        contador += 1
print()
print(f'\033[1;36m Você informou {contador} valores pares e a soma foi {soma}.\033[m ')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

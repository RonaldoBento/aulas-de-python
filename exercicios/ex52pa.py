# Enunciado: Progressão Aritmética (P.A)
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o 1º termo e a razão de uma P.A. No final mostre os 10 primeiros termos dessa progressão. '''

print()
print('-='*40)
print(f'{"Progressão Aritmética (P.A)":^80}')
print('-='*40)
print()

p = int(input('\033[1;33m Informe o primeiro termo da P.A:\033[m '))
r = int(input('\033[1;32m Informe a razão da P.A:\033[m '))
decimo = p + (10 -1) * r
print()
for c in range(p, decimo +r, r):
    print(f'\033[1;37m {c}\033[m', end= ' -')
print('\033[1;36m ACABOU!\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()


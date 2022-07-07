# Enunciado: Progressão Aritmética (PA)
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos dessa progressão.'''

print()
print('-='*40)
print(f'\033[1;35m{"Progressão Aritmética":^80}\033[m')
print('-='*40)
print() 

p = int(input('\033[1;37m Informe o primeiro termo da P.A: '))
r = int(input(' Informe a razão da P.A: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print(f' {c}', end= "-")
print('\033[m\033[1;32m ACABOU!\033[m')

print()
print('-='*40)
print(f'\033[1;33m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

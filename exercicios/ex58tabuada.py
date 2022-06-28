# Enunciado: Tabuada
# Programa Desenvolvido em Python 03
# Desenvolva um programa que leia um valor inteiro qualquer e mostre na tela a sua tabuada.

print()
print('-='*40)
print(f'\033[1;32m{"TABUADA":^80}\033[m')
print('-='*40)
print()

n = int(input('\033[1;34m Digite um valor inteiro qualquer:\033[m '))
print()
for c in range(0, 11):
    print(f'\033[1;32m {n} X {c:2} = {n * c}\033[m')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

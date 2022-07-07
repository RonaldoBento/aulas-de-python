# Enunciado: Números Primos
# Programa Finalizado com Sucesso
# Desenvolva um programa que leia um número e mostre se ele é Primo ou náo.

print()
print('-='*40)
print(f'\033[1;32m{"Número Primo ou Não?":^80}\033[m')
print('-='*40)
print()

n = int(input('\033[1;37m Informe um número inteiro:\033[m '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(' ', end = "")
        total += 1 # total = total + 1
    else:
        print(' ', end = "")
print(f'\033[1;34m \n O número {n} foi divisível {total} vezes: ')
if total == 2: 
    print('\033[1;32m LOGO, ELE É PRIMO!\033[m')
else:
    print('\033[1;33m LOGO, ELE NÃO É PRIMO!\033[m')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


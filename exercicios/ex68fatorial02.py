# Enunciado: Cálculo do Fatorial de um Número
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia um número inteiro qualquer e mostre na tela o seu Fatorial, por exemplo: 5! = 5 X 4 X 3 X 2 X 1 = 120'''

print()
print('-='*40)
print(f'\033[1;32m{"Cálculo do Fatorial":^80}\033[m')
print('-='*40)
print()


n = int(input('\033[1;37m Informe um número inteiro para calcular seu Fatorial:\033[m '))
c = n # Contador recebe o número digitado
f = 1 # Factorial recebe 1
print(f'\033[1;33m Calcuando {n}!=\033[m', end= "")
while c > 0: # Repetição com teste lógico no inicio
    print('\033[1;37m{}'.format(c), end = "")
    print('X' if c > 1 else '=\033[m', end = "")
    f *= c # f = f * c
    c = c - 1 
print(f'\033[1;33mO fatorial de {n} vale {f}.\033[m')
        
print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

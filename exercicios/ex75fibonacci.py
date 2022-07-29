# Enunciado: Sequência de Fibonacci
# Programa Desenvolvido em Python 03
'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma seguência de Fibonacci.'''

print()
print('-='*40)
print(f'\033[1;34m{"Sequência de Fibonacci":^80}\033[m')
print('-='*40)
print()

n = int(input('\033[1;37m Quantos termos você quer mostrar? '))
t1 = 0 # Termo um inicia com zero
t2 = 1 # Termo dois inicia com um
print('-'*80)
print(' {} - {} '.format(t1,t2), end= "")
c = 3 # Contador inicia com três
while c <= n:
    t3 = t1 + t2
    print(' - {} '.format(t3), end= "")
    t1 = t2
    t2 = t3
    c += 1
print(' FIM\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

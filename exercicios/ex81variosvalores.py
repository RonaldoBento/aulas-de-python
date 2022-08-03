# Enunciado: Tratando Vários Valores
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia vários valores inteiros pelo teclado. O progama só vai parar quando o usuário digitar o valor 999, que é a condição de parada (flag). No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999).'''

print()
print('-='*40)
print(f'\033[1;34m{"Tratando Vários Valores":^80}\033[m')
print('-='*40)
print()

numero = contador = soma = 0
n = int(input('\033[1;37m Informe um número inteiro: [Digite 999 para encerrar]:\033[m '))
while n != 999:
    soma += numero 
    contador += 1
    n = int(input('\033[1;37m Informe um número inteiro: [Digite 999 para encerrar]:\033[m '))
print(f'\033[1;33m Você digitou {contador} números e a soma entre eles foi de {soma}.\033[m')

print()
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


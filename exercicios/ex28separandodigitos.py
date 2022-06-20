#Enunciado: Separando Dígitos de um Número
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia um número inteiro entre 0 e 999999 e mostre na tela cada um dos dígitos separados. Exemplo: 1834 - 4 unidades, 3 dezenas, 8 centenas e 1 milhar.'''

print()
print('-='*40)
print(f'{"Separando dígitos de um número":^80}')
print('-='*40)
print()

n = int(input(' Informe um número inteiro: '))
print(f' Analisando o número inteiro {n}: ')
print(f' Analisando sua unidade: {n//1%10}, dezena: {n//10%10}, centena: {n//100%10},\n milhar: {n//1000%10}, dezena de milhar: {n//10000%10} e centena de milha: {n//100000%10} - FIM ')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)



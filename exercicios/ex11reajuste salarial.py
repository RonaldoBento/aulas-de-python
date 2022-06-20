#Enunciado: Reajuste Salarial
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.'''

print()
print('-='*40)
print(f'{"Reajuste Salarial":^80}')
print('-='*40)
print()

s = float(input(' Qual é o salário do funcionário? '))
novo = s + (s * 15 / 100)
print(f' Um funcionário que ganhava R$ {s:.2f}, com 15% de \n aumento, passou a receber  um novo salário de {novo:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

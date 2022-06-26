# Enunciado: Classificando Nadadores
# Programa Desenvolvido em Python 03
'''A Confederação Nacional de Natação solicitou o desenvolvimento de um programa que leia o ano de nascimento de um nadador e mostre sua categoria de acordo com a idade: Até 9 anos - MIRIN. Até 14 anos - INFANTIL. Até 19 anos - JUNIOR. Até 25 anos - SÊNIOR. Acima é MASTER'''

print()
print('-='*40)
print(f'{"Classificando Nadadores":^80}')
print('-='*40)
print()

from datetime import date
atual = date.today().year
nome = str(input(' Qual é o nome do(a) nadador(a): ')).strip().upper()
nasc = int(input(' Informe o ano de nascimento: '))
idade = atual - nasc
print(f'\033[1;33m {nome} possui {idade} anos.\033[m')
if idade <= 9:
    print('\033[1;37m CLASSIFICAÇÃO MIRIM\033[m')
elif idade <= 14:
    print('\033[1;32m CLASSIFICAÇÃO INFANTIL\033[m')
elif idade <= 19:
    print('\033[1;35m CLASSIFICAÇÃO JUNIOR\033[m')
elif idade <= 25:
    print('\033[1;34m CLASSIFICAÇÃO SÊNIOR\033[m')
else:
    print('\033[1;31m CLASSIFICAÇÃO MASTER\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()


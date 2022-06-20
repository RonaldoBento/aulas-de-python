# Enunciado: Aumentos Múltiplos
# Programa desenvolvido em Python 03
'''Desenvolva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$ 2500,00. Calcule o aumento de 12% e para os salários inferiores ou iguais, o aumento é de 15% '''

print()
print('-='*40)
print(f' {"Aumento Múltiplos":^80}')
print('-='*40)
print()

nome = str(input(' \033[1;34mInforme o nome do funcionário: \033[m')).strip().upper()
salario = float(input(f' Qual é o salário do funcionário {nome}: R$ '))
if salario > 2500:
    novo = salario + (salario * 12 / 100)
else:
    novo = salario + (salario * 15 / 100)
print(f' O funcionário {nome} que ganahva \033[1;33mR$\033[m {salario:.2f} com o aumento passou a ganhar \033[1;33mR$\033[m {novo:.2f} ')

print()
print('-='*40)
print(f'{"Programa Finalzado com Sucesso":^80}')
print('-='*40)


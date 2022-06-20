# Enunciado: Aumentos Múltiplos
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para Salários Superiores a R$ 1250,00. Calcule um aumento de 10% e para os Inferiores ou Iguais, o aumento será de 15%. Mostre na tela o NOVO SALÁRIO.'''

print()
print('-='*40)
print(f'{"Aumentos Múltiplos de Salários":^80}')
print('-='*40)
print()

s = float(input(' Qual é o salário do funconário? R$ '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print(f' O funcionário que ganhava R$ {s:.2f} passa a ganhar R$ {novo:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-=*40')

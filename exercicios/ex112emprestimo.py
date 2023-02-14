# Enunciado: Empréstimo Bancário
# Programa Desenvolvido em Python 03 

'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa.O programa vai perguntar o valor 
da casa, o salário do comprador e em quantos anos ele 
vai pagar.

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

   
print() 
print('-='*40)
print(f'\033[1;31m{" Empréstimo Bancário":^80}\033[m')
print('-='*40)
print()

preco = float(input(f'\033[1;33m Qual o valor da casa? \033[m'))
sal = float(input(f'\033[1;34m Qual é o seu salário? \033[m'))
tempo = int(input(f'\033[1;32m Em quantos anos você vai pagar? \033[m'))

mensalidade = (preco / (tempo * 12))
print(f' Valor da casa: {preco:.2f}')
print(f' Prestação: {mensalidade:.2f}')

if mensalidade >= (sal * 30 / 100):
    # if sal < (mensalidade * (30 / 100)):
    print(" Empréstimo negado.")
else:
    print(f' >>> Empréstimo concedido. Mensalidade durante {tempo} anos: R${mensalidade:.2f}.')

print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()



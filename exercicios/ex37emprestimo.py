# Enunciado: Aprovando Empréstimo
# Programa Desenvolvido em Python 03
'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado. '''

print()
print('-='*40)
print(f'{"Aprovando empréstimo para compra da casa":^80}')
print('-='*40)
print()

casa = float(input('\033[1;36m Informe o valor da casa: R$\033[m  '))
salario = float(input('\033[1;35m Informe o salário do comprador: R$\033[m]  '))
anos = int(input('\033[1;33m Em quantos anos de financiamento?\033[m '))
prestacao = casa / (anos * 12) # O valor da casa dividido em 12 meses
minimo = salario * 30 / 100 # 30% do salário

print(f' Para pagar uma casa de R$ {casa:.2f} em {anos} anos: ',end='')
if prestacao <= minimo:
    print('\033[1;32mEMPRÉSTIMO CONCEDIDO!\033[m')
else:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()


# Aprovando Empréstimo
# Programa desenvolvido em Python 03
'''Desenvolva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa e o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder a 30% do salário ou então o emprestimo será negado. '''

print() 
print('-='*40)
print(f'{" Aprovando Empréstimo":^80}')
print('-='*40)
print()

casa = float(input(' Informe o valor da casa: \033[1;32mR$\033[m '))
s = float(input(' Informe o salário do comprador: \033[1;32mR$\033[m '))
anos = int(input(' \033[1;33mEm quantos anos de financiamento?\033[m '))
prestacao = casa / (anos * 12)
# A prestação mensal, não pode exceder a 30% do salário ou então o emprestimo será negado.
minimo = s * 30 / 100
print(f' Para pagar uma casa de \033[1;32mR$\033[m {casa:.2f} em {anos} anos, a prestação será de \033[1;32mR$\033[m {prestacao:.2f}')
if prestacao <= minimo:
    print('\033[1;35m Empréstimo Concedido!\033[m')
else:
    print('\033[1;31m Empréstimo Negado!\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()


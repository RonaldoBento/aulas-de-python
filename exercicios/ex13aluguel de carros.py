#Enunciado: Aluguel de Carros
#programa desenvolvido em Python 03
'''Desenvolva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
a pagar, sabendo que o carro custa R$ 90.00 por dia e R$ 0.50 por Km rodados?'''

print()
print('-='*40)
print(f'{"Aluguel de Carros":^80}')
print('-='*40)
print()

dias = int(input(' Quantos dias você alugou? '))
km = float(input(' Quantos Km rodados? '))
pago = (dias * 90) + (km * 0.50)
print(f' O total a pagar pelo serviço é R${pago:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


      

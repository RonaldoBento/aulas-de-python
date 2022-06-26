# Enunciado: Gerenciador de Pagamento
# Programa Desenvolvido em Python 03
'''Elabore um programa que calcule o valor a ser pago por um determinado produto, considerando o seu preço normal e condições de pagamento: 
- À vista  Dinheiro / Cheque: (10% de desconto);
- À vista no Cartão: (5% de desconto):
- Em até 2X no Cartão: (Preço Normal);
- Em 3X ou mais no Cartão: (Com 20% de Juros).'''

print()
print('-='*40)
print(f'{"Gerenciador de pagamento":^80}')
print('-='*40)
print()

p = float(input('\033[1;33m Informe o Preço das Compras: R$\033[m '))
''' [1] - À vista  Dinheiro / Cheque: (10% de desconto);
   [2] - À vista no Cartão: (5% de desconto):
   [3] - Em até 2X no Cartão: (Preço Normal);
   [4] - Em 3X ou mais no Cartão: (Com 20% de Juros).'''
op = int(input('\033[1;32m >>> Qual é sua opção?\033[m '))
if op == 1:
    total = p - (p * 10 / 100) # Com 10% de desconto
elif op == 2:
    total = p - (p * 5 / 100 ) # Com 5% de desconto
elif op == 3: 
    total = p # Preço Normal
    parcelas = total / 2 # 2X no Cartão
    print(f'\033[1;34m Sua compra que custa R$ {p:.2f} será parcelada em 2X de R$ {parcelas:.2f} sem Juros.\033[m')
elif op == 4:
    total = p + (p * 20 / 100) # Com 20% de Juros
    totalparcelas = int(input('\033[1;35m Em quantas parcelas?\033[m '))
    parcelas = total / totalparcelas
    print(f'\033[1;37m Sua compra será parcelada em {totalparcelas}X de R$ {parcelas:.2f} com Juros.\033[m ')
else:
    total = p
    print('\033[1;31m Opção Inválida de Pagamento. Tente outra opção!\033[m')
    
print(f'\033[1;37m Sua compra de R$ {p:.2f} vai custar R$ {total:.2f} no final.\033[m ')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()

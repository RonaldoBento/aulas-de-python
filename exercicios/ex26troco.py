#Enunciado: Troco a ser devolvido
#Programa desenvolvido em Python 03
'''Desenvolva um programa que, dado o valor da mercadoria e o valor pago, calcule e exiba o troco a ser devolvido.'''

print()
print('-='*40)
print(f'{"Troco a ser devolvido ao cliente":^80}')
print('-='*40)
print()


v = float(input(' Informe o valor da mercadoria: R$ '))
p = float(input(' Quanto em dinheiro você pagou? R$ '))
troco = p - v #Troco recebe pagamento menos valor da mercadoia
print()
if troco == 0:
    print(f' O preço foi de R$ {v:.2f} e você pagou R$ {p:.2f},\n logo não houve troco. ')
else:
    print(f' O preço foi de R$ {v:.2f} e você pagou R$ {p:.2f},\n logo seu troco foi de R$ {troco:.2f} ')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)




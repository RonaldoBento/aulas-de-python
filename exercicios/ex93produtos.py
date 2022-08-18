# Enunciado: Estatísticas de Produtos
# Programa Desenvolvido em Python 03

'''Desenvolva um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar. No final mostre:
A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$ 1000,00;
C) Qual é o nome do produto mais barato.'''

print() 
print('-='*40)
print(f'\033[1;32m{"Estatística de Produtos":^80}\033[m')
print('-='*40)
print() 
total = totmil = menor = cont = 0
barato = ' '
while True: 
    produto = str(input('\033[1;37m Informe o nome do Produto: '))
    preco = float(input(' Informe o preço do produto: R$\033[m '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('\033[1;33m Quer continuar? [s ou n]\033[m ')).strip().lower()[0]
    if resposta == 'n':
        break
print()    
print(f'\033[1;37m O total da compra foi R${total:.2f}')
print(f' Temos {totmil} produtos custando mais de R$ 1000,00')
print(f' O produto mais barato foi {barato} que custa {menor:.2f}\033[m')             


print() 
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

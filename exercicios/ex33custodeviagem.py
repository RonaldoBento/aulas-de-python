# Enunciado: Custo de Viagem
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagem de até 200Km e R$  0,45 para viagens mais longas.'''

print()
print('-='*40)
print(f'{"Custo da Viagem":^80}')
print('-='*40)
print()

d = float(input(' Qual é a distância de sua viagem? '))
print(f' Você está preste a começar uma viagem de {d} Km.')
if d <= 200: 
    preco = d * 0.50 # Ou d * 0.50 if d <= 200 else d * 0.45
else:
    preco = d * 0.45

# Condição Simplificada 
# preco = d * 0.50 if d <= 200 else d * 0.45
print(f' E o preço da sua passagem será de : R$ {preco:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
    
    
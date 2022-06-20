#Enunciado: Conversor de Medida Monetária
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia quanto dinheiro em R$ uma pessoa possui na
carteira e mostre quantos US$ ela pode comprar.'''

print()
print('-='*40)
print(f'{"Conversor Monetário":^80}')
print('-='*40)
print()

#Considere  US$ 1.00 = R$ 8.5
r = float(input(' Digite quantos reais você possui na carteira? R$ '))
d = r / 8.5 #d = dolares
print(f' Com R$ {r:.2f} você pode comprar US$ {d:.2f}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)



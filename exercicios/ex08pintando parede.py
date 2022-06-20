#Enunciado: Pintando uma Parede
#programa desenvovido em Python 03
'''Desenvolva um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
cada litro de tinta, pinta apenas uma área de aproximadamente 2m².'''

print()
print('-='*40)
print(f'{"Pintando Parede":^80}')
print('-='*40)
print()

l = float(input(' Informe a largura da parede: '))
a = float(input(' Informe a altura da parede: '))
area = l * a
print(f' Sua parede possui as dimensões de {l} X {a} e sua área é de {area}m².')

print()
tinta = area / 2 #2m² = 1Litro de tinta
print(f' Para pintar essa parede foi preciso {tinta} Litros de tinta.')
print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)










# Enunciado: Analisador de Triângulos
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o comprimento de 3 segmentos de retas e diga ao usuário se elas podem ou não formar um triângulo. Se forma triângulo mostre: Equilátero - todos os lados iguais. Isósceles - dois lados iguais. Escaleno - todos os lados diferentes. '''

print()
print('-='*40)
print(f'{"Analisador de Triângulos":^80}')
print('-='*40)
print()

r1 = float(input(' Informe o primeiro segmento de reta: '))
r2 = float(input(' Informe o segundo segmento de reta: '))
r3 = float(input(' Informe o terceiro segmento de reta: '))
# Vereficando se os segmentos de reta podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print()
    print(' Os segmentos podem formar um Triângulo ', end = '')
    if r1 == r2 == r3 == r1:
        print('\033[1;33mEQUILÁTERO.\033[m')
    elif r1  != r2 != r3 != r1:
        print('\033[1;32mESCALENO.\033[m')
    else:
        print('\033[1;35mISÓSCELES.\033[m')
else:
    print()
    print(' Os segmentos de reta \033[1;31mNÃO\033[m podem formar um Triângulo.')    

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
    
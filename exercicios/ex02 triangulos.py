# ENUNCIADO: ANALIZANDO TRIÂNGULOS
#Programa desenvolvido em Python 03

'''Desenvolva um programa que leia o comprimento de 3 segmentos de reta e diga ao usuário
se eles podem ou não formar um Triângulo?
Equilátero: todos os lados iguais.
Isósceles: dois lados iguais.
Escaleno: todos os lados deiferentes.'''

print()
print('-='*40)
print(f'{"ANALIZANDO TRIÂNGULOS":^80}')
print('-='*40)
print()

r1 = float(input(' Informe o 1º segmento de reta: '))
r2 = float(input(' Informe o 2º segmento de reta: '))
r3 = float(input(' Informe o 3º segmento de reta: '))
print()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Formam um Triângulo: ', end = '')
    if r1 == r2 == r3 == r1:
        print('Triângulo Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno.')
    else:
        print('Triângulo Isósceles.')
else:
    print(' Os segmentos de reta NÃO podem formar um Triângulo.')
    
print()
print('-='*40)
print(f'{"PROGRAMA FINALIZADO COM SUCESSO":^80}')
print('-='*40)


    

# Enunciado: Analisando Triângulos
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que verefique se pode formar um Triângulo e classifique-os em Equilátero: todos os lados iguais. Isósceles: dois lados iguais e Escaleno: todos os lados diferentes.'''

print()
print('-='*40)
print(f'{"Analisando Triângulos ":^80}')
print('-='*40)
print()

# Escreva três segmentos de reta para vereficar se pode formar um Triângulo
r1 = float(input(' Informe o primeiro segmento de reta: '))
r2 = float(input(' Informe o segundo segmento de reta: '))
r3 = float(input(' Informe o terceiro segmento de reta: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;33m Os segmentos de reta podem formar um Triângulo\033[m', end = "") 
    if r1 == r2 == r3 == r1:
        print('\033[1;32m EQUILÁTERO.\033[m')
    elif r1!= r2 != r3 != r1:
        print('\033[1;36m ESCALENO.\033[m')
    else:
        print('\033[1;35m ISÓSCELES.\033[m')
else:
    print('\033[1;31m Os segmentos de reta NÃO podem formar um Triângulo.\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()


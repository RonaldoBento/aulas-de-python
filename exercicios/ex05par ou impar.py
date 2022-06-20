#Enunciado: Par ou Impar
#Programa desenvolvido em Python 03
'''Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR.'''

print()
print('-='*40)
print(f'{">>> Par ou Impar <<<":^80}')
print('-='*40)
print()

n = int(input(' Informe um número inteiro: '))
r = n % 2 # Resto da divisão
print(f' O resto da divisão foi {r}: ')
if r == 0:
    print(f' O resultado {n} é um número PAR!')
else:
    print(f' O resultado {n} é um número IMPAR!')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

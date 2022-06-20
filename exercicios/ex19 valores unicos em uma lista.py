# Enunciado: VALORES ÚNICOS EM UMA LISTA
#Programa desenvolvido em Python 03
'''Desenvolva um programa onde o usuário possa digitar vários valores númericos
e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado. No
final, serão serão exibidos todos os valores únicos digitados, em ordem crescente.'''

print()
print('-='*40)
print(f'{"VALORES ÚNICOS EM UMA LISTA":^80}')
print('-='*40)
print()

numero = [] # or list()
while True:
    n = int(input(' Informe um valor inteiro: '))
    if n not in numero:
        numero.append(n)
        print(' valor adicionado com sucesso!')
    else:
        print(' Valor duplicado! Não será adicionado...')
    resp = str(input(' Quer continuar? [S/N] ')).upper().strip()
    if resp in "N":
        break
numero.sort()
print()
print(f' Você digitou os valores {numero}')
print()

print('-='*40)
print(f'{"PROGRAMA FINALIZADO COM SUCESSO":^80}')
print('-='*40)



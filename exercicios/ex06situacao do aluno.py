#Enunciado: Situação do Aluno
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia as três notas do aluno, calculando e
mostrando a sua média aritmética.'''

print()
print('-='*40)
print(f'{"Situação do Aluno":^80}')
print('-='*40)
print()

nome = str(input(' Informe o nome do aluno: '))
n1 = float(input(f' Infome a 1º nota do aluno {nome}: '))
n2 = float(input(f' Informa a 2º nota do aluno {nome}: '))
n3 = float(input(f' Informe a 3º nota do aluno {nome}: '))
m = (n1 + n2 + n3) / 3

print(f' A média do aluno {nome} é igual a {m:.1f}')
print()
print('-'*80)
print()

if m >= 7:
    print(f' O aluno {nome} foi APROVADO!')
elif m < 7 and m >= 5:
    print(f' O aluno {nome} está em RECUPERAÇÃO!')
else:
    print(f' O aluno {nome} foi REPROVADO!')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
















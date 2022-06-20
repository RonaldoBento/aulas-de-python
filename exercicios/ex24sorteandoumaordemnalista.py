#Enunciado: Sorteando uma Ordem na Lista
#Programa desenvolvido em Python 03
'''O mesmo professor do exercício anterior (ex24) quer sortear a ordem de apresentação de trabalhos dos alunos. Desenvolva um programa que leia o nome dos 4 alunos e mostre a ordem sorteada...'''

print()
print('-='*40)
print(f'{"Sorteando 4 alunos para apresentação dos trabalhos.":^80}')
print('-='*40)
print()

from random import shuffle #Shuffle = embaralhar
#Ler o nomes dos 4 alunos
n1 = str(input(' Informe o nome do primeiro aluno: ')).strip().upper()
n2 = str(input(' Informe o nome do segundo aluno: ')).strip().upper()
n3 = str(input(' Informe o nome do terceiro aluno: ')).strip().upper()
n4 = str(input(' Informe o nome do quarto aluno: ')).strip().upper()
lista = [n1, n2, n3, n4] #Variáveis dentro de uma lista
shuffle(lista) #Embaralhar lista
print(' A ordem da apresentação será: ', end= '')
print(lista)

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

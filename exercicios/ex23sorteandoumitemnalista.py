#Enunciado: Sorteando um item na lista
#Programa Desenvolvido em Python 03
'''Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Desenvolva um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. '''

print()
print('-='*40)
print(f'{"Sorteando um dos 4 alunos":^80}')
print('-='*40)
print()

from random import choice #choice = escolha
#ler 4 nomes de alunos
n1 = str(input(' Informe o nome do primeiro aluno: ')).strip().upper()
n2 = str(input(' Informe o nome do segundo aluno: ')).strip().upper()
n3 = str(input(' Informe o nome do terceiro aluno: ')).strip().upper()
n4 = str(input(' Infomre o nome do quarto aluno: ')).strip().upper()
lista = [n1, n2, n3, n4] #Variáveis dentro de um lista
escolhido = choice(lista) #Vai escolher uma variável da lista, no caso (n1,n2,n3,n4) 
print(f' O aluno escolhido para apagar o quadro foi {escolhido}.')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

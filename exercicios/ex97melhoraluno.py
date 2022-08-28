# Enunciado: Algoritmo para detectar o melhor aproveitamento dos alunos
# Programa Desenvolvido em Python 3
'''Desenvolva um programa que leia quantos alunos há numa sala de aula. Atribua valores aos alunos como (nome, nota, maior_nota) e mostre o aluno com melhor aproveitamneto.'''

from rich import print

print() 
print('-='*40)
print(f'[blue]{" Escola de Línguas Orlando de Campos":^80}[/]')
print('-='*40)
print() 

contador = 1
maior_nota = 0



total = int(input(' Informe quantos alunos há em sala de aula: '))
while contador <= total:
    nome = str(input(f' Digite o nome do {contador}º Aluno: ')).strip().upper()
    nota = float(input(f' Digite a nota do aluno {nome}: '))
    if nota > maior_nota:
        maior_nota = nota
        melhor_aluno = nome
    contador += 1
    
print()

print(f' O melhor aproveitamento foi do aluno {melhor_aluno} com a nota {maior_nota:.2f}.')
     
print() 
print('-='*40)
print(f'[green]{" Programa Finalizado com Sucesso":^80}[/]')
print('-='*40)
print() 

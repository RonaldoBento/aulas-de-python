#Enunciado: Procurando uma string dentro de outra
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o nome de uma pessoae diga se ela possui "SILVA" no nome.'''

print()
print('-='*40)
print(f'{"Procurando uma String dentro de outra":^80}')
print('-='*40)
print()

nome = str(input(' Qual é seu nome completo: ')).strip().lower()
#Testa se é verdadeiro ou falso
print(f' Seu nome possui Silva? [Verdadeiro ou Falso] {"silva" in nome}') 

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


      
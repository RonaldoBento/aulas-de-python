#Enunciado: Primeiro e Último nome de uma pessoa
#Programa desenvolvido em Python 03
''''Desenvolva um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

print()
print('-='*40)
print(f'{"Primeiro e Último Nome de uma Pessoa":^80}')
print('-='*40)
print()

n = str(input(' Digite seu nome completo: ')).strip().upper()
nome = n.split() 
print(f' Muito prazer em conhecê-lo(a)!')
print(f' Seu primeiro nome é {nome[0]} e seu último é {nome[len(nome) - 1]}.')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)




#Enunciado: Analisador de Texto
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras ao todo (sem considerar os espaços);
- Quantas letras possui o primeiro nome.'''

print()
print('-='*40)
print(f'{"Analisador de Texto":^80}')
print('-='*40)

nome = str(input(' Digite o seu nome completo: ')).strip()
print(f' Seu nome com letras maiúsculas é: {nome.upper()}.')
print(f' Seu nome com letras minúsculas é: {nome.lower()}.')
print(f' Seu nome tem ao todo {len(nome)} letras.')
separa = nome.split()
print(f' Seu primeiro nome é {separa[0]} e ele possui {len(separa[0])} letras.')

print()
print('-='*40)
print(f'{"Programa Finalisado com Sucesso":^80}')
print('-='*40)



      
















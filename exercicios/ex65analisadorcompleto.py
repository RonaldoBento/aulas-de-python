# Enunciado: Analisador Completo
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o nome, idade e o sexo de 5 pessoas. No final, mostre: A média de idade do grupo. Qual é o nome do homen mais velho. Quantas mulheres têm menos de 20 anos.''' 

print()
print('-='*40)
print(f'\033[1;36m{"Analisador Completo":^80}\033[m')
print('-='*40)
print()

soma_idade = 0
maior_idade_homem = 0
media_idade = 0
nome_homem_velho = 0
mulher20 = 0

for p in range(1,6):
    print(f'\033[1;32m >>> Analisando {p}º Pessoas:\033[m ')
    nome = str(input('\033[1;37m Informe o nome completo: ')).strip().upper()
    idade = int(input(' Informe a idade: '))
    sexo = str(input(' Informe o sexo[M/F]:\033[m' )).strip().upper()
    soma_idade += idade 
    if p == 1 and sexo in "M":
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in "F" and idade < 20:
        mulher20 += 1
media_idade = soma_idade / 5

print()
print(f'\033[1;33m A Média de idade do grupo é de {media_idade:.1f} idade.\033[m') 
print(f'\033[1;37m O homem mais velho possui {maior_idade_homem} anos e se chama {nome_homem_velho}.\033[m')
print(f'\033[1;35m Ao todo são {mulher20} mulheres com menos de 20 anos.\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

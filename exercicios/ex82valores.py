# Enunciado: Maior e Menor Valores
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a Média Aritmética de todos os valores e qual foi o maior e o menor valor lido. O program deve perguntar ao usuário se ele quer ou não continuar a digitar valores inteiros. '''

print()
print('-='*40)
print(f'\033[1;34m{"Maior e Menor Valores":^80}\033[m')
print('-='*40)
print()
soma = quantidade = media = maior = menor = 0
resposta = 's'

while resposta in "Ss":
    numero = int(input('\033[1;32m Informe um número inteiro:\033[m '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('\033[1;33m Quer continuar? [S/N]\033[m ')).strip().upper()
media = soma / quantidade
print(f'\033[1;37m Você digitou {quantidade} número e a média foi de {media:.1f}\n e o menor valor foi {menor} e o maior foi {maior}.\033[m ')

print()
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

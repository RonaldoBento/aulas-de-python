#Enunciado: Maior e Menor Valores
#Programa desenvolvido em Python 03

'''Desenvolva um programa que leia 3 números e mostre qual é o Maior e qual é o
Menor número. Números: a, b, c'''

print()
print('-='*40)
print(f'{"Maior e Menor Valores":^80}')
print('-='*40)
print()

a = int(input(' Informe o 1º valor inteiro: '))
b = int(input(' Informe o 2º valor inteiro: '))
c = int(input(' Informe o 3º valor inteiro: '))

#Verificando quem é o Maior Valor
maior = a #Afirmo que a é maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#Verificando quem é o Menor Valor
menor = a #Afirmo que a é menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f' O maior valor foi  {maior}.')
print(f' O menor valor foi  {menor}.')
print()
print('-'*80)
print(f'{" >>> Maior e Menor Valor Revelado":^80}')
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)



    

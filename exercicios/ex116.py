#Programa desenvolvido no Python 03
#Exercício 116: Valores Únicos em uma Lista

'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista, ele não sera
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

print() 
print('-='*30)
print('>>>> Valores Únicos em uma Lista')
print('-='*30)
print()

numero = []
while True:
    valor = int(input(' Informe um valor inteiro: '))
    if valor not in numero:
        numero.append(valor)
        print(' Valor adicionado com sucesso!')
    else:
        print(' Valor duplicado! Não precisa adicionar...')
    resposta = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in "Nn":
        break
numero.sort()
print(f' Você digitou os valores {numero}.')
        
print()
print('-='*30)
print()
print('>>>> Programa desenvolvido com sucesso.')
print()


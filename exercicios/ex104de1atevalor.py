# Enunciado: Somando valores de 1 até o valor digitado
# Programa Desenvolvido em Python 03
# Faça um programa que leia um valor e mostre a soma de 1 até o valor digitado

from rich import print
print()
print('-='*40)
print(f'[green][bold]{"Somando valores de 1 até o valor digitado":^80}[/][/]')
print('-='*40)
print()

soma = 0
valor = int(input('\033[1;33m Digite um valor inteiro até o qual deseja somar:\033[m '))
for contador in range(1, valor + 1):
    soma += contador
    
print(f'[blue][bold] A soma de 1 até {valor} é {soma}.[/][/]')

print()
print('-='*40)
print(f'[green][bold]{"Programa Finalizado com Sucesso":^80}[/][/]')
print('-='*40)
print()






# Enunciado: Mostrar por extenso
# Programa Desenvolvido em Python 03 

'''Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso'''
   
print() 
print('-='*40)
print(f'\033[1;31m{" MOSTRAR POR EXTENSO":^80}\033[m')
print('-='*40)
print()
extensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )
while True:
    n = int(input(f'\033[1;33m Digite um número entre 0 até 20:\033[m'))
    if n >= 0 and n <= 20:
        print(f'\033[1;33m Você digitou: {extensos[n]}.\033[m')
        break
    else:
        print('\033[1;33m Tente novamente.\033[m', end='')

print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

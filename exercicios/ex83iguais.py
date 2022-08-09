# Enunciado: Retorne se os números são iguais
# Programa Desenvolvido em Python 03
# Escreva um programa que, dados dois valores inteiros, retorne se eles são iguais.

print()
print('-='*40)
print(f'\033[1;34m{"Números Iguais":^80}\033[m')
print('-='*40)
print()

valor1 = int(input('\033[1;37m Informe o 1º valor inteiro: '))
valor2 = int(input(' Informe o 2º valor inteiro: \033[m'))
if valor1 == valor2:
    print(f'\033[1;33m Os valores {valor1} e {valor2} são iguais.\033[m')
else:
    print(f'\033[1;32m Os valores {valor1} e {valor2} são diferentes.\033[m')

print() 
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

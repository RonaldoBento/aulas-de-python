# Enunciado: Comparando Números
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O 1º valor digitado é maior ou menor. O 2º valor digitado é maior ou menor ou ambos são iguais. '''

print()
print('-='*40)
print(f'{"Comparando Números":^80}')
print('-='*40)
print()

n1 = int(input(' Informe o 1º valor inteiro: '))
n2 = int(input(' Informe o 2º valor inteiro: '))

if n1 > n2:
    print(' O 1º valor é \033[1;32mMAIOR!\033[m')
elif n2 > n1:
    print(' O 2º valor é \033[1;33mMAIOR!\033[m' )
else:
    print(' \033[1;34mOs dois valores são iguais.\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()

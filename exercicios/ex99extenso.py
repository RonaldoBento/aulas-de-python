# Enunciado: Números por Extenso
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de Zero até Dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.'''

print() 
print('-='*40)
print(f'\033[1;31m{" Números Por Extenso":^80}\033[m')
print('-='*40)
print() 

c = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito','Nove','Dez')
while True:
    n = int(input('\033[1;33m Entre com um número inteiro entre 0 e 10:\033[m '))
    if n >=0 and n <=10:
        break
    print('\033[1;35m ERRO: Tente Novamente...\033[m', end = '')
print(f'\033[1;36m Você digitou o número {c[n]}\033[m.')

print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 


# Enunciado: Contagem de Números Pares
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que mostre na tela todos os números pares que estão no intervalo que o usuário solicitar: Iniciando com o número 2  e Fim o usuário escolhe, mas o passo precisa ser 2.'''

print()
print('-='*40)
print(f'\033[1;32m{"Contagem de Números Pares":^80}\033[m')
print('-='*40)
print()
fim = int(input('\033[1;33m Informe um número inteiro para o final do intervalo:\033[m '))
for c in range(2, fim + 1, 2):
    print('',c, end = " ")
print('\n\033[1;35m Terminei de Contar!\033[m')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

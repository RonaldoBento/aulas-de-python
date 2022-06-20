# Enunciado: Conversor de Bases Numéricas
# Programa Desenvolvido em Python 03
'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a Base Numérica de conversão: 1 para Binário, 2 para Octal e 3 para Hexadecimal.'''

print()
print('-='*40)
print(f'{"Conversor de Bases Numéricas":^80}')
print('-='*40)
print()

n = int(input('\033[1;33m Para escolher digite um número inteiro:\033[m '))
print(''' Escolha uma das bases para conversão: 
      [1] Converte para Binário;
      [2] Converte para Octal;
      [3] Converte para Hexadecimal.''')
print()
opcao = int(input(' \033[1;31m >>> Sua opção é:\033[m '))
if opcao == 1:
    print(f' Convertido para\033[1;32m BINÁRIO\033[m é igual a {bin(n)[2:]}')
elif opcao == 2: 
    print(f' Convertido para\033[1;36m OCTAL\033[m é igual a {oct(n)[2:]} ')
elif opcao == 3:
    print(f' Convertendo para\033[1;35m HEXADECIMAL\033[m é igual a {hex(n)[2:]}')
elif opcao != 1 != 2 != 3:
    print('\033[1;31m OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\033[m ')
 
print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

    
    
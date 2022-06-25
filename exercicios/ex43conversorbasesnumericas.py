# Enunciado: Conversor de Bases Numéricas
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia um número qualquer e peça para o usuário escolher qual será a base de conversão: 1 para Binário, 2 para Octal e 3 para Hexadecimal'''

print()
print('-='*40)
print(f'{"Conversor de Bases Numéricas":^80}')
print('-='*40)
print()

n = int(input(' \033[1;32mDigite um número inteiro:\033[m '))
print(''' Escolha uma das Bases Numéricas para conversão:
      [1] Converte para Binário
      [2] Converte para Octal
      [3] Converte para Hexadecimal ''')
print('-'*80)
opcao = int(input(' >>> Informe sua opção: '))
if opcao == 1:
    print(f' O número {n} convertido para \033[1;32mBinário\033[m é igual a {bin(n)[2:]} ')
elif opcao == 2:
    print(f' O número {n} convertido para \033[1;36mOctal\033[m é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f' O número {n} convertido para \033[1;35mHexadecimal\033[m é igual a {hex(n)[2:]}')
else:
    print('\033[1;31mOpcão Inválida: Tente novamente!\033[m')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()

# Enunciado: Validação de Dados 
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou   'F'. Caso o usuário digite errado peça para digitar novamente os valores, até ter um valor digitado corretamente.'''

print()
print('-='*40)
print(f'\033[1;32m{"Validação de Dados":^80}\033[m')
print('-='*40)
print()

print(f'\033[1;33m{" Digite: M para Masculino e F para Feminino":^80}\033[m')
sexo = str(input('\033[1;37m Informe o sexo com: [M/F]\033[m ')).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input('\033[1;31m ERRO: Dados Inválidos. Por favor, informe o sexo com: [M/F]\033[m ')).strip().upper()[0]
print()
print(f'\033[1;35m Sexo {sexo} registrado com Sucesso!\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


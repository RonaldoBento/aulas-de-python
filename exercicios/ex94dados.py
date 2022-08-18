# Enunciado: Analisador de Dados
# Programa Desenvolvido em Python 03

'''Desenvolva um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre na tela: 
A) Quantas pessoas possui mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres possui menos de 20 anos.'''

print()
print('-='*40)
print(f'\033[1;32m{"Analisador de Dados":^80}\033[m')
print('-='*40)
print()

t18 = 0 # Total de Pessoas com mais de 18 anos
th = 0 # Total de Homens 
t20 = 0 # Total de mulheres com menos de 20 anos

while True:
    idade = int(input('\033[1;36m Informe a idade:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1;37m Informe o sexo:[M/F]\033[m ')).strip().upper()[0]
        if idade >= 18:
            t18 += 1
        if sexo == 'M':
            th += 1
        if sexo == 'F' and idade < 20:
            t20 += 1
        resposta = ' '
    while resposta not in 'SN':
        resposta = str(input(' Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break 
              
print(f'\033[1;33m Total de pessoas com mais de 18 anos: {t18}\033[m ')
print(f'\033[1;32m Ao todo temos {th} homens cadastrados.\033[m')
print(f'\033[1;35m E temos {t20} mulheres com menos de 20 anos.\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

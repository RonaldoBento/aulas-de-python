# Enunciado: Alistamento Militar
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o ano de nascimento de um jovem homem e informe, de acordo com sua idade: Alistar ao serviço militar, ou seja, terá que se alistar imediatamente. Passou do prazo de alistamento ou deverá mostrar o tempo que ainda falta  para se apresentar.'''

print()
print('-='*40)
print(f'{"Alistamento Militar":^80}')
print('-='*40)
print()

from datetime import date

nome = str(input('\033[1;32m Qual é seu nome?\033[m ')).strip().upper()
# Ano atual do sistema do PC
atual = date.today().year
nasc = int(input('\033[1;33m Informe o seu ano de nascimento:\033[m '))
idade = atual - nasc
print(f'\033[1;37m Quem nasceu em {nasc} tem {idade} anos em {atual}\033[m.')
# Alistamento obrigatório aos 18 anos
if idade == 18:
    print(f'\033[1;31m Você {nome}, tem que se alistar imediatamente!\033[m' )
elif idade < 18:
    saldo = 18 - idade
    print(f'\033[1;32m {nome}, ainda faltam {saldo} anos para o seu alistamento!', end= '')
    ano = atual + saldo
    print(f' E seu alistamento será em {ano}\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[1;36m {nome}, você já deveria ter se alistado há {saldo} anos.', end = '')
    ano = atual - saldo
    print(f' E seu alistamento foi em {ano}\033[m.')
    
print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()
    

    
    
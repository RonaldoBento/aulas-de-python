#Enunciado: Ano Bissexto
#programa desenvolvido em Python 03
'''Desenvolva um programa que leia um ano qualquer e mostre se ele é Bissexto.'''

print()
print('-='*40)
print(f'{"Ano Bissexto":-^80}')
print('-='*40)
print()

from datetime import date
ano = int(input(' Qual ano gostaria de analisar?\n Coloque 0(zero) para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f' O ano {ano} é Bissexto!')
else:
    print(f' O ano {ano} não é Bissexto!')

print()
print('-='*40)
print(f'{" Programa Finalizado com Sucesso":^80}')
print('-='*40)

    

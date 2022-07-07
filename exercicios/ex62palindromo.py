# Enunciado: Detector de Palíndromo
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia uma frase qualquer e diga se ela é um palíndromo, claro desconsiderando os espaços. Exemplo: A POS A SOPA, O LOBO AMA O BOLO, A TORRE DA DERROTA, 
ANOTARAM A DATA DA MARATONA...'''  

print()
print('-='*40)
print(f'\033[1;33m{"Detector de Palíndromo":^80}\033[m')
print('-='*40)
print()

frase = str(input('\033[1;32m Digite uma frase qualquer:\033[m ')).strip().upper()
palavra = frase.split() # Dividar a frase em partes
junto = ''.join(palavra) # Juntar tudo
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra] # inverso = inverso + junto[letra]
print(f'\033[1;33m O inverso de {junto} é {inverso}.\033[m')
if inverso == junto:
    print('\033[1;33m Temos um Palíndromo!')
else:
    print('\033[1;31m A frase não é um Palíndromo!')  
print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

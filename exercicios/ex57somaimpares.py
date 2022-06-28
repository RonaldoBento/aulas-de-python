# Enunciado: Soma Valores Ímpares e Múltiplos de 3
# Programa Desenvolvido em Python 03
'''Crie um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.'''

print()
print('-='*40)
print(f'\033[1;33m{"Soma Valores Ímpares e Múltiplos de 3":^80}\033[m')
print('-='*40)
print()

soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        contador += 1
print(f'\033[1;32m A soma de todos os {contador} valores foi de {soma}.\033[m')

print()
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

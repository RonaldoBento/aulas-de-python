# Enunciado: Somando Números Impares
# Programa Desenvolvido em Python 03
# Desenvolva um programa que conte entre 0 e 10, além disso, some os número ímpares.

print()
print('-='*40)
print(f'\033[1;32m{"Somando Númenos Impares":^80}\033[m')
print('-='*40)
print()

total10 = 0
soma_impares = 0
for c in range(1, 7): # Repita 6 vezes
    valor = int(input(f'\033[1;37m Informe o {c}º valor inteiro:\033[m '))
    if valor >= 0 and valor <= 10:
        total10 += 1 # total10 = total10 + 1
        if valor % 2 == 1: 
            soma_impares += valor # soma_impares = soma_impares + valor
print(f'\033[1;33m Ao todo foram {total10} valores.\n e nesse intervalo a soma dos números ímpares foi de {soma_impares}.\033[m')

print()
print('-='*40)
print(f'\033[1;35m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

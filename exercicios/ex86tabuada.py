# Enunciado: Tabuada
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que mostre a tabuada de diversos números um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado (digitado) foi negativo.'''

print() 
print('-='*40)
print(f'\033[1;32m{"Tabuada":^80}\033[m')
print('-='*40)
print()

while True:
    print(' \033[1;34m >>> Números negativos para interroper o programa.\033[m')
    n = int(input('\033[1;35m Que ver a tabuada de qual número?\033[m'))
    print('-'*40)
    if n < 0:
        break
    for c in range (0, 11):
        print(f'\033[1;37m {n} X {c} = {n*c}\033[m')
    print('-'*40)
print()
print(f'\033[1;32m Programa Tabuada Encerrado\033[m')

print() 
print('-='*40)
print(f'\033[1;36m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


# Enunciado: Vários Números com Flag
# Programa Desenvolvido com Python 03
'''Desenvolva um progama que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição da parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o FLAG).   '''

print() 
print('-='*40)
print(f'\033[1;35m{"Vários Números com Flag":^80}\033[m')
print('-='*40)
print()

soma = contador = 0
while True:
    n = int(input('\033[1;32m Digite um número inteiro\033[m \033[1;33m[999 para sair do programa]:\033[m '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'\033[1;36m A soma dos {contador} valores foi {soma}\033[m')

print() 
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

# Enunciado: Números Sorteados
# Programa Desenvolvido em Python 03
'''Leia um número inteiro entre 0 e 15 e mostre uma mensagem: se o número sorteado é igual ou diferente do número digitado.'''

print() 
print('-='*40)
print(f'\033[1;33m{" Os Números Sorteados são Iguais":^80}\033[m')
print('-='*40)
print()  

from random import randint

valor = int(input('\033[1;37m Informe um valor inteiro entre 0 e 15:\033[m '))
num_sorteado = randint(0,15)
if valor >= 0 and valor <= 15:
    if valor == num_sorteado: # verifica se o valor sorteado é igual ao valor digitado pelo usuário 
        print('\033[1;37m Os números digitados são iguais!\033[m')
    else:
        print('\033[1;36m Os números digitados são diferentes.\033[') 
    print(f'\033[1;33m Os números digitados: {valor}\033[m')
    print(f'\033[1;35m Os números sorteados: {num_sorteado}\033[m')
    
else:
    print('\033[1;31m ERRO: O número digitado deve estar entre 0 e 15\033[m')
    
print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

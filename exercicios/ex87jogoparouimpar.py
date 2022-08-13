# Enunciado: Jogo do Par ou Impar
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que jogue Par ou Impar com o Computador. O jogo será interrompido quando o jogador Perder, mostrando no final do jogo o total de vitórias consecutivas.'''

print() 
print('-='*40)
print(f'\033[1;32m{"Jogo do Par ou Impar":^80}\033[m')
print('-='*40)
print()

# Importando módulo 
from random import randint
v = 0 # vitória recebe (começa com zero ) 0

while True:
    player = int(input('\033[1;37m Informe um número inteiro para iniciar:\033[m '))
    pc = randint (0,1) # computador "pensa"  entre zero e um
    total = player + pc
    tipo = ""
    while tipo in "pi":
        tipo = str(input('\033[1;37m Digite Par ou Impar? [P/I]')).strip().lower()[0]
        print(f' Você jogou {player} e o computador {pc}. Total de {total}', end= "")    
        print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR\033[m ')
        if tipo == "p":
            if total % 2 == 0:
                print('\033[1;33m JOGADOR VENCEU!\033[m')
                v += 1 # v = v + 1
            else:
                print('\033[1;31m JOGADOR PERDEU!\033[m')
                break
        elif tipo == "i":
            if total % 2 == 1:
                print('\033[1;33m JOGADOR VENCEU!\033[m')
                v += 1 # v = v + 1
            else:
                print('\033[1;31m JOGADOR PERDEU!\033[m')
                break
        print()        
        print(f'\033[1;33m{" VAMOS JOGAR NOVAMENTE?":^80}\033[m')
    break    
print()
print(f'\033[1;32m JOGADOR VENCEU {v} VEZES.\033[m')
print()
print('-'*80)
print()
print(f'\033[1;31m{" GAME OVER":^80}\033[m')

print() 
print('-='*40)
print(f'\033[1;36m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

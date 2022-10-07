# Enunciado: Programa para criar um contador através de menus.
# Programa Desenvolvido em Python 03

print() 
print('-='*40)
print(f'\033[1;31m{"Contador Através de Menus. ":^80}\033[m')
print('-='*40)
print()

from time import sleep 
from rich.table import Table

while True:
    print('''\033[1; 37m
              
                |=================|
                |    M E N U    |
                |=================|
                | [1] De 0 até 10 |
                | [2] De 10 até  |
                | [3] Sair      |
                |=================|\033[m''')
    print()
    opcao = int(input('\033[1;33m Escolha uma opção: '))
    if opcao == 1:
        for c in range(0,11,1):
            print( c, '..',  end ='') 
    elif opcao == 2:
        for c in range(10,-1,-1):
           print( c, '..',  end ='') 
    elif opcao == 3:
        break
    else:
        print('\033[1;31m Opção Inválida!\033[m')

sleep(1)
print(' Saindo...\033[m')

print() 
print('-='*40)
print(f'\033[1;31m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


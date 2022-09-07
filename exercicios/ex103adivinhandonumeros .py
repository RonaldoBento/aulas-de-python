# Enunciado: Game - Adivinhando um número entre 1 e 100
# Programa Desenvolvido em Python 03

from rich import print
from random import randint

print()
print('-='*40)
print(f'{"[blue][bold]Adivinhando um número entre 1 e 100":^80}[/][/]')
print('-='*40)
print()


print(f'{"[yellow][bold] Bem-Vindo ao Game de Adivinhação":^80}[/][/]')
print()
sorteado = randint (1, 100)
chute = 0

while chute != sorteado:
    chute = int(input ('\033[1;37m Chute um número inteiro entre 1 e 100:\033[m '))
    if chute == sorteado:
        print ('[yellow][bold] Você Venceu![/][/]')  
    else:
        if chute > sorteado:
            print ('[red][bold] Seu chute foi Alto![/][/]')
        else:
            print ('[green][bold] Seu chute foi Baixo![/][/]')
print()
print (f'{"[red][bold] GAME OVER":^80}[/][/]')

print()
print('-='*40)
print(f'{"[blue][bold]Programa Finalizado com Sucesso":^80}[/][/]')
print('-='*40)
print()

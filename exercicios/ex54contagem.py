# Enunciado: Contagem com laço no intervalo
# Programa Desenvolvido em Python 03
# Desenvolva um programa que faça uma contagem com: INICIO, FIM e PASSOS digitados pelo usuário.

print()
print('-='*40)
print(f'{"Contagem com Laço no Intervalo":^80}')
print('-='*40)
print()

inicio = int(input('\033[1;32m Informe o ínicio da contagem:\033[m '))
fim = int(input('\033[1;33m Informe o fim da contagem:\033[m '))
passo = int(input('\033[1;35m Informe o salto para a realizaçã da contagem:\033[m '))
for c in range(inicio, fim + 1, passo):
    print('', c, end = " ")
print('\n\033[1;34m Terminei de contar!\033[m')    

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()

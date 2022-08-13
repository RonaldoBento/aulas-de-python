# Enunciado: Simulador de Caixa Eletrônico
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que simule o funcionamento de um caixa aletrônico. No inicio pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregue. OBS: Considerando que o caixa possui cédulas de R$ 100.00, R$ 50.00, R$ 20.00, R$ 10.00 e R$ 5,00'''

print() 
print('-='*40)
print(f'\033[1;32m{"Simulador de caixa eletrônico":^80}\033[m')
print('-='*40)
print() 

print(f'\033[1;35m{"Banco Ouro de Tolo":^80}\033[m')
print()
valor = int(input('\033[1;37m Que valor inteiro você quer sacar? R$\033[m '))
total = valor
cedula = 100 # Cédula vai começar com 100 reais
total_cedula = 0
while True: 
    if total >= cedula:
        total -= cedula 
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f' \033[1;37mTotal de {total_cedula} cédulas de R$ {cedula}\033[m')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        total_cedula = 0
        if total == 0:
            break
print()
print(f'\033[1;33m{"Volte sempre ao nosso Banco!":^80}\033[m')

print() 
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

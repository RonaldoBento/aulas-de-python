# Enunciado: Idade para Votar
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que verifique através da Idade de um individuo, no caso, um eleitor, se ele pode ou não votar. '''

print()
print('-='*40)
print(f'\033[1;32m{"Idade para Votar":^80}\033[m')
print('-='*40)
print()

idade = int(input('\033[1;37m Quantos anos você possui? '))
if idade < 16:
    print(' Você ainda não pode votar! ')
elif idade >= 16 and idade < 18:
    print(' Você pode votar, mas é facutativo! ')
elif idade >= 18 and idade < 70: 
    print(' Você é obrigado a votar! ')
else:
    print(' Você não é mais obrigado a votar, seu voto é facutativo!\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

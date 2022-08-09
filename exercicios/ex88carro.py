# Enunciado: Multa de Trânsito
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que el foi multado. A multa vai custar R$ 9.00 por cada km acima do limite.'''

print() 
print('-='*40)
print(f'\033[1;35m{"Multa de Trânsito":^80}\033[m')
print('-='*40)
print() 

v = float(input('\033[1;37m Qual é a velocidade atual do carro: (km/h) \033[m'))
if v > 80: # Se velocidade for acima de 80km/h
    print('\033[1;31m MULTADO!\033[m \033[1;37m Você excedeu o limite permitido que é de 80km/h\033[m')
    multa = (v - 80) * 9
    print(f'\033[1;33m Você deve pagar uma multa de R$ {multa:.2f}\033[m')
else:
    print('\033[1;37m Tudo certo! Está de acordo com o limite de velocidade!\033[m ')
print()
print('\033[1;36m Tenha um bom dia! Dirija com segurança.\033[m')
    
print() 
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

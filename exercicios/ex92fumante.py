# Calcular a Redução do Tempo de Vida de um Fumante
# Programa Desenvolvido em Python 03
'''Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.'''

print() 
print('-='*40)
print(f'\033[1;36m{"Calcular a Redução do Tempo de Vida de um Fumante":^80}\033[m')
print('-='*40)
print() 

perde_vida = 10.0

cigarro_dia = int(input('\033[1;37m Infomre a quantidade de cigarros fumados durante o dia: '))
anos_fumando = int(input(' Informe a quantidade de anos que você é fumante:\033[m '))
tempo_perdido = (((cigarro_dia * perde_vida) / 60) / 24) * anos_fumando
print(f'\033[1;33m Seu tempo perdido de vida em dias foi de {tempo_perdido * 365:.3f}\033[m') 

print() 
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()
 
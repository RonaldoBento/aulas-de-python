#Enunciado: Verificando as primeiras letras de um texto
#Programa desenvolvido em Python 03
'''Desenvolva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".'''

print()
print('-='*40)
print(f'{"Verificando as primeiras letras de um texto":^80}')
print('-='*40)
print()

cidade = str(input(' Em que cidade você nasceu? ')).strip().upper()

#Começa com a palavra SANTO
print( cidade[:5] == "SANTO") 

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)



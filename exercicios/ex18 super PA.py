#Enunciado: SUPER GERADOR DE P.A COM WHITE
#Programa desenvolvido em Python 03
'''Desenvolva um programa que pergunte ao usuário se ele quer mostrar mais alguns termos
da sua P.A após os 10 primeiros. O Programa encerra quando digitado o número 0 (ZERO).'''

print()
print('-='*40)
print(f'{"SUPER GERADOR DE P.A":^80}')
print('-='*40)
print()

#O Programa encerra quando digitado o número 0.
p = int(input(' Informe o primeiro termo da P.A: '))
r = int(input(' Informe a razão da P.A: '))
termo = p
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <=total:
        print(f' {termo} -' ,end = '')
        termo = termo + r
        contador = contador + 1
    print(f'{" PAUSA"} - ')
    mais = int(input(' Quantos termos você quer mostrar? '))
    
print()
print('-='*40)
print(f'{"PROGRAMA FINALIZADO COM SUCESSO":^80}')
print('-='*40)




      
      
      



      

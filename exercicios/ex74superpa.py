# Enunciado: Super Progressão Aritmética P.A 
# Programa Desenvolvido em Python 03

'''Aprefeçoando o anterior, perguntando para o usuário se ele quer continuar e mostrar alguns termos. O programa encerra quando digitar 0 (zero). '''

print()
print('-='*40)
print(f'\033[1;34m{"Super Progressão Aritmética P.A":^80}\033[m')
print('-='*40)
print()

p = int(input('\033[1;37m Informe o primeiro termo da P.A: '))
r = int(input(' Informe a razão da P.A:\033[m '))
t = p # Termo recebe primeiro
c = 1 # Contador recebe 1
total = 0
mais = 10 # Quantos termos você quer mostrar a mais?
while mais != 0: # flag - O programa encerra quando digitar o número 0
    total += mais
    while c <= total:
        print(' {} - '.format(t), end = "")
        t += r # termo recebe termo + razão
        c += 1
    print('\033[1;33m PAUSA \033[m')
    mais = int(input('\033[1;37m Quantos termos você quer mostrar a mais?\033[m '))
    if mais == 0: # Encerra o programa 
        break
print(f'\033[1;36m Programa finalizado com {total} termos mostrados.\033[m ')

print()
print('-='*40)
print(f'\033[1;33m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

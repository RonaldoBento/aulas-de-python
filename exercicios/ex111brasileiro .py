# Enunciado: Tabela do Campeonato Brasileiro
# Programa Desenvolvido em Python 03 

'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense'''
   
print() 
print('-='*40)
print(f'\033[1;31m{" TABELA DO CAMPEONATO BRASILEIRO":^80}\033[m')
print('-='*40)
print()

times = (
    "Atlético", "Flamengo", "Corinthians", "Palmeiras", "Fluminense",
    "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo",
    "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense",
    "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná"
)

# a) os primeiros 5 colocados:
print(f'a) Primeiros 5 colocados do Brasileirão: \n{times[0:6]}')
print()
# b) Dos últimos o 4 colocados:
print(f'b) Dos últimos o 4 colocados foi: \n{times[-4]}')

# c) Times em ordem alfabética:
print(f'\n Times em ordem alfabética: \n')
for time in sorted(times):
    print(time)

# d) em que posição da tabela está o time da Chapecoense:
chape = times.index('Chapecoense') + 1
print(f' A Chapecoense está na {chape}ª posição.')

print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()


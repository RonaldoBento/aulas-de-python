# Enunciado: SELETOR DE PESSOAS
# Programa Desenvolvido em Python 03 

'''Algoritmo para ler Sexo, Idade e Cor de Cabelo de diversas pessoas 
   e ao final, mostrar:
   => Total de HOMENS com mais de 18 ANOS e cabelos CASTANHOS.
   => Total de MULHERES entre 25 e 30 ANOS e cabelos LOIROS.'''
   
print() 
print('-='*40)
print(f'\033[1;31m{" SELETOR DE PESSOAS ":^80}\033[m')
print('-='*40)
print()
total_homens = 0
total_mulheres = 0

while True:
    
    sexo = str(input('\033[1;33m Informe o sexo [M/F]: \033[m')).strip().upper()
    idade = int(input('\033[1;32m Informe a idade: \033[m'))

    print('''\033[1;37m  
            [1] Preto
            [2] Castanho
            [3] Loiro
            [4] Ruivo\033[m''')
    print()
    
    cabelo = int(input('\033[1;35m Qual é a cor cabelo? \033[m'))
    print()
    if sexo == 'M' and idade > 18 and cabelo == 2:
        total_homens += 1
    if sexo == 'F' and idade >= 25 and idade <= 30 and cabelo == 3:
        total_mulheres += 1
  
    resposta = str(input('\033[1;33m Quer coninuar? [S/N]: \033[m')).strip().upper()
    print()
    if resposta == 'N':
        break
    
print('-='*40)
print(f'\033[1;33m{" RESULTADO FINAL ":^80}\033[m')
print('-='*40)
print(f'\033[1;37m Total de homens com mais de 18 e cabelos castanhos {total_homens}.')
print(f' Total de mulheres entre 25 e 30 e cabelos loiros {total_mulheres}.\033[m ')
    
print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

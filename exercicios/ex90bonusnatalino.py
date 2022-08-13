# Enunciado: Bonus Natalino
# Programa Desenvolvido em Python 03
'''Desenvolva um programa em que os funcionánios de uma empresa que forem solteiros não receberão bonus natalino. Já os funcionários que não forem solteiros e tivirem filhos receberão o valor de seu salário acrescido de 20%. Os funcionários que não forem solteiros e não tiverem filhos receberão um bonus natalino de 15% de seu salário base.'''

print() 
print('-='*40)
print(f'\033[1;32m{"Bonus Natalino":^80}\033[m')
print('-='*40)
print() 

salario = float(input('\033[1;33m Informe o valor do salário do funcionário: R$\033[m '))
estado_civil = str(input('\033[1;37m É solteiro? [S ou N]:\033[m ')).strip().upper()[0]
if estado_civil == "S":
    print('\033[1;37m Você não tem direito ao bonus natalino', end="")
    print(f' e seu salário continua sendo R$ {salario:.2f}\033[m ')
else:
    filhos = str(input('\033[1;33m Possui filhos? [S ou N]:\033[m ')).strip().upper()[0]
    if filhos == "S":
        novo_salario = salario + (salario * 20 / 100)
        print(f'\033[1;37m Seu novo salário natalino é de R$ {novo_salario:.2f}\033[m ')
    else:
        salario2 = salario + (salario * 15 / 100)
        print(f'\033[1;37m Seu novo salário é de R$ {salario2:.2f}\033[m ')
    
print() 
print('-='*40)
print(f'\033[1;32m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 

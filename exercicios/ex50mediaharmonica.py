# Enunciado: Média Harmônica
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia o nome de um aluno e as notas de suas três provas e calcule e exibe a Média Harmônica das provas.'''

print()
print('-='*40)
print(f'{"Média Harmônica":^80}') 
print('-='*40)
print()

nome = str(input('\033[1;37m Informe o nome do(a) aluno(a):\033[m ')).strip().upper()
print('\033[1;33m Entre com as notas do(a) aluno(a):\033[m ')
n1 = float(input('\033[1;37m Informe a primeira nota:\033[m '))
n2 = float(input('\033[1;37m Informe a segunda nota:\033[m '))
n3 = float(input('\033[1;37m Informe a terceira nota:\033[m '))

# A Média Harmônica está relacionado ao Cálculo Matemático das situações envolvendo as grandezas inversamente proporcionais.
mh = 3 / (1 / n1 + 1 / n2 + 1 / n3)
print(f'\033[1;32m A Média Harmônica do(a) aluno(a):{nome} é igual a {mh:.2f}\033[m ')

if mh >= 7.0:
    print(f' {nome} está \033[1;32mAPROVADO.\033[m')
elif mh < 7.0 and mh >= 5.0:
    print(f' {nome} está em \033[1;33mRECUPERAÇÃO.\033[m')
else:
    print(f' {nome} está \033[1;31mREPROVADO.\033[m') 

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()
  
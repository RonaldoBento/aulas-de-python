# Enunciado: Média Aritmética do Aluno
# Programa Desenvolvido em Python 03
'''Crie um programa que leia 3 notas de um aluno e calcule sua Média Aritmética, mostrando uma mensagem no final, de acordo com a média atingida: Se a média for abaixo de 5.0 - Aluno Reprovado
Se a média for entre 5.0 e menor que 7 - Aluno em Recuperação. Se a média for entre 7 ou superior - Aluno Aprovado.'''

print()
print('-='*40)
print(f'{"Calculo da Média Aritmética do Aluno":^80}')
print('-='*40)
print()

nome = str(input(' Informe o nome do aluno: ')).strip().upper()
n1 = float(input(' Informe a \033[1;33m1º nota do aluno:\033[m '))
n2 = float(input(' Informe a \033[1;32m2º nota do aluno:\033[m ' ))
n3 = float(input(' Informe a \033[1;36m3º nota do aluno:\033[m '))
m = (n1 + n2 + n3) / 3
print(f'\033[1;37m Tirando as notas {n1}, {n2} e {n3}, a Média Aritmética do aluno {nome} foi de {m:.1f}\033[m')
if m >= 5.0 and m < 7:
    print(f' O aluno {nome} está em \033[1;33mRECUPERAÇÂO!\033[m')
elif m < 5.0:
    print(f' O aluno {nome} está \033[1;31mREPROVADO!\033[m')
else:
    print(f' O aluno {nome} está \033[1;32mAPROVADO!\033[m')    

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()





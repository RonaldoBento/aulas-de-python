#Enunciado: Multiplique pelo primeiro número
#Programa desenvolvido em Python 03
'''Desenvova um programa que, dados dois números inteiros, some esses números e multiplique pelo primeiro exibindo em seguida, o resultado obtido.'''

print()
print('-='*40)
print(f'{"Multiplique pelo primeiro número somado":^80}')
print('-='*40)
print()

n1 = int(input(' Informe um número inteiro: '))
n2 = int(input(' Informe outro número inteiro: '))
print(f' A soma entre os números {n1} e {n2} é igual a {n1 + n2}')
print(f' Mutiplicando {n1 + n2} com o primeiro número digitado que é {n1}, temos {n1 *(n1 + n2)}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


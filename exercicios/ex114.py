print() 
print('-='*40)
print(f'Total de valores e valores impares"')
print('-='*40)
print()

total = 0
impares = 0
for contador in range (1,11):
    valor = int(input(' Informe um valor inteiro: '))
    if valor >= 0 and valor <= 10:
        total = total + 1
        if valor % 2 == 1:
            impares = impares + valor
print()
print(f' Ao todo foram {total} valores entre 0 e 10.')
print(f' Nesse intervalo, soma de valores impares foi de {impares}.')
print()
print(f' Programa desenvolvido com sucesso.')
print()


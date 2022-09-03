# Enunciado: Caixa Registradora de um Supermecado
# Programa Desenvolvido em Python 03
''' Desenvolva um programa para simular uma caixa registradora de
    supermercado. O caixa deve digitar a quantidade comprada e o
	preço unitário de cada item. O algoritmo deve mostrar: o total
	da compra e a quantidade de volumes comprados.
	Observação: Não se sabe previamente quantos volumes cada
	pessoa tem no seu carrinho. Assim, ao digitar quantidade
	comprada = 0 (zero) indica que não há mais itens e a compra
	pode ser totalizada:
	. SAÍDA: total da compra e quantidade de volumes;
	. ENTRADA: quantidade e preço de cada item;
	. PROCESSAMENTO:
	. Calcular o total do item : item = quantidade * preco_unitario
	. Acumular o total da compra: preco_total = preco_total + item
	. Acumular o total de itens: total_volumes = total_volumes + quantidade'''

print() 
print('-='*40)
print(f'\033[1;31m{" Caixa Registradora de Supermercado":^80}\033[m')
print('-='*40)
print()

quantidade = 1
preco_total = 0
total_volumes = 0

while True:
    # Ao digitar quantidade comprada = 0 (zero) indica que não há mais itens e a compra pode ser totalizada e o looping desfeito.
    if quantidade == 0:
        break
    else:
        quantidade = float(input('\033[1;35m Informe a quantidade comprada do produto:\033[m'))
        preco_unitario = float(input('\033[1;37m Informe o preço unitário de cada item R$ :\033[m '))
        
        item = quantidade * preco_unitario
        preco_total = preco_total + item
        total_volumes = total_volumes + quantidade

print()        
print(f'\033[1;33m O total da compra é igual a {preco_total:.2f}\033[m')
print(f'\033[1;33m A quantidade de volumes comprados foi de {total_volumes}\033[m')

print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

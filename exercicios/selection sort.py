# Algoritmo SELECTION SORT | Algoritmo de Ordenação 
# Programa Desenvolvido em Python 03

'''Implementando a ordenação por seleção (selection sort). Este é um dos algoritmos
mais básicos para ordenação e a sua ideia é bastante intuitiva, de modo que você
pode acabar pensando em algo similar mesmo sem nunca tê-lo visto.
O selection sort é um algoritmo de ordenação com complexidade de tempo quadrática.'''

import random

# Selection Sort

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
            
# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

# Testando

any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]


if __name__ == "__main__":
    print()
    print(''' Listas:
                Números aleatórios: any_numbers, 
                Já ordenados: already_sorted, 
                Ordem inversa: inversed, 
                Elementos repetidos: repeated.''')
    print()
    lista = repeated # Escolha entre uma das listas 
    print(lista)
    selection_sort(lista)
    print("\n Ordenado:")
    print()
    print(lista)
    
        
    






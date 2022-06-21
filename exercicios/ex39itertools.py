# Enunciado: Testando Biblioteca Itertools
# Programa desenvolvido em Python 03

'''A itertools provê uma série de funções de manipulação de iteráveis para
se construir iteradores complexos e úteis!
O módulo forma uma “álgebra iterativa”, tornando possível construir ferramentas
especializadas de forma sucinta e eficiente em Python puro.

O módulo traz três categorias de iteradores:

Iteradores infinitos (Infinite Iterators)
Iteradores combinatórios (Combinatoric Iterators)
Iteradores de encerramento (Terminating Iterators)'''

#Função cycle
'''Função cycle
Assinatura da função: cycle(iterable)

Esta função imprime todos os valores em ordem a partir do iterável iterable
passado como parâmetro. Ele reinicia a impressão do início novamente quando
todos os elementos são impressos de maneira cíclica.
Entenda melhor no exempo a seguir:'''

print()
print('-='*40)
print(f'{"Função Cycle":^80}')
print('-='*40)
print()

from itertools import cycle

contador = 0
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in cycle(entrada): 
  if contador > len(entrada) * 3: 
    break
  else: 
    print(i, end = " ") 
    contador += 1

print()
print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

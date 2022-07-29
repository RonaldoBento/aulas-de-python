# Enunciado: Sequência de Fibonacci
# Programa Desenvolvido em Python 03

print()
print('-='*40)
print(f'\033[1;34m{"Sequência de Fibonacci":^80}\033[m')
print('-='*40)
print()

def fib(n): # Escrever a série de Fibonacci
    a, b = 0 , 1
    while a < n:
        print(a, end= "")
        a, b = b, a + b
    print()
fib(100)
      
print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

# Enunciado: Testando a Instrução Continue
# Programa Desenvolvido em Python 03

print()
print('-='*40)
print(f'\033[1;32m{"Testando a Instrução Continue":^80}\033[m')
print('-='*40)
print()

for n in range(2,10):
    if n % 2 == 0:
        print(f'\033[1;36m Encontrou até mesmo o número: {n}.\033[m')
        continue # Continua com a próxima iteração do laço 
    print(f'\033[1;37m Encontrou o número: {n}.\033[m')
print('\033[1;35m FIM\033[m')

print()
print('-='*40)
print(f'\033[1;33m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

# Enunciado: Progresão Aritmética com a estrutura While
# Programa Desenvolvido em Python 03
# Leia o primeiro termo e a razão de uma P.A, mostrando os 10 primeiros termos da progressão.

print()
print('-='*40)
print(f'\033[1;33m{"Progressão Aritmética (P.A)":^80}\033[m')
print('-='*40)
print()

primeiro = int(input('\033[1;37m Informe o primeiro termo da P.A: '))
razao = int(input(' Informe a Razão da P.A: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f' {termo} - ', end = "")
    termo += razao
    contador += 1 
print('FIM\033[m')
print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

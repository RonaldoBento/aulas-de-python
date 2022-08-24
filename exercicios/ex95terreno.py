# Enunciado: Classificação de Terreno
# Programa Desenvolvido em Python 03

''' Faça um programa que leia a largura e o comprimento de um terreno
    retangular, calculando e mostrando a sua área em m². O programa também
    devemostrar a classificação desse terreno, de acordo com a lista abaixo:
    - Abaixo de 100m² = TERRENO POPULAR
    - Entre 100m² e 500m² = TERRENO MASTER
    - Acima de 500m² = TERRENO VIP'''
    
print()
print('-='*40)
print(f'\033[1;33m{"Classificação de Terreno":^80}\033[m')
print('-='*40)
print()

largura = float(input('\033[1;37m Infomre a Largura do terreno em metros: '))
comprimento = float(input(' Informe o Comprimento do terreno em metros:\033[m '))
area = largura * comprimento
print()
print(f'\033[1;34m A área do terreno retangular é {area:.3f} m².\033[m')
print()
if area < 100: # Abaixo de 100m² = TERRENO POPULAR
    print('\033[1;32m TERRENO POPULAR.\033[m')
elif area >= 100 and area < 500: # Entre 100m² e 500m² = TERRENO MASTER
    print('\033[1;33m TERRENO MASTER.\033[m')
else:
    print('\033[1;36m TERRENO VIP.\033[m')

print()
print('-='*40)
print(f'\033[1;34m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

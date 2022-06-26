# Enunciado: IMC - Indíce de Massa Corporal
# Programa Desenvolvido em Python 03
'''Desenvolva um programa que leia a massa e a altura de uma pessoa . Calcule o IMC e mostre seu STATUS de acordo com a tabela abaixo:
- Abaixo de 18.5 = Abaixo do peso (IMC < 18.5);
- Entre 18.5 e 25 = Peso Ideal (IMC  >=  18.5) e (IMC < 25);
- Entre 25 e 30 = SobrePeso (IMC >= 25) e (IMC < 30);
- Entre 30 e 40 = Obesidade (IMC >= 30) e (IMC < 40);
- Acima de 40 = Obesidade (IMC > = 40). '''

print()
print('-='*40)
print(f'{"IMC - Indíce de Massa Corporal":^80}')
print('-='*40)
print()

massa = float(input('\033[1;32m Qual é seu peso? kg:\033[m '))
altura = float(input('\033[1;36m Qual é sua altura? m:\033[m '))
#Formula para calcular o IMC - Indíce de Massa Corporal: imc = massa / altura²
imc = massa / (altura **2)

print()
print(f'{" STATUS ":=^80}')
print()
print(f'\033[1;33m O IMC  da pessoa analisada é de {imc:.1f}\033[m')
# Aplicando as condições aninhadas para aplicar a tabela
if imc  < 18.5:
    print('\033[1;37m Você está Abaixo do Peso Normal.\033[m')
elif 18.5 <= imc < 25: # elif imc >= 18.5 and imc < 25:
    print('\033[1;32m Você está no Peso Ideal.\033[m')
elif 25 <= imc < 30: # elif imc >= 25 and imc < 30:
    print('\033[1;35m Você está em SobrePeso.\033[m')
elif 30 <= imc < 40: # elif imc >= 30 and imc < 40:
    print('\033[1;34m Você está em Obesidade.\033[m') 
else:
    print('\033[1;31m Você está em Obesidade Mórbida.\033[m')

print() 
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)
print()

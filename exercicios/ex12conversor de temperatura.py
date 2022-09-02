#Enunciado: Conversor de Temperatura
#Programa desenvolvido em Python 03
'''Desenvolva um programa que converta uma temperatura digitada em °C (Celsius)
e converta para °F (Fahrenheit).'''

print()
print('-='*40)
print(f'{"Conversor de Temperatura":^80}')
print('-='*40)
print()

c = float(input(' Informa a temperatura em graus Celsius: °C '))
f = ((9 * c) / 5) + 32 #f = Fahrenheit
print(f' A temperatura de graus Celsius {c}°C corresponde\n a graus Fahrenheit {f}°F.')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)




#Enunciado: Conversor de Temperatura
#Programa desenvolvido em Python 03
'''Desenvolva um programa que converta uma temperatura digitada em ºC (Celsius)
e converta para ºF (Fahrenheit).'''

print()
print('-='*40)
print(f'{"Conversor de Temperatura":^80}')
print('-='*40)
print()

c = float(input(' Informa a temperatura em grau Celsius: ºC '))
f = ((9 * c) / 5) + 32 #f = Fahrenheit
print(f' A temperatura de grau Celsius {c}ºC corresponde\n a grau Fahrenheit {f}ºF.')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)




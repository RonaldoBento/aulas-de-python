# Empresa de Telefonia Bento
# Programa Desenvolvido em Python 03
'''Considere a empresa de telefonia Bento ltda. Abaixo de 200 minuto, a empresa cobra R$ 0.20 por minuto, entre 200 e 400 minutos, o preço é de R$ 0.18. Acima de 400 minutos o preço permitido é de R$ 0.15. Uma promoção onde a tarifa é de R$ 0.08 quando você utiliza mais de 800 minutos. Calcule sua conta de telefone. '''

print() 
print('-='*40)
print(f'\033[1;32m{"Empresa de Telefonia Bento":^80}\033[m')
print('-='*40)
print() 



minutos = int(input('\033[1;37m Infomre quantos minutos você utilizou:\033[m '))
if minutos < 200:
    preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
    
print(f'\033[1;33m Sua conta de telefone ficou em R$ {preco * minutos:.2f}\033[m') 

print() 
print('-='*40)
print(f'\033[1;37m{"Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

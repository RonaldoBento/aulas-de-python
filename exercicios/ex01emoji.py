#Testando a Biblioteca emoji
#Programa desenvolvido em Python 03

print()
print('-='*40)
print(f'{"Teste com Emojis":^80}')
print('-='*40)
print()

import emoji

print(emoji.emojize('Hello!:angel:',use_aliases = True))
print(emoji.emojize('Yes, Python!:sunglasses:',use_aliases = True))
print(emoji.emojize('Good!:dash:',use_aliases = True))
print(emoji.emojize('Continue!:boy:',use_aliases = True))
print(emoji.emojize('Finish!:girl:',use_aliases = True))
print(emoji.emojize('SuperPower!:muscle:',use_aliases = True))
print(emoji.emojize('Fine!:heart:',use_aliases = True))
print(emoji.emojize('NotBad!:poop:',use_aliases = True))
print(emoji.emojize('Sun!:sun:',use_aliases = True))
print(emoji.emojize('Moon!:moon:',use_aliases = True))
print(emoji.emojize('Wars!:bird:',use_aliases = True))
print(emoji.emojize('The End!:baby:',use_aliases = True))
print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)


                    

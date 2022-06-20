#Enunciado: Primeira e Última ocorrência de uma String
#Programa Desenvolvido em Pynthon 03
''''Desenvolva um programa que leia uma frase pelo teclado e mostre:
 - Quantas vezes aparece a letra "A";
 - Em que posição ela apareceu na primeira vez;
 - Em que posição ela apareceu pela última vez.'''
 
print()
print('-='*40)
print(f'{"Primeira e Última Ocorrência de uma String":^80} ')
print('-='*40)
print()
 
frase = str(input(' Digite uma frase qualquer: ')).strip().upper()
#Conta quantas vezes a letra 'A' aparece.
print(f' A letra A aparece {frase.count("A")} vezes na frase.') 
#Encontra e mostra a primeira vez que a letra 'A' aparece.
print(f' A primeira letra A aparece {frase.find("A") + 1} vezes na frase. ')
#Encontra e mostra a última posição da letra 'A'.
print(f' A última letra A aparece na posição {frase.rfind("A") + 1}')

print()
print('-='*40)
print(f'{"Programa Finalizado com Sucesso":^80}')
print('-='*40)

 
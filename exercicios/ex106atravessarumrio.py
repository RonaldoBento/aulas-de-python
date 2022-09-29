# Enunciado: ALGORITMO - ATRAVESSAR A MARGEM DO RIO
# Programa Desenvolvido em Python 03
''' Para atravessar um rio, uma família com um menino (criança) de 30 kg, 
	sua irmã adolescente de 40 kg, sua mãe de 60 kg e seu pai de 100 kg 
	dispõe de um barco a remo maltratado pelo tempo que suporta apenas 100 kg, 
	ou seja, como todos os integrantes da família poderia
    atravessar o rio com total segurança?
       
	ATENÇÃO: A criança não pode atravessar e ficar sozinha.
	  
	Autor: Ronaldo Rodrigues Bento '''

print() 
print('-='*40)
print(f'\033[1;31m{" ATRAVESSAR A MARGEM DO RIO":^80}\033[m')
print('-='*40)
print()     

print('\033[1;33m Suas Opções são: ')
print(' [1] Mãe cruza o rio com sua filha; ')
print(' [2] Pai cruza o rio sozinho; ')
print(' [3] Mãe cruza com seu filho; ')
print(' [4] Filha cruza com seu irmão; ')
print(' [5] Mãe cruza o rio sozinha.\033[m ')
  
print()
opcao = int(input('\033[1;32m Escolha uma opção do Menu:\033[m '))

print('-='*40)

if opcao == 1:
    print('\033[1;37m A mãe (60 kg) cruza o rio com sua filha (40 kg).') 
    print(' Deixando na margem a filha e regressa sozinha;') 
    print(' A mãe (60 kg) cruza o rio novamente com a criança (30 kg) e depois regressa só ') 
    print(' O pai (100 kg) cruza o rio sozinho;')
    print(' A filha (40 kg) regressa só;')
    print(' A mãe (60 kg) cruza o rio com sua filha (40 kg). Parabéns! A Família está SEGURA!\033[m') 
 
elif opcao == 2:
    print('\033[1;33m O pai (100 kg) cruza o rio sozinho. ERRO: O barco não volta sozinho. TENTE DE NOVO!\033[m')	
	
elif opcao == 3:
    print('\033[1;34m A mãe (60 kg) cruza o rio com seu filho (30 kg). ERRO: A criança não pode atravessar e ficar sozinha. TENTE DE NOVO!\033[m') 
    
elif opcao == 4:
    print('\033[1;35m A filha (40 kg) cruza o rio com seu irmão (30 kg). ERRO: A criança não pode atravessar e ficar sozinha. TENTE DE NOVO!\033[m')

elif opcao == 5:
    print('\033[1;36m A mãe (60 kg) cruza o rio sozinha. ERRO: O barco não volta sozinho. TENTE DE NOVO!\033[m')

else:
    print('\033[1;31m Opção Inválida! Tente Novamente!\033[m')       
  
print() 
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print() 


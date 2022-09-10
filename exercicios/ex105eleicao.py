# Enunciado: Eleições 2022
# Programa Desenvolvido em Python 3
# Simulador de uma Eleição de 2ª Turno entre dois candidatos.

print()
print('-='*40)
print(f'\033[1;33m{"ELEIÇÕES 2022":^80}\033[m')
print('-='*40)
print()

candidato_lula = candidato_ciro = brancos = nulos = total_votos = 0
porcentagem_candidato1 =  porcentagem_candidato2 = 0  

while True:  
    print('''\033[1;37m Escolha seu candidato ou tecle 0 [zero] para encerrar a votação:
            1 para o Candidato Lula;
            2 para o Candidato Ciro;
            3 para Branco.\033[m''')
    print()
    print('\033[1;33m Qualquer número diferente de 0, 1, 2 e 3 anulará o seu voto.\033[m')
    voto = int(input('\033[1;37m Digite seu voto:\033[m ')) 
            
    if not voto != 0: # Digitar Zero encerra o programa 
        print('\033[1;31m Votação Encerrada!\033[m') 
        break

    else:
        if candidato_lula == 1: # Soma um voto para o candidato Lula
            candidato_lula += 1
        elif candidato_ciro == 2: # Soma um voto para o candidado Ciro
            candidato_ciro += 1
        elif brancos == 3: # Soma um voto em branco
            brancos += 1
        else:
            nulos += 1 # Opção inválida. Soma um voto nulo
        total_votos = candidato_lula + candidato_ciro + brancos + nulos # Soma total de votos

    # Se houve votos, calcula a porcentagem de votos de cada candidato
    if total_votos > 0:
        porcentagem_candidato1 = (candidato_lula * 100 / total_votos)  
        porcentagem_candidato2 = (candidato_ciro * 100 / total_votos)
        porcentagem_brancos = (brancos * 100) / total_votos
        porcentagem_nulos = (nulos * 100) / total_votos

        print()
        print(f' Total de votos: {total_votos}')
        print(f' Candidato Lula: {candidato_lula}  voto(s) {porcentagem_candidato1:.2f}% do total.' )
        print(f' Candidato Ciro: {candidato_ciro} voto(s) {porcentagem_candidato2:.2f}% do total.')
        print(f' Brancos: {brancos} voto(s) {porcentagem_brancos:.2f}% do total.')
        print(f' Nulos: {nulos} voto(s) {porcentagem_nulos:.2f}% do total.')

print()  
print('-='*40)
print(f'\033[1;32m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()



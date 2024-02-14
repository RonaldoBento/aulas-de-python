# Enunciado: ALGORITMO - ATRAVESSAR A MARGEM DO RIO
# Programa Desenvolvido em Python 03
''' Para atravessar um rio, uma família com um menino (criança) de 30 kg, 
	sua irmã adolescente de 40 kg, sua mãe de 60 kg e seu pai de 100 kg 
	dispõe de um barco a remo maltratado pelo tempo que suporta apenas 100 kg, 
	ou seja, como todos os integrantes da família poderia
    atravessar o rio com total segurança?
       
	ATENÇÃO: A criança não pode atravessar e ficar sozinha na margem do rio;
    Poderá fazer várias viagens; 
    Passou de 100 kg é Game Over.
	  
	Autor: Ronaldo Rodrigues Bento'''

print() 
print('-='*40)
print(f'\033[1;31m{" ATRAVESSAR A MARGEM DO RIO":^80}\033[m')
print('-='*40)
print() 

PESO_MAXIMO_BARCO = 100

listaPersonagens = {
    0: {
        'nome': 'Menino',
        'peso': 30,
        'lado': 'esquerdo',
        'podeFicarSozinho': False,
    },
    1: {
        'nome': 'Menina',
        'peso': 40,
        'lado': 'esquerdo',
        'podeFicarSozinho': True,
    },
    2: {
        'nome': 'Mãe',
        'peso': 60,
        'lado': 'esquerdo',
        'podeFicarSozinho': True,
    },
    3: {
        'nome': 'Pai',
        'peso': 100,
        'lado': 'esquerdo',
        'podeFicarSozinho': True,
    },
}

ladoBarco = 'esquerdo'

# Popula a lista de opções disponíveis recursivamente
def popularOpcoesDisponiveis(opcoesDisponiveis, opcoesSelecionadas):
    for indexPersonagem in listaPersonagens:
        personagem = listaPersonagens[indexPersonagem]

        pesoAtual = getPesoPersonagens(opcoesSelecionadas)

        if personagem['lado'] == ladoBarco and pesoAtual + personagem['peso'] <= PESO_MAXIMO_BARCO and indexPersonagem not in opcoesSelecionadas:
            possivelOpcao = opcoesSelecionadas + [indexPersonagem]
            possivelOpcao.sort()

            if(possivelOpcao not in opcoesDisponiveis):
                if(len(opcoesSelecionadas) == 0 and not personagem['podeFicarSozinho']):
                    continue

                if(not ausenciaPersonagemFicaSozinho(possivelOpcao)):
                    opcoesDisponiveis.append(possivelOpcao)

                popularOpcoesDisponiveis(opcoesDisponiveis, opcoesSelecionadas + [indexPersonagem])

# Retorna o peso dos personagens passados por parâmetro
def getPesoPersonagens(personagens):
    return sum(map(lambda indexPersonagem: listaPersonagens[indexPersonagem]['peso'], personagens))

# Verifica se na ausência dos personagens saindo, algum personagem vai ficar sozinho
def ausenciaPersonagemFicaSozinho(personagensSaindo):
    personagensFicariamSozinhos = list(filter(lambda indexPersonagem: listaPersonagens[indexPersonagem]['lado'] == ladoBarco and indexPersonagem not in personagensSaindo, listaPersonagens))
    return len(personagensFicariamSozinhos) == 1 and not listaPersonagens[personagensFicariamSozinhos[0]]['podeFicarSozinho']

# Printa as opções possíveis que o jogador pode escolher
def printarOpcoesDisponiveis(opcoesDisponiveis):
    for index, opcao in enumerate(opcoesDisponiveis):
        nomes = map(lambda indexPersonagem: listaPersonagens[indexPersonagem]['nome'], opcao)
        print("{} - {}".format(index, ", ".join(nomes)))

# Retorna uma lista de personagens do lado passado por parâmetro
def getPersonagensDoLado(lado):
    return list(filter(lambda indexPersonagem: listaPersonagens[indexPersonagem]['lado'] == lado, listaPersonagens))

# Verifica se o jogo foi vencido
def jogoFinalizado():
    return len(getPersonagensDoLado('esquerdo')) == 0

if(__name__ == '__main__'):
   
    while True:
        opcoes = []
        popularOpcoesDisponiveis(opcoes, [])

        personagensLadoAtual = getPersonagensDoLado(ladoBarco)

        print("\033[1;37m O barco está do lado {}. Os personagens desse lado são: {}\033[m".format(ladoBarco, ", ".join(map(lambda indexPersonagem: listaPersonagens[indexPersonagem]['nome'], personagensLadoAtual))))
        print()
       
        print("\033[1;37m Quais personagens você deseja que remem para o outro lado?\n\033[m ")
        printarOpcoesDisponiveis(opcoes)
        print()

        opcao = int(input("\033[1;32m Escolha uma opção:\033[m "))
        print('-='*40)
        print()

        for indexPersonagem in opcoes[opcao]:
            listaPersonagens[indexPersonagem]['lado'] = 'direito' if ladoBarco == 'esquerdo' else 'esquerdo'

        ladoBarco = 'direito' if ladoBarco == 'esquerdo' else 'esquerdo'

        if(jogoFinalizado()):
            print("\033[1;33m Parabéns, você conseguiu!\033[m")
            break

print() 
print('-='*40)
print(f'\033[1;31m{" Programa Finalizado com Sucesso":^80}\033[m')
print('-='*40)
print()

# Enunciado: Jogo da Velha
# Programa Desenvolvido em Python 03
# Desenvolva um programa no caso o famigerado JOGO DA VELHA.

from random import randint
from time import sleep

#funções
def limparTela():
    print('\n'*100)

def cabecalho():
    print('{:^50}'.format('-=' * 30))
    print('{:^50}'.format('\033[1;34mJOGO DA VELHA\033[m'))
    print('{:^50}'.format('-=' * 30))

def boasvindas():
    limparTela()
    cabecalho()
    print('{:^50}'.format('\033[1;32mBem-vindo ao jogo da velha!\033[m'))
    print('{:^50}'.format('-=' * 30))

def placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, simboloP1):
    limparTela()
    cabecalho()
    if simboloP1 == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif simboloP1 == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'
    print(' '*9, f'{nomeP1[0:15]:.<15}({simboloP1}): {vitoriasP1} vitórias')
    print(' '*9, f'{nomeP2[0:15]:.<15}({simboloP2}): {vitoriasP2} vitórias')
    print(' '*9, f'                    {empates} empates')
    print('{:^50}'.format('-=' * 30))

def tabuleiro (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print('{:^19}'.format('\033[1;37mMAPA DO JOGO\033[m'), '          ', '{:^19}'.format('\033[1;33mJOGO EM ANDAMENTO\033[m'))
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  1  │  2  │  3  │', '          ', f'│  {c1}  │  {c2}  │  {c3}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  4  │  5  │  6  │', '          ', f'│  {c4}  │  {c5}  │  {c6}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  7  │  8  │  9  │', '          ', f'│  {c7}  │  {c8}  │  {c9}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print()
    print('{:^50}'.format('-=' * 30))

def opcaoInicial():
    while True:
        boasvindas()
        print('\033[1;37mEscolha...\n'
              '[0] para conhecer as regras\n'
              '[1] para ser " o "\n'
              '[2] para ser " x "\n\033[m')
        opcao = input('\033[1;35mQual a sua opção? \033[m').strip()
        while opcao != '0' and opcao != '1' and opcao != '2':
            opcao = input('\033[1;35mOpção inválida. Qual a sua opção? [0/1/2] \033[m').strip()
        if opcao == '0':
            regras()
        if opcao == '1' or opcao == '2':
            break
    return opcao

def opcaoPlayer():
    print('\033[1;37mEscolha...\n'
          '[1] para jogar contra o computador\n'
          '[2] para jogar contra outra pessoa\n')
    opcao = input('Qual a sua opção? \033[m').strip()
    while opcao != '1' and opcao != '2':
        opcao = input('\033[1;32mOpção inválida. Qual a sua opção? [1/2] \033[m').strip()
    return opcao

def modoDificil():
    print()
    print('\033[1;37mDeseja jogar em qual dificuldade?\n'
          '[1] normal (movimentos aleatórios pc)\n'
          '[2] difícil (movimentos do pc são calculados)')
    opcao = input('Qual a sua opção? \033[m').strip()
    while opcao != '1' and opcao != '2':
        opcao = input('\033[1;32mOpção inválida. Qual a sua opção? [1/2] \033[m').strip()
    if opcao == '1':
        return False
    else:
        return True

def verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    #validando linhas
    if c1 == c2 and c1 == c3 and c1 != ' ':
        return True
    elif c4 == c5 and c4 == c6 and c4 != ' ':
        return True
    elif c7 == c8 and c7 == c9 and c7 != ' ':
        return True
    #validando colunas
    elif c1 == c4 and c1 == c7 and c1 != ' ':
        return True
    elif c2 == c5 and c2 == c8 and c2 != ' ':
        return True
    elif c3 == c6 and c3 == c9 and c3 != ' ':
        return True
    #validando diagonais
    elif c1 == c5 and c1 == c9 and c1 != ' ':
        return True
    elif c3 == c5 and c3 == c7 and c3 != ' ':
        return True
    else:
        return False

def verificarEmpate(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == ' ' or c2 == ' ' or c3 == ' ' or c4 == ' ' or c5 == ' ' or c6 == ' ' or c7 == ' ' or c8 == ' ' or c9 == ' ':
        return False
    elif verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
        return False
    else:
        return True

def nivelDificil(c1, c2, c3, c4, c5, c6, c7, c8, c9, pc):
    if pc == 'o':
        adv = 'x'
    elif pc == 'x':
        adv = 'o'
    sugestao = 0
    listaOpcoes1 = []
    listaOpcoes2 = []
    listaOpcoes3 = []
    listaOpcoes4 = []
    listaOpcoes5 = []
    listaOpcoes6 = []
    #lista sugestões 1
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == pc and c3 == pc or c4 == pc and c7 == pc or c5 == pc and c9 == pc:
            listaOpcoes1.append(1)
    #vai sugerir casa 2
    if c2 == ' ':
        if c1 == pc and c3 == pc or c5 == pc and c8 == pc:
            listaOpcoes1.append(2)
    #vai sugerir casa 3
    if c3 == ' ':
        if c1 == pc and c2 == pc or c6 == pc and c9 == pc or c5 == pc and c7 == pc:
            listaOpcoes1.append(3)
    #vai sugerir casa 4
    if c4 == ' ':
        if c5 == pc and c6 == pc or c1 == pc and c7 == pc:
            listaOpcoes1.append(4)
    #vai sugerir casa 5
    if c5 == ' ':
        if c4 == pc and c6 == pc or c2 == pc and c8 == pc or c1 == pc and c9 == pc:
            listaOpcoes1.append(5)
    #vai sugerir casa 6
    if c6 == ' ':
        if c4 == pc and c5 == pc or c3 == pc and c9 == pc:
            listaOpcoes1.append(6)
    #vai sugerir casa 7
    if c7 == ' ':
        if c8 == pc and c9 == pc or c1 == pc and c4 == pc or c3 == pc and c5 == pc:
            listaOpcoes1.append(7)
    #vai sugerir casa 8
    if c8 == ' ':
        if c7 == pc and c9 == pc or c2 == pc and c5 == pc:
            listaOpcoes1.append(8)
    #vai sugerir casa 9
    if c9 == ' ':
        if c7 == pc and c8 == pc or c3 == pc and c6 == pc or c1 == pc and c5 == pc:
            listaOpcoes1.append(9)
    #lista sugestões 2
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == adv and c3 == adv or c4 == adv and c7 == adv or c5 == adv and c9 == adv:
            listaOpcoes2.append(1)
    if c2 == ' ':
        if c1 == adv and c3 == adv or c5 == adv and c8 == adv:
            listaOpcoes2.append(2)
    if c3 == ' ':
        if c1 == adv and c2 == adv or c6 == adv and c9 == adv or c5 == adv and c7 == adv:
            listaOpcoes2.append(3)
    if c4 == ' ':
        if c5 == adv and c6 == adv or c1 == adv and c7 == adv:
            listaOpcoes2.append(4)
    if c5 == ' ':
        if c4 == adv and c6 == adv or c2 == adv and c8 == adv or c1 == adv and c9 == adv:
            listaOpcoes2.append(5)
    if c6 == ' ':
        if c4 == adv and c5 == adv or c3 == adv and c9 == adv:
            listaOpcoes2.append(6)
    if c7 == ' ':
        if c8 == adv and c9 == adv or c1 == adv and c4 == adv or c3 == adv and c5 == adv:
            listaOpcoes2.append(7)
    if c8 == ' ':
        if c7 == adv and c9 == adv or c2 == adv and c5 == adv:
            listaOpcoes2.append(8)
    if c9 == ' ':
        if c7 == adv and c8 == adv or c3 == adv and c6 == adv or c1 == adv and c5 == adv:
            listaOpcoes2.append(9)
    #lista sugestões 3
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == pc and c3 == ' ' or c3 == pc and c2 == ' ':
            listaOpcoes3.append(1)
        if c4 == pc and c7 == ' ' or c7 == pc and c4 == ' ':
            listaOpcoes3.append(1)
        if c5 == pc and c9 == ' ' or c9 == pc and c5 == ' ':
            listaOpcoes3.append(1)
    #vai sugerir casa 2
    if c2 == ' ':
        if c1 == pc and c3 == ' ' or c3 == pc and c1 == ' ':
            listaOpcoes3.append(2)
        if c5 == pc and c8 == ' ' or c8 == pc and c5 == ' ':
            listaOpcoes3.append(2)
    #vai sugerir casa 3
    if c3 == ' ':
        if c1 == pc and c2 == ' ' or c2 == pc and c1 == ' ':
            listaOpcoes3.append(3)
        if c6 == pc and c9 == ' ' or c9 == pc and c6 == ' ':
            listaOpcoes3.append(3)
        if c5 == pc and c7 == ' ' or c7 == pc and c5 == ' ':
            listaOpcoes3.append(3)
    #vai sugerir casa 4
    if c4 == ' ':
        if c5 == pc and c6 == ' ' or c6 == pc and c5 == ' ':
            listaOpcoes3.append(4)
        if c1 == pc and c7 == ' ' or c7 == pc and c1 == ' ':
            listaOpcoes3.append(4)
    #vai sugerir casa 5
    if c5 == ' ':
        if c4 == pc and c6 == ' ' or c6 == pc and c4 == ' ':
            listaOpcoes3.append(5)
        if c2 == pc and c8 == ' ' or c8 == pc and c2 == ' ':
            listaOpcoes3.append(5)
        if c3 == pc and c7 == ' ' or c7 == pc and c3 == ' ':
            listaOpcoes3.append(5)
    #vai sugerir casa 6
    if c6 == ' ':
        if c4 == pc and c5 == ' ' or c5 == pc and c4 == ' ':
            listaOpcoes3.append(6)
        if c3 == pc and c9 == ' ' or c9 == pc and c3 == ' ':
            listaOpcoes3.append(6)
    #vai sugerir casa 7
    if c7 == ' ':
        if c8 == pc and c9 == ' ' or c9 == pc and c8 == ' ':
            listaOpcoes3.append(7)
        if c1 == pc and c4 == ' ' or c4 == pc and c1 == ' ':
            listaOpcoes3.append(7)
        if c3 == pc and c5 == ' ' or c5 == pc and c3 == ' ':
            listaOpcoes3.append(7)
    #vai sugerir casa 8
    if c8 == ' ':
        if c7 == pc and c9 == ' ' or c9 == pc and c7 == ' ':
            listaOpcoes3.append(8)
        if c2 == pc and c5 == ' ' or c5 == pc and c2 == ' ':
            listaOpcoes3.append(8)
    #vai sugerir casa 9
    if c9 == ' ':
        if c7 == pc and c8 == ' ' or c8 == pc and c7 == ' ':
            listaOpcoes3.append(9)
        if c3 == pc and c6 == ' ' or c6 == pc and c3 == ' ':
            listaOpcoes3.append(9)
        if c1 == pc and c5 == ' ' or c5 == pc and c1 == ' ':
            listaOpcoes3.append(9)
    #lista sugestões 4
    #vai sugerir casa 5
    if c5 == ' ':
        if c1 == adv or c3 == adv or c7 == adv or c9 == adv:
            listaOpcoes4.append(5)
    #lista sugestões 5
    #vai sugerir casas 1, 3, 7 ou 9
    if c1 == ' ':
        listaOpcoes5.append(1)
    if c3 == ' ':
        listaOpcoes5.append(3)
    if c7 == ' ':
        listaOpcoes5.append(7)
    if c9 == ' ':
        listaOpcoes5.append(9)
    #lista sugestões 6
    if c1 == ' ':
        listaOpcoes6.append(1)
    if c2 == ' ':
        listaOpcoes6.append(2)
    if c3 == ' ':
        listaOpcoes6.append(3)
    if c4 == ' ':
        listaOpcoes6.append(4)
    if c5 == ' ':
        listaOpcoes6.append(5)
    if c6 == ' ':
        listaOpcoes6.append(6)
    if c7 == ' ':
        listaOpcoes6.append(7)
    if c8 == ' ':
        listaOpcoes6.append(8)
    if c9 == ' ':
        listaOpcoes6.append(9)

    #vai sugerir um número com base na situação do jogo
    if len(listaOpcoes1) > 0:
        sugestao = listaOpcoes1[randint(0, len(listaOpcoes1)-1)]
    elif len(listaOpcoes2) > 0:
        sugestao = listaOpcoes2[randint(0, len(listaOpcoes2)-1)]
    elif len(listaOpcoes3) > 0:
        sugestao = listaOpcoes3[randint(0, len(listaOpcoes3)-1)]
    elif len(listaOpcoes4) > 0:
        sugestao = listaOpcoes4[randint(0, len(listaOpcoes4)-1)]
    elif len(listaOpcoes5) > 0:
        sugestao = listaOpcoes5[randint(0, len(listaOpcoes5)-1)]
    else:
        sugestao = listaOpcoes6[randint(0, len(listaOpcoes6)-1)]

    return sugestao

def regras():
    limparTela()
    cabecalho()
    print('|{:^48}|'.format('\033[1;34mREGRAS DO JOGO\033[m'))
    print('{:^50}'.format('-=' * 30))
    print("""
- O tabuleiro  é uma matriz  de três linhas por
três colunas.
- Dois jogadores escolhem uma marcação cada um,
geralmente um círculo (o) e um xis (x).
- Os jogadores jogam alternadamente, uma marcação
por vez, numa lacuna que esteja vazia.
- O objectivo é conseguir três círculos ou três
xis em linha, quer horizontal, vertical ou
diagonal , e ao mesmo tempo, quando possível,
impedir o adversário de ganhar na próxima jogada.
Pronto para jogar?
""")
    input('\033[1;37mTecle enter para continuar!\033[m')

def dica():
    print("""Dica: para jogar, escolha o número de uma casa que
      esteja disponível no tabuleiro da direita.
Digite " novo " para reiniciar a rodada atual.
Digite " trocar " para novos jogadores.
Digite " zerar " para zerar o placar.
Digite " sair " para encerrar o aplicativo.""")
    print('{:^50}'.format('=' * 50))

#execução
jogada = ''
while True:
    # inicializando variaveis do jogo
    nomeP1 = ''
    nomeP2 = ''
    simboloP1 = ''
    simboloP2 = ''
    vitoriasP1 = 0
    vitoriasP2 = 0
    empates = 0
    proximoJogador = ''
    # variaveis dos campos do tabuleiro
    c1 = ' '
    c2 = ' '
    c3 = ' '
    c4 = ' '
    c5 = ' '
    c6 = ' '
    c7 = ' '
    c8 = ' '
    c9 = ' '

    opcaoUsuario = opcaoInicial()
    nomeP1 = input('\033[1;34mQual o seu nome? \033[m').strip().upper()
    if opcaoUsuario == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif opcaoUsuario == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'

    jogadores = opcaoPlayer()
    if jogadores == '2':
        nomeP2 = input('\033[1;32mQual o nome do segundo jogador? \033[m').strip().upper()
    else:
        dificil = modoDificil()
        nomeP2 = 'Computador'

    while True:
        if jogada == 'sair':
            break
        elif jogada == 'trocar':
            jogada = ''
            break
        elif jogada == 'novo':
            c1 = ' '
            c2 = ' '
            c3 = ' '
            c4 = ' '
            c5 = ' '
            c6 = ' '
            c7 = ' '
            c8 = ' '
            c9 = ' '
        elif jogada == 'zerar':
            vitoriasP1 = 0
            vitoriasP2 = 0
            empates = 0
            # variaveis dos campos do tabuleiro
            c1 = ' '
            c2 = ' '
            c3 = ' '
            c4 = ' '
            c5 = ' '
            c6 = ' '
            c7 = ' '
            c8 = ' '
            c9 = ' '

        placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
        tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        dica()

        if proximoJogador == '' or proximoJogador == nomeP2:
            proximoJogador = nomeP1
            proximoSimbolo = simboloP1
        else:
            proximoJogador = nomeP2
            proximoSimbolo = simboloP2

        while True:
            if jogadores == '1' and proximoJogador == 'Computador':
                if dificil:
                    jogada = str(nivelDificil(c1, c2, c3, c4, c5, c6, c7, c8, c9, simboloP2))
                else:
                    jogada = str(randint(1, 9))
            else:
                jogada = input(f'É a vez do {proximoJogador}({proximoSimbolo}): ').strip().lower()
            if jogada == 'sair' or jogada == 'trocar' or jogada == 'zerar' or jogada == 'novo':
                break
            if jogada.isnumeric():
                if int(jogada) >= 1 or int(jogada) <= 9:
                    if jogada == '1' and c1 == ' ':
                        c1 = proximoSimbolo
                        break
                    elif jogada == '2' and c2 == ' ':
                        c2 = proximoSimbolo
                        break
                    elif jogada == '3' and c3 == ' ':
                        c3 = proximoSimbolo
                        break
                    elif jogada == '4' and c4 == ' ':
                        c4 = proximoSimbolo
                        break
                    elif jogada == '5' and c5 == ' ':
                        c5 = proximoSimbolo
                        break
                    elif jogada == '6' and c6 == ' ':
                        c6 = proximoSimbolo
                        break
                    elif jogada == '7' and c7 == ' ':
                        c7 = proximoSimbolo
                        break
                    elif jogada == '8' and c8 == ' ':
                        c8 = proximoSimbolo
                        break
                    elif jogada == '9' and c9 == ' ':
                        c9 = proximoSimbolo
                        break
                    else:
                        if jogadores == '2':
                            print('\033[1;31mOpção inválida, por favor escolha uma casa que esteja disponível e digite seu número!\033[m')
                else:
                    if jogadores == '2':
                        print('\033[1;31mOpção inválida, por favor escolha uma casa que esteja disponível e digite seu número!\033[m')
            else:
                if jogadores == '2':
                    print('\033[1;31mOpção inválida, por favor escolha uma casa que esteja disponível e digite seu número!\033[m')

        if jogadores == '1' and proximoJogador == 'Computador':
            print('\033[1;32mO computador está jogando, por favor aguarde!\033[m')
            sleep(3)


        if verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
            if proximoJogador == nomeP1:
                vitoriasP1 += 1
            else:
                vitoriasP2 += 1
            placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
            tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
            if jogadores == '1' and proximoJogador == nomeP2:
                print('\033[1;35mQue pena! Você perdeu!\033[m')
            else:
                print(f'\033[1;33mParabéns {proximoJogador}({proximoSimbolo}), você venceu!\033[m')
            opcao = input('\033[1;34mDeseja continuar jogando? [S/N]\033[m ').strip().upper()
            while opcao != 'S' and opcao != 'N':
                opcao = input('\033[1;31mOpção inválida! Deseja continuar jogando? [S/N] \033[m').strip().upper()
            if opcao == 'S':
                jogada = 'novo'
            else:
                jogada = 'sair'
        elif verificarEmpate(c1, c2, c3, c4, c5, c6, c7, c8, c9):
            empates += 1
            placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
            tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
            print('\033[1;33mEssa rodada empatou!\033[m')
            opcao = input('\033[1;32mDeseja continuar jogando? [S/N]\033[m ').strip().upper()
            while opcao != 'S' and opcao != 'N':
                opcao = input('\033[1;31mOpção inválida! Deseja continuar jogando? [S/N] \033[m').strip().upper()
            if opcao == 'S':
                jogada = 'novo'
            else:
                jogada = 'sair'

    if jogada == 'sair':
        print('='*50)
        print('\033[1;34mObrigado por jogar! Espero que tenha gostado!\033[m')
        print('-='*30)
        break

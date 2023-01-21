# sistema.py
#Enunciado:
'''Crie um pequeno Sistema Modularizado que permite cadastrar pessoas pelo nome e dados
em Arquivos de texto simples. O Sistema só terá 2 opções: Cadastrar uma nova pessoa e
listar todas as pessoas cadastradas. '''

from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([' Ver pessoas cadastradas',' Cadastrar nova pessoa',' Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input(' Informe o nome: '))
        idade = leiaInt(' Informe a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho(' Saindo do Sistema...Até logo!')
        break
        
    else:
        # Digitou uma opção errada no menu
        print(' ERRO: Digite uma opção válida do menu.')
        sleep(2)

    


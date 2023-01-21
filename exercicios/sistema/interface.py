# interface.py

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print(' ERRO: por favor, digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print(' Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c +=1
    print(linha())
    opc = leiaInt('SUA OPÇÃO: ')
    return opc



    

# Python Turtle Graphics
# Projeto Turtle Race
# Enunciado: Corrida gráfica com tartarugas
# Programa Desenvolvido em Python 03
# Módulo Turtle e Random

# Importando módulos
import turtle, random

# Utilizando a função Turtle() do módulo turtle
tartaruga = turtle.Turtle() # Criando tartarugas

# Posição inicial para a criação das linhas do cenário: Tuplas(x,y)
posicao_inicial = (-300,200)
espacamento = 30 # Espaçamento de 30 pixel

# Desativando a caneta antes de qualquer movimento 
tartaruga.penup() # subir caneta

# Movendo a tartaruga para posição inicial e apontando para baixo
tartaruga.right(90)
tartaruga.setpos(posicao_inicial[0], posicao_inicial[1])

# Faça o passo 20 vezes, para criar 20 linhas
for step in range(0,20): # Escrevendo o número de linhas
    tartaruga.write(step + 1) # Step + 1 (um), pois começa com 0 (zero)
    tartaruga.pendown() # Ativando a caneta
    # Criando linhas pontilhadas de tamanho 400
    for step in range(0,40):
        if step % 2 == 0: # Ativando ou desativando a caneta
            tartaruga.penup()
        else:
            tartaruga.pendown()
            # Anda 10 pixel para frente
        tartaruga.forward(10)
    tartaruga.penup() # Desativando a caneta
    
    # Partindo para a próxima posição
    novo_x = tartaruga.pos()[0] + espacamento
    novo_y = posicao_inicial[1]
    tartaruga.setpos(novo_x, novo_y)
    
# Dados com nomes e cores das tartarugas
nomes = ["Duda", "Caio", "Lucas", "Pedro", "Laura"]
cores = ["red", "blue", "yellow", "green", "purple"]
tartarugas = dict() # Dicionário que irá manter as tartarugas

# Posição de largada
posicao_largada = (-330,150)
espacamento = 50

# Criando cada tartaruga
for nome, cor in zip(nomes, cores):
    tartarugas[nome] = turtle.Turtle()
    tartarugas[nome].shape("turtle")
    tartarugas[nome].color(cor)
    
    # Movendo para a posição de largada
    pos_x = posicao_largada[0]
    pos_y = posicao_largada[1] - (espacamento * len(tartarugas))
    tartarugas[nome].penup()
    tartarugas[nome].setpos(pos_x, pos_y)
    passos = 8 # Passos para dar uma volta completa
    for passo in range(0, passos):
        tartarugas[nome].right(360 / passos)
    tartarugas[nome].pendown()

# Váriavel para armazenar o nome da tartaruga vencedora
vencedora = ""
while not vencedora: # Enquanto não houver vencedora
    # Váriavel nomes é uma lista com todos os nomes das tartarugas
    for nome in nomes:
        # Obtendo a distância aleatória
        distancia = random.randint(1,5) # Gerando um número entre 1 e 5
        # Elaborando com que a tartaruga anda numa distância
        tartarugas[nome].forward(distancia)
        # Verificando se a tartaruga venceu
        if tartarugas[nome].pos()[0] > 300:
            vencedora = nome
            break

# Tartaruga que desenhou a pista decorrida
tartaruga.penup()
tartaruga.setposition(0,-300)
mensagem = " A Tartaruga vencedora foi: {} ".format(vencedora)

# Fonte com nome, tamanho e forma
fonte = ("Comic Sans",20, "bold")

# Texto, move a tartaruga para o final, alinhamento e fonte
tartaruga.write(mensagem, True, "center", fonte)

# Movendo a tartaruga vencedora
tartarugas[vencedora].penup()
tartarugas[vencedora].setposition(0, -330)

# Comemorando
while True: # Enquanto verdadeiro
    tartarugas[vencedora].right(10)
# "__main__":    
tartarugas.mainloop()


     
 
        
     
     

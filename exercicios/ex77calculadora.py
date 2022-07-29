# Coding: utf-8
# Enunciado: Desenvovimento de Interface Gráfica com Módulo Tkinter
# Programa Desenvolvido em Python 03
# Calculadora Simples

from tkinter import *

def bt_click():
    if str(ent1.get()).isnumeric() and str (ent2.get()).isnumeric():
        num1 = int(ent1.get())
        num2 = int(ent2.get())
        
        lb['text'] = 'Soma:', num1 + num2
        lb1['text'] = 'Subtração:', num1 - num2
        lb2['text'] = 'Divisão:', num1 / num2
        lb3['text'] = 'Multiplicação:', num1 * num2
    else:
        lb['text'] = 'Valores Inválidos'
        lb1['text'] = 0
        lb2['text'] = 0
        lb3['text'] = 0

# Componentes da janela
janela = Tk()

ent1 = Entry(janela)   # Entrada 1
ent1.place(x = 100, Y = 80)

ent2 = Entry(janela)   # Entrada 2
ent2.place(x = 100, Y = 110)

bt = Button(janela, background = 'silver', font = 25, text = 'ENTER', width = 20, command = bt_click) # Botão ENTER
bt.place(x = 70, y = 140)

lb = Label(janela, font = 25, text = 'Soma')
lb.place(x = 100, y =  180)

lb1 = Label(janela, font = 25, text = 'Subtração')
lb1.place(x = 100, y =  200)

lb2 = Label(janela, font = 25, text = 'Divisão')
lb2.place(x = 100, y =  220)

lb3 = Label(janela, font = 25, text = 'Multiplicação')
lb3.place(x = 100, y =  240)

lb4 = Label(janela, font = 30, text = 'Calculadora')
lb4.place(x = 110, y =  20)

lb5 = Label(janela, font = 30, text = 'Valor 1')
lb5.place(x = 30, y =  77)

lb5 = Label(janela, font = 25, text = 'Valor 2')
lb5.place(x = 30, y =  110)

janela.geometry('300x300+300+300')
janela.title('Calculadora Simples')
janela.mainloop()



# Enunciado: Tkinter - Testando o pacote (Interface Python para tcl/Tk)
# GUI - Graphic User Interface (Interface Gráfica de usuário) 
# Módulo Tkinter

from tkinter import *
def bt_click():
    print('bt_click')
    lb['text'] = 'Congratulations'
    
janela = Tk()
janela.geometry('400x200+200+200')
janela['background'] = 'silver'

bt = Button(janela, width=20, font=25, text='START', command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela,background='silver', font=25, text='PRESS START')
lb.place(x=150, y=150)
janela.mainloop()

    

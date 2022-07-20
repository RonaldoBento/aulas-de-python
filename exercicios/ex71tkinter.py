# Enunciado: Tkinter - Testando o pacote (Interface Python para tcl/Tk)
# GUI - Graphic User Interface (Interface Gráfica de usuário) 

from tkinter import*

janela = Tk()
janela.title('Primeiro Exemplo')
janela.geometry('200x200+100+100')
janela['background'] = 'silver'
lb = Label (janela,background = 'silver', font=25, text= 'Olá, Mundo!')
lb.place(x=70, y= 70)
janela.mainloop()

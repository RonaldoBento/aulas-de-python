#Programa desenvolvido no Python 3

from cgitb import text
from ctypes import alignment
from email import charset
from re import T
from struct import pack
from tkinter import *
from tkinter.ttk import Style
from turtle import bgcolor, right

root = Tk()

def acess():
    statusMsg.config(text="")
    user = entryUsername.get()
    password = entryPassword.get()

    sucessMsg = "Login efetuado com sucesso!!"
    ErrorMsg = "Dados incorretos, tente novamente!!"
    emptyFieldsMsg = "Por favor preencha ambos os campos!!"

    if user == "" or password == "":
        statusMsg.config(text=emptyFieldsMsg, foreground="black",
                         background="orange", font="Verdana")
    elif user == "testando" and password == "123":
        statusMsg.config(text=sucessMsg, foreground="white",
                         background="green", font="Verdana")
        newWindow = Tk()
        newWindow.geometry("400x400+200+200")
        loggedMsg = Label(newWindow, text="Logado com sucesso no CPanel!!",
                          font="verdana", foreground="white", background="green")
        loggedMsg.place(relwidth=1, relheight=1)

    else:
        statusMsg.config(text=ErrorMsg, foreground="white",
                         background="red", font="Verdana")

    entryUsername.delete(0, END)
    entryPassword.delete(0, END)


root.title("Welcome to system")
root.geometry("400x400+200+200")

# FORM TITULE
lblTitle = Label(root, text="Acess to CPanel",
                 foreground="white", background="black", font="Verdana")
lblTitle.place(relwidth=1, relheight=0.2)

# USERNAME FRAME
inputUsernameFrame = LabelFrame(root)
inputUsernameFrame.place(relwidth=1, relheight=0.1, rely=0.21)
usernameLabel = Label(inputUsernameFrame, text="Username",
                      foreground="white", background="black")
usernameLabel.place(relwidth=.4, relheight=1)
entryUsername = Entry(inputUsernameFrame)
entryUsername.place(relwidth=.6, relheight=1, relx=0.41)

# PASSOWRD FRAME
inputPasswordFrame = LabelFrame(root)
inputPasswordFrame.place(relwidth=1, relheight=0.1, rely=0.32)
passwordLabel = Label(inputPasswordFrame, text="Password",
                      foreground="white", background="black")
passwordLabel.place(relwidth=.4, relheight=1)
entryPassword = Entry(inputPasswordFrame, show="*")
entryPassword.place(relwidth=.6, relheight=1, relx=0.41)

# ACESS CPANEL BTN
acessBtn = Button(root, text="Acess CPanel", foreground="black",
                  background="orange", font="Verdana", command=acess)
acessBtn.place(relwidth=.5, relheight=.1, relx=.25, rely=0.45)

# ACESS MENSAGES
statusMsg = Label(root, text="")
statusMsg.place(relwidth=1, relheight=.1, rely=0.7)


root.mainloop()

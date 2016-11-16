from Views import Results_View
from Tkinter import *


class License:

    def __init__(self, master):
        top = Toplevel(master)
        top.resizable(width=False, height=False)
        top.title("Licencia")
        _text = open("C:\\Users\\lossi\\Dropbox\\Escuela\\Facultad de Ingenieria\\3er Semestre\\PROBABILIDAD\\Proyecto_Proba\\LICENSE.txt", 'r')

        scroll = Scrollbar(top)
        scroll.pack(side=RIGHT, fill=Y)
        listbox = Listbox(master=top, yscrollcommand=scroll.set, selectmode=EXTENDED, width=65, height=40)
        for line in _text:
            listbox.insert(END, line)

        listbox.pack(side=LEFT)
        scroll.config(command=listbox.yview)
        _text.close()

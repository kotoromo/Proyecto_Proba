from Views import Results_View
from Tkinter import *


class License:

    def __init__(self, master):
        top = Toplevel(master)
        top.title("Licencia")
        _text = open('./LICENSE.txt', 'r')

        scroll = Scrollbar(top)
        scroll.pack(side=RIGHT, fill=Y)
        listbox = Listbox(master=top, yscrollcommand=scroll.set, selectmode=EXTENDED, width=65, height=40)
        for line in _text:
            listbox.insert(END, line)

        listbox.pack(side=LEFT)
        scroll.config(command=listbox.yview)
        _text.close()

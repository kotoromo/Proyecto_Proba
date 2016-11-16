from Tkinter import *


class ResultsView:

    def __init__(self, master, inputs_list):
        self.master = master
        self.inputs_list = inputs_list
        self.draw()

    def draw(self):
        print self.inputs_list
        top = Toplevel(master=self.master)
        top.title("Resultados: ")
        labels_list = []

        i = 0
        j = 0

        for _list in self.inputs_list:
            labels_list.append(Label(top, text=_list[0]))
            labels_list.append(Label(top, text=_list[1]))


        for label in labels_list:
            label.pack()

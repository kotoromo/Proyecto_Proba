# -*- coding: utf-8 -*-

from Distribution_View import *
from Tkinter import *


class BernoulliView(DistributionView, Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame = Frame(master)
        self.btn = None

    def get_frame(self):
        return self.frame

    def draw(self):
        self.frame.pack()
        frame = self.frame

        #frame.grid(row=0)

        succ_label = Label(frame, text="Número de Éxitos: ")
        ind_var_label = Label(frame, text="Variable Independiente: ")

        succ_entry = Entry(frame)
        ind_var_entry = Entry(frame)

        submit_btn = Button(frame, text="Calcular")
        self.btn = submit_btn

        succ_label.grid(row=0, column=0)
        ind_var_label.grid(row=1, column=0)

        succ_entry.grid(row=0, column=1)
        ind_var_entry.grid(row=1, column=1)
        submit_btn.grid(columnspan=2)

    def clear(self):
        self.btn.grid_forget()
        self.frame.pack_forget()


# -*- coding: utf-8 -*-
from Distributions import Bernoulli
from Distribution_View import *
from Views import Results_View
from Tkinter import *
import matplotlib.pyplot as plt

class BernoulliView(DistributionView, Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame = Frame(master)
        self.btn = None
        self.results_list = None
        self.entry_1 = None
        self.entry_2 = None
        self.success = None

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

        self.entry_1 = succ_entry
        self.entry_2 = ind_var_entry

        submit_btn = Button(frame, text="Calcular", command=self.maketop)
        self.btn = submit_btn


        succ_label.grid(row=0, column=0)
        ind_var_label.grid(row=1, column=0)

        succ_entry.grid(row=0, column=1)
        ind_var_entry.grid(row=1, column=1)
        submit_btn.grid(columnspan=2)


    def maketop(self):
        self.success = self.entry_1.get()

        bernoulli = Bernoulli.Bernoulli(self.entry_1.get(), self.entry_2.get())

        results_list = [
            [u"Distribución: ", bernoulli.getDistribution()],
            [u"Media: ", bernoulli.getMed()],
            [u"Varianza: ", bernoulli.getVar()]
        ]

        self.distribution = bernoulli.getDistribution()

        print "click!"
        print self.results_list
        top = Results_View.ResultsView(self.master, results_list)
        self.plot()


    def clear(self):
        self.btn.grid_forget()
        self.frame.pack_forget()

    def plot(self):
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.plot([int(self.success)], [self.distribution], 'ro')
        plt.axis([0, 1, 0, 1])
        plt.show()



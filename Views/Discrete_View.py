# -*- coding: utf-8 -*-
from Distributions.Discrete import Discrete
from Distribution_View import *
from Views import Results_View
from Tkinter import *
import matplotlib.pyplot as plt

class DiscreteView(DistributionView, Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame = Frame(master)
        self.btn = None
        self.results_list = None
        self.entry_1 = None
        self.entry_2 = None
        self.space = None
        self.ran_var = None
        self.distribution = None
        self.med = None
        self.var = None
        self.bernoulli = None

    def get_frame(self):
        return self.frame

    def draw(self):
        self.frame.pack()
        frame = self.frame

        #frame.grid(row=0)

        space_label = Label(frame, text="Tamaño del Espacio Muestral: ")

        space_entry = Entry(frame)

        self.entry_1 = space_entry

        submit_btn = Button(frame, text="Calcular", command=self.maketop)
        self.btn = submit_btn

        space_label.grid(row=0, column=0)

        space_entry.grid(row=0, column=1)

        submit_btn.grid(columnspan=2)


    def maketop(self):
        self.space = self.entry_1.get()

        bernoulli = Discrete(self.entry_1.get())
        self.bernoulli = bernoulli

        results_list = [
            [u"Probabilidad: ", bernoulli.getProbability()],
            [u"Media: ", bernoulli.getMed()],
            [u"Varianza: ", bernoulli.getVar()]
        ]

        self.distribution = bernoulli.getProbability()
        self.med = bernoulli.getMed()
        self.var = bernoulli.getVar()

        print "click!"
        print self.results_list
        top = Results_View.ResultsView(self.master, results_list)
        self.plot()


    def clear(self):
        self.btn.grid_forget()
        self.frame.pack_forget()

    def plot(self):
        plt.grid(True)

        plt.xlabel(r'$P[x=k]$')
        plt.ylabel(r'$k$')
        plt.title(u'Distribución Discreta Unitaria'+' $f_x(x)$')
        plt.text(float(self.space)-1, self.distribution-.1, r'$\mu_x='+str(self.med)+',\ \sigma^2_x='+str(self.var)+'$'+
                 ', $f_x(x)='+str(self.distribution)+'$')

        plt.text(float(self.space), self.distribution+0.03,
                 r'$k=' + str(self.space) + ',\ P[x=k]=' + str(self.distribution) + '$')
        plt.plot([float(self.space)], [self.distribution], 'ro')
        plt.axis([0, float(self.space)+10, 0, float(self.distribution)+10])

        list_aux = []
        list_k = []
        for i in range(0, int(self.space)):
            probability = self.bernoulli.getProbability()
            list_aux.append(probability)
            list_k.append(i)
            k = i

            i+=1

        plt.plot([list_k], [list_aux], marker='o', linestyle='--')


        plt.show()



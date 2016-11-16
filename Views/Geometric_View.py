# -*- coding: utf-8 -*-
from Distributions.Geometric import Geometric
from Distribution_View import *
from Views import Results_View
from Tkinter import *
import matplotlib.pyplot as plt
from Utilities.Maths import Maths


class GeometricView(DistributionView, Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.frame = Frame(master)

        self.btn = None

        self.results_list = None

        self.entry_1 = None
        self.entry_2 = None

        self.success = None
        self.essays = None
        self.probability = None

        self.probability = None
        self.med = None
        self.var = None

        self.binomial = None

    def get_frame(self):
        return self.frame

    def draw(self):
        self.frame.pack()
        frame = self.frame

        succ_label = Label(frame, text="Probabilidad de Éxito: ")
        essay_label = Label(frame, text="Número de Ensayos: ")

        succ_entry = Entry(frame)
        essay_entry = Entry(frame)

        self.entry_1 = succ_entry
        self.entry_2 = essay_entry

        submit_btn = Button(frame, text="Calcular", command=self.maketop)
        self.btn = submit_btn

        succ_label.grid(row=0, column=0)
        essay_label.grid(row=1, column=0)

        succ_entry.grid(row=0, column=1)
        essay_entry.grid(row=1, column=1)

        submit_btn.grid(columnspan=2)

    def maketop(self):
        self.success = self.entry_1.get()
        self.essays = self.entry_2.get()

        binomial = Geometric(self.entry_1.get(), self.entry_2.get())
        self.binomial = binomial

        results_list = [
            [u"Probabilidad: ", binomial.getProbability()],
            [u"Media: ", binomial.getMed()],
            [u"Varianza: ", binomial.getVar()]
        ]

        self.probability = binomial.getProbability()
        self.med = binomial.getMed()
        self.var = binomial.getVar()

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
        plt.title(u'Distribución Geométrica'+' $f_x(x; n, p)$')
        plt.text(Maths.convertToDecimal(self.success)-1, self.probability-.1, r'$\mu_x='+str(self.med)+',\ \sigma^2_x='+str(self.var)+'$'+
                 ', $f_x(x; n, p)='+str(self.probability)+'$')

        plt.text(Maths.convertToDecimal(self.success), self.probability+0.03,
                 r'$k=' + str(self.success) + ',\ P[x=k]=' + str(self.probability) + '$')
        plt.plot([float(Maths.convertToDecimal(self.success))], [self.probability], 'ro')
        plt.axis([0, float(Maths.convertToDecimal(self.success))+10, 0, float(self.probability)+10])

        list_aux = []
        list_k = []
        for i in range(0, int(self.essays)):
            self.binomial.set_X(i)
            probability = self.binomial.getProbability()
            list_aux.append(probability)
            list_k.append(i)
            k = i

            i+=1

        plt.plot([list_k], [list_aux], marker='o', linestyle='--')


        plt.show()
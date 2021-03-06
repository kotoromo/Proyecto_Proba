# -*- coding: utf-8 -*-
import subprocess
from Tkinter import *
from Views.Discrete_View import DiscreteView
from Utilities import util
from Views import Bernoulli_View
from Views.Binomial_View import BinomialView
from Views.NegativeBinomial_View import NegativeBinomialView
from Views.Geometric_View import GeometricView
from Views import Distribution_View
from Views.Licence_View import License
from Views.Info_View import InfoView


class View:
    master = Tk()
    master.title(u"Calculadora de Distribuciones Binomiales")
    master.resizable(width=False, height=False)
    master.minsize(width=350, height=450)
    fi_logo = PhotoImage(file="C:\\Users\\lossi\\Dropbox\\Escuela\\Facultad de Ingenieria\\3er Semestre\\PROBABILIDAD\\Proyecto_Proba\\img\\logo-fi.gif")
    icon = PhotoImage(file="C:\\Users\\lossi\\Dropbox\\Escuela\\Facultad de Ingenieria\\3er Semestre\\PROBABILIDAD\\Proyecto_Proba\\img\\icon.gif")

    menu = Menu(master, bg="darkgray", activebackground="silver")
    distribution_menu = Menu(menu, tearoff=0, bg="darkgray", activebackground="silver")
    tools_menu = Menu(menu, tearoff=0, bg="darkgray", activebackground="silver")
    
    master_frame = Frame(master, bg="white", width=350, height=450)

    tools_elements = None

    pic_label = Label(master_frame, image=fi_logo)
    curr_view = pic_label

    bernoulli_view = Bernoulli_View.BernoulliView(master_frame)
    binomial_view = BinomialView(master_frame)
    neg_binomial_view = NegativeBinomialView(master_frame)
    geometric_view = GeometricView(master_frame)
    discrete_view = DiscreteView(master_frame)

    HELP_FILE = "C:\\Users\\lossi\\Desktop\\Proyecto_Proba\\RES\\doc.pdf"



    tools_methods = [util.Util.raise_not_defined, util.Util.raise_not_defined, util.Util.raise_not_defined]

    # distribution_labels = [u"Binomial", u"Binomial Negativa", u"Bernoulli", u"Geométrica", u"Unitaria"]
    # distribution_methods = []

    def __init__(self):
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.icon)

        self.draw_menu()
        self.draw_window()

        self.master.mainloop()

    def draw_window(self):
        self.master_frame.pack()
        self.pic_label.pack()

        self.curr_view = self.pic_label

    def draw_menu(self):
        self.master.config(menu=self.menu)
        self.menu.add_cascade(label=u"Seleccionar Distribución", menu=self.distribution_menu)
        self.menu.add_separator()
        self.menu.add_cascade(label=u"Herramientas", menu=self.tools_menu)
        self.draw_distribution_menu(None, None)
        self.draw_tools_menu()

    def draw_distribution_menu(self, distribution_label_list, distribution_methods_list):
        self.distribution_menu.add_command(label=u"Binomial",
                                           command=lambda: self.refresh_view(self.curr_view,
                                                                     self.binomial_view)
                                           )

        self.distribution_menu.add_command(label=u"Binomial Negativa",
                                           command=lambda: self.refresh_view(self.curr_view,
                                                                             self.neg_binomial_view)
                                           )

        self.distribution_menu.add_separator()
        self.distribution_menu.add_command(label=u"Bernoulli",
                                           command=lambda: self.refresh_view(self.curr_view,
                                                                             self.bernoulli_view)
                                           )
        self.distribution_menu.add_command(label=u"Geométrica",
                                           command=lambda: self.refresh_view(self.curr_view,
                                                                             self.geometric_view)
                                           )
        self.distribution_menu.add_separator()
        self.distribution_menu.add_command(label=u"Uniforme",
                                           command=lambda: self.refresh_view(self.curr_view,
                                                                             self.discrete_view)
                                           )

    def draw_tools_menu(self):

        tools_elements = [
            [u"Información", lambda: InfoView(self.master)],
            [u"Licencia", lambda: License(self.master)],
            [u"Ayuda", lambda: self.show_pdf()]
        ]

        self.tools_elements = tools_elements

        for string, method in tools_elements:
            self.tools_menu.add_command(label=string, command=method)

    def set_current_view(self, view):
        self.curr_view = view

    def refresh_view(self, view, new_view):
        print("Refreshing...")
        print("Current view: ", self.curr_view)

        if isinstance(view, Distribution_View.DistributionView):
            view.clear()
        else:
            view.pack_forget()

        self.set_current_view(new_view)
        print("Current view: ", self.curr_view)
        self.curr_view.draw()

    def show_pdf(self):
        subprocess.Popen([self.HELP_FILE], shell=True)

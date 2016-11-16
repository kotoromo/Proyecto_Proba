# -*- coding: utf-8 -*-

from Tkinter import *
from Utilities import util
from Views import Bernoulli_View
from Views.Binomial_View import BinomialView
from Views.NegativeBinomial_View import NegativeBinomialView
from Views.Geometric_View import GeometricView
from Views import Distribution_View


class View:
    master = Tk()
    master.resizable(width=False, height=False)
    master.minsize(width=350, height=450)
    fi_logo = PhotoImage(file="img/logo-fi.gif")
    icon = PhotoImage(file="img/icon.gif")

    menu = Menu(master, bg="darkgray", activebackground="silver")
    distribution_menu = Menu(menu, tearoff=0, bg="darkgray", activebackground="silver")
    tools_menu = Menu(menu, tearoff=0, bg="darkgray", activebackground="silver")
    
    master_frame = Frame(master, bg="white", width=350, height=450)

    pic_label = Label(master_frame, image=fi_logo)
    curr_view = pic_label

    bernoulli_view = Bernoulli_View.BernoulliView(master_frame)
    binomial_view = BinomialView(master_frame)
    neg_binomial_view = NegativeBinomialView(master_frame)
    geometric_view = GeometricView(master_frame)

    tools_elements = [
        [u"Información", util.Util.raise_not_defined],
        [u"Licenica", util.Util.raise_not_defined],
        [u"Ayuda", util.Util.raise_not_defined]
    ]

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
        self.draw_tools_menu(self.tools_elements)

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
        self.distribution_menu.add_command(label=u"Uniforme")

    def draw_tools_menu(self, elements):
        for string, method in elements:
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

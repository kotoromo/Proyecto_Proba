# -*- coding: utf-8 -*-
from Tkinter import *


class InfoView:

    def __init__(self, master):
        top = Toplevel(master)
        top.title(u"Información")

        labelframe = LabelFrame(top, text=u"Autor y Programador:")
        label_1 = Label(labelframe, text=u"Nicky García Fierros"+'\n'
                                         +u"nick.garc.96@gmail.com \n https://github.com/kotoromo")
        labelframe_2 = LabelFrame(top, text=u"Programado Para:")
        label_2 = Label(master=labelframe_2, text=u"Facultad de Ingeniería, Universidad Autónoma de México")

        labelframe_3 = LabelFrame(top, text=u"Última Compilación:")
        label_3 = Label(master=labelframe_3, text=u"16/11/2016 9:03 hrs")

        labelframe.pack(fill="both", expand="yes")
        label_1.pack()
        labelframe_2.pack(fill="both", expand="yes")
        label_2.pack()
        labelframe_3.pack(fill="both", expand="yes")
        label_3.pack()
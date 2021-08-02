#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gilles_VERONIE
#
# Created:     03/01/2020
# Copyright:   (c) Gilles_VERONIE 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
from tkinter import *

class EnterMessage(Frame):
    """ Classe EnterMessage (Frame de saisie du message)
    Cette classe dérive de la classe Tkinter.Frame"""
    def __init__(self, master=None):
        """Initialisation : création d'un widget Frame"""
        Frame.__init__(self, master, bg='navy')
        self.pack(padx=10, pady=10)
        self.CreateWidgets()

    def CreateWidgets(self):
        """ Création des widgets Entry et Button dans le widget Frame """
        self.NouveauMessage = StringVar()
        Entry(master=self, textvariable=self.NouveauMessage).pack(side=LEFT, padx=10, pady=10)
        Button(master=self, text="Nouveau", fg="navy", command=self.Nouveau).pack(padx=10, pady=10)

    def Nouveau(self):
        """ Création d'une instance de la classe NewPostIt """
        if self.NouveauMessage.get() != "":
            NewPostIt(master=self.master, message=self.NouveauMessage.get())
            self.NouveauMessage.set("")


class NewPostIt(Frame):
    """ Classe post-it (Frame Post-It)
    Cette classe dérive de la classe Tkinter.Frame"""
    def __init__(self, master=None, message=None):
        """Initialisation : création d'un widget Frame"""
        Frame.__init__(self, master, bg="grey")
        self.pack(side=LEFT, padx=10, pady=10)
        self.CreateWidgets(message)

    def CreateWidgets(self, message):
        """ Création des widgets Label et Button dans le widget Frame"""
        Label(master=self, text=message, fg='maroon', bg='white').pack(padx=10, pady=10)
        Button(master=self, text="Effacer", fg="navy", command=self.destroy).pack(padx=10, pady=10)


if __name__ == '__main__':
    # création de la fenêtre principale
    Mafenetre = Tk()
    Mafenetre.title('Post-it')
    Mafenetre['bg'] = 'blue'

    # Création d'une instance de la classe EnterMessage
    EnterMessage(master=Mafenetre)

    Mafenetre.mainloop()
#-------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      Administrator
#
# Created:     08/06/2021
# Copyright:   (c) Administrator 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -- coding: utf-8 --
from tkinter import *

##
##class CreerButton(Button):
##    """Classe CreerButton(Button du clavier)"""
##
##    def init(self, master=None):
##        """Initialisation : création d'un widget Button"""
####        Button.init(self, master, text='Bouton', bg="black")
####        self.pack(padx=10, pady=10)
##        pass
##
##    def CreateWidgets(self):
##        """ Création des widgets Entry et Button dans le widget Frame """
##        self.NouveauMessage = StringVar()
##        Entry(master=self, textvariable=self.NouveauMessage).pack(side=LEFT, padx=10, pady=10)
##        Button(master=self, text="Nouveau", fg="navy", command=self.Nouveau).pack(padx=10, pady=10)
##
##
##root = Tk()
##a = CreerButton(master=root)


def calcul():
    t = Label(root, text='test')
    t.place()

root = Tk()
root.geometry("618x360")

listAzerty = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]

for i in listAzerty:
    for j in range(10):
        i = Button(root, text=i, bg="blue", command=calcul)
        i.pack(side=LEFT, padx=10, pady=10)
root.mainloop()




def main():
    pass

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------
# Name:        Jeu Pendu
# Purpose:
#
# Author:      1,2,3,4,5
#
# Created:     01/06/2021
# Copyright:   Greta Classe Python
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import random


### Classe couleur
##class Couleur:
##    """Stocker les couleurs"""
##    def __init__(self):
##        self.fen_bg = "#FF8D34"
##        self.title1 = "#FFEC35"
##        self.title2 = "#FFFFFF"
##        self.tex = "#FFFFFF"
##        self.bou = "#FFFFFF"
##
### Classe font
##class Font:
##    """stocker les polices de caractères"""
##    def __init__(self):
##        self.title1 = Font(family="Bauhaus 93", size='40', weight="bold")
##        self.title2 = Font(family="Berlin Sans FB Demi", size='30', weight="bold")
##        self.tex = Font(family="Berlin Sans FB Demi", size='15', weight="bold")
##        self.bou = Font(family="Berlin Sans FB Demi", size='15', weight="bold")
##
### Intanciation des classe Couleur et Fonts
##couleur = Couleur()
##font = Font ()

# Varibales couleurs
couleur_bg = "#FF8D34"
couleur_titre = "#FFEC35"
couleur_text = "#FFFFFF"
couleur_bouton = "#D67CE3"
couleur_bouton_text = "#FFFFFF"

# Variables polices de caractères
##fontTitre1 = '("Bauhaus 93", 40, "bold")'
##fontTitre2 = '("Berlin Sans FB Demi", 30, "bold")'
##fontText = '("Berlin Sans FB Demi", 15, "bold")'

# Création de la fenêtre du jeu
fen = Tk()
fen.title = "Jeu Pendu"
fen.geometry("900x600")
fen.config(bg ="#FF8D34")
fen.resizable(width=False, height=False)

#écran 1
def ecran1():
    # Création des 3 frames dans écran 1
    fra_1 = Frame(fen, width=900, height=229, bg="black")
    fra_2 = Frame(fen, width=900, height=229, bg="white")
    fra_3 = Frame(fen, width=900, height=142, bg="red")
##
##    fra_1.pack()
##    fra_2.pack()
##    fra_3.pack()

    fra_1.grid()
    fra_1.grid_rowconfigure(1, weight=1)
    fra_1.grid_columnconfigure(1, weight=1)
    fra_2.grid()
    fra_3.grid()


    # widget dans frame 1
    fra_1_1 = Frame(fra_1, width=900, height=229)

    titre_jeu = Label(fra_1_1, text='Bienvenue \n sur le jeu du pendu !', font=("Bauhaus 93", 40, "bold"), bg=couleur_bg, fg=couleur_titre)
    titre_jeu.pack()


    fra_1_1.place(x=0, y=0)
##    fra_1_1.grid_rowconfigure(1, weight=1)
##    fra_1_1.grid_columnconfigure(1, weight=1)


    # widget dans frame 2
    fra_2_1 = Frame(fra_2, width=900, height=229)

    titre_reg = Label(fra_2_1, text='Règles du jeu', font=("Berlin Sans FB Demi", 30, "bold"), bg= couleur_bg, fg=couleur_text)
    relge_1= Label(fra_2_1, text='* Le but du jeu consiste à deviner toutes les lettres', font=("Berlin Sans FB Demi", 15, "bold"), bg= couleur_bg, fg=couleur_text)
    regle_2=Label(fra_2_1, text ='* Vous pouvez choisir la thématique de votre choix *', font=("Berlin Sans FB Demi", 15, "bold"), bg= couleur_bg, fg=couleur_text)
    regle_3= Label(fra_2_1, text='* A chaque fois que vous devinez une lettre*',font=("Berlin Sans FB Demi", 15, "bold"), bg= couleur_bg, fg=couleur_text)

    relge_1.pack()
    regle_2.pack()
    regle_3.pack()


    fra_2_1.place(x=0, y=0)
##    fra_2_1.grid_rowconfigure(1, weight=1)
##    fra_2_1.grid_columnconfigure(1, weight=1)


def main():
    ecran1()
    fen.mainloop()

if __name__ == '__main__':
    main()

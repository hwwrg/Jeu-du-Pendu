#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tf
#
# Created:     25/05/2021
# Copyright:   (c) tf 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from easygui import *
from PIL import *

fen_4 = Tk()
fen_4.geometry("1200x400")

def restart():
    pass

mot_ran = None
mot_sai = None

def aff_res():
    if mot_sai == mot_ran:
        resultat = Label(fen_4, text = "Vous avez gagné!")
        img = PhotoImage(file="bravo.png")
        imglabel = Label(fen_4, image=img)

        resultat.grid(row=1, column=0)
        imglabel.grid(row=1, column=1)
    else:
        resultat = Label(fen_4, text = "Vous avez perdu!")
        img = PhotoImage(file="sorry.png")
        imglabel = Label(fen_4, image=img)

        resultat.grid(row=1, column=0)
        imglabel.grid(row=1, column=1)


def main():
    global mot_ran



    bon_mot = Label(fen_4, text="Le bon mot est : ")
    mot_res = Label(fen_4, text="Test, doit lié mot_ran")

    bou_reserve = Button(fen_4, text="Résultat, bouton réservé", command=aff_res)
    recom = Button(fen_4, text="Recommencer", command=restart)

    #columnspan --> regrouper case en row

    bon_mot.grid(row=0, column=0)
    mot_res.grid(row=0, column=1)
    bou_reserve.grid(row=2, column=0)
    recom.grid(row=2, column=1)


    fen_4.mainloop()

if __name__ == '__main__':
    main()

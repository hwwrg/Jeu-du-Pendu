#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tf
#
# Created:     09/06/2021
# Copyright:   (c) tf 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.font as tkFont

# Classe couleur
class Couleur:
    """Stocker les couleurs"""
    def __init__(self):
        self.fen_bg = "#FF8D34"
        self.title1 = "#FFEC35"
        self.title2 = "#FFFFFF"     #White
        self.title3 = "#FFFFFF"
        self.tex = "#FFFFFF"        #White
        self.bou_bg = "#728C00"     #Venom Green
        self.bou_fg = "#3BB9FF"     #Deep Sky Blue
        self.lettre = "#3BB9FF"

class Font:
    """stocker les polices de caractères"""
    def __init__(self):
        self.title1 = tkFont.Font(family="Bauhaus 93", size='60', weight="bold")
        self.title2 = tkFont.Font(family="Berlin Sans FB Demi", size='45', weight="bold")
        self.title3 = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.tex = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.bou = tkFont.Font(family="Berlin Sans FB Demi", size='40', weight="bold")
        self.bou2 = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.lettre = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")



root = Tk()
root.geometry("618x360")

# Intanciation des classe Couleur
couleur = Couleur()
font = Font()


def appuyerBouton(index, valeurBouton):

##    print(buttons_Liste[index])
    print(valeurBouton)
##    buttons_Liste[index].destroy()
    buttons_Liste[index].config(state="disabled", relief='sunken')

# liste Azerty
listAzerty = ["A","Z","E","R","T","Y","U","I","O","P",
" ","Q","S","D","F","G","H","J","K","L","M"," "," ","W","X","C","V","B","N"]

# Supprimer espace dans la listAzerty
list_Tmp = []
for i in listAzerty:
    if i != " ":
        list_Tmp.append(i)
    listAzerty = list_Tmp

# Création 3 frames du clavier
ligne1_Lettre = Frame(root)
ligne1_Lettre.place(x=9, y=40)

ligne2_Lettre = Frame(root)
ligne2_Lettre.place(x=9, y=140)

ligne3_Lettre = Frame(root)
ligne3_Lettre.place(x=120, y=240)

# Création boutons des lettre
buttons_Liste = []
# ligne 1
for i in range(10):
    lettre_Bouton = Button(ligne1_Lettre, text=listAzerty[i], fg=couleur.lettre,
                        font=font.lettre, width=2, borderwidth=4,
                        command=lambda index=i, valeurBouton=listAzerty[i]:appuyerBouton(index, valeurBouton))
    lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
    buttons_Liste.append(lettre_Bouton)

# ligne 2
for i in range(10):
    lettre_Bouton = Button(ligne2_Lettre, text=listAzerty[10+i], fg=couleur.lettre,
                        font=font.lettre, width=2, borderwidth=4,
                        command=lambda index =(10+i), valeurBouton=listAzerty[10+i]:appuyerBouton(index, valeurBouton))
    lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
    buttons_Liste.append(lettre_Bouton)
# ligne 3
for i in range(6):
    lettre_Bouton = Button(ligne3_Lettre, text=listAzerty[20+i], fg=couleur.lettre,
                        font=font.lettre, width=2, borderwidth=4,
                        command=lambda index =(20+i),  valeurBouton=listAzerty[20+i]:appuyerBouton(index, valeurBouton))
    lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
    buttons_Liste.append(lettre_Bouton)
print(buttons_Liste)



root.mainloop()

def main():
    pass

if __name__ == '__main__':
    main()

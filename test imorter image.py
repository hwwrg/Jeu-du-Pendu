from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import random





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

# Création de la fenêtre du jeu
fen = Tk()
fen.title("Jeu Pendu")
fen.geometry("1000x600")
fen.resizable(width=False, height=False)

# Intanciation des classe Couleur
couleur = Couleur()
font = Font()

fen.config(bg =couleur.fen_bg)



def ecran1():
    global fra_1
    global fra_2
    global fra_3
    global fra_4

    # Création des 3 frames dans écran 1
    fra_1 = Frame(fen, width=1000, height=229, bg=couleur.fen_bg)
    fra_2 = Frame(fen, width=1000, height=229, bg=couleur.fen_bg)
    fra_3 = Frame(fen, width=1000, height=50, bg=couleur.fen_bg)
    fra_4 = Frame(fen, width=1000, height=141, bg=couleur.fen_bg)

##    fra_1.pack()
##    fra_2.pack()
##    fra_3.pack()
##    fra_4.pack()

    fra_1.grid()
    fra_2.grid()
    fra_3.grid()
    fra_4.grid()


    # frame 1
    titre_jeu = Label(
    fra_1, text='Bienvenue \n sur le jeu du pendu !',
    height=3,
    font=font.title1,
    bg=couleur.fen_bg, fg=couleur.title1)
    titre_jeu.grid(ipady=15)


    # frame 2
    titre_reg = Label(fra_2, text='Règles du jeu', font=font.title2, bg=couleur.fen_bg, fg=couleur.tex)
    relge_1= Label(fra_2, text='* Le but du jeu consiste à deviner toutes les lettres', font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)
    regle_2=Label(fra_2, text ='* Vous pouvez choisir la thématique de votre choix *', font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)
    regle_3= Label(fra_2, text='* A chaque fois que vous devinez une lettre*',font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)

    titre_reg.pack()
    relge_1.pack()
    regle_2.pack()
    regle_3.pack()


    # Frame 4
    bou_commencer = Button(fra_4, text="Commmencer", height=1, font=font.bou, bg=couleur.bou_bg, fg=couleur.bou_fg, command=ecran2)
    bou_commencer.pack()


# Ecran2
# Fonctions de Ecran2
def tirageThemeFruLeg():
    global mot_Tir
    global theme_Tir

    # Tirage du mot : avec choices
    nom_Theme_Tir = "Fruits et légumes"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Tir = random.choices(theme_Tir)         # retourne type : liste
    mot_Tir = mot_Tir[0].upper()
    # Ecran 3
    ecran3()

def tirageThemeEtats():
    global mot_Tir
    global theme_Tir

    # Tirage du mot
    nom_Theme_Tir = "Etats USA"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Choices = random.choices(theme_Tir)
    mot_Tir = mot_Choices[0].upper()
    # Ecran 3
    ecran3()


def tirageThemeMarVoi():
    global mot_Tir
    global theme_Tir

    # Tirage du mot
    nom_Theme_Tir = "Marques Auto"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Choices = random.choices(theme_Tir)
    mot_Tir = mot_Choices[0].upper()
    # Ecran 3
    ecran3()

def tirageThemeAni():
    global mot_Tir
    global theme_Tir

    # Tirage du mot
    nom_Theme_Tir = "Animaux"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Choices = random.choices(theme_Tir)
    mot_Tir = mot_Choices[0].upper()
    # Ecran 3
    ecran3()

# Interface Ecran2
def ecran2():

    global fra_5
    global fra_6
    global fra_7

    global img_Button_Astro
    global img_Button_FruLeg
    global img_Button_Etats
    global img_Button_MarVoi
    global img_Button_Ani


    fra_1.grid_forget()
    fra_2.grid_forget()
    fra_3.grid_forget()
    fra_4.grid_forget()

    img_Open =Image.open("animaux-test.png")
    img_Ani = ImageTk.PhotoImage(img_Open)

    test = Label(fen, text="Why So Serious?")
    test.pack()



    #Création 2 frames
    fra_5 = Frame(fen, width=1000, height=119, bg=couleur.fen_bg)
    fra_6 = Frame(fen, width=1000, height=10, bg=couleur.fen_bg)
    fra_7 = Frame(fen, width=1000, height=471, bg=couleur.fen_bg)

    fra_5.pack()
    fra_6.pack()
    fra_7.pack()

    # Frame 5
    titre_choixTheme = Label(fra_5, text='Choisissez Un Thème', font=font.title2, bg=couleur.fen_bg, fg=couleur.title2)
    titre_choixTheme.pack(pady=20)

    # Frame 6 : réserver l'espace

    # Frame 7 : 5 Boutons des thèmes

    img_Astro = PhotoImage(file="bravo.png")
    img_FruLeg = PhotoImage(file="bravo.png")
    img_Etats = PhotoImage(file="bravo.png")
    img_MarVoi = PhotoImage(file="bravo.png")
    img_Ani = PhotoImage(file="animaux-test.png")

    img_Button_Astro = Button(fra_7, image=img_Astro)
    img_Button_FruLeg = Button(fra_7, image=img_FruLeg)
    img_Button_Etats = Button(fra_7, image=img_Etats)
    img_Button_MarVoi = Button(fra_7, image=img_MarVoi)
    img_Button_Ani = Label(fra_7, image=img_Ani)

    img_Button_Astro = Button(fra_7, text="Astronomie", width=20, height=3, command=tirageThemeAstro)
    img_Button_FruLeg = Button(fra_7, text="Fruits & Légumes", width=20, height=3, command=tirageThemeFruLeg)
    img_Button_Etats = Button(fra_7, text="Les Etats des USA", width=20, height=3, command=tirageThemeEtats)
    img_Button_MarVoi = Button(fra_7, text="Marques de voiture", width=20, height=3, command=tirageThemeMarVoi)
    img_Button_Ani = Button(fra_7, text="Animaux", width=20, height=3, command=tirageThemeAni)

    img_Button_Astro.place(x=150, y=100)
    img_Button_FruLeg.place(x=600, y=100)
    img_Button_Etats.place(x=400, y=200)
    img_Button_MarVoi.place(x=250, y=350)
    img_Button_Ani.place(x=550, y=350)

##

def main():
##
##    ecran1()
##    fen.mainloop()
##
##    fen = Tk()
##    fra_7 = Frame(fen, width=1000, height=471)
##    fra_7.pack()
##
##    img_Open =Image.open("animaux-test.png")
##    img_Ani = ImageTk.PhotoImage(img_Open)
##
####    img_Ani = PhotoImage(file="animaux-test.png")
##
##    img_Button_Ani = Button(fra_7, image=img_Ani)
##    img_Button_Ani.pack()

    fen.mainloop()


if __name__ == '__main__':
    main()

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
        self.bou_bg = "#E5E4E2"     #Platinum
        self.bou_fg = "#C11B17"     #Chilli Pepper
        self.lettre = "#C11B17"     #Chilli Pepper

class Font:
    """stocker les polices de caractères"""
    def __init__(self):
        self.title1 = tkFont.Font(family="Bauhaus 93", size='60', weight="bold")
        self.title2 = tkFont.Font(family="Berlin Sans FB Demi", size='45', weight="bold")
        self.title3 = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.tex = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.tex2 = tkFont.Font(family="Berlin Sans FB Demi", size='30', weight="bold")
        self.bou = tkFont.Font(family="Berlin Sans FB Demi", size='40', weight="bold")
        self.bou2 = tkFont.Font(family="Berlin Sans FB Demi", size='20', weight="bold")
        self.lettre = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.labelframe = tkFont.Font(family="Berlin Sans FB Demi", size='18', weight="bold")
        self.tiret = tkFont.Font(family="Berlin Sans FB", size='30')


# Création de la fenêtre du jeu
fen = Tk()
fen.title("Jeu Pendu")
fen.geometry("1000x600")
fen.resizable(width=False, height=False)

# Intanciation des classe Couleur
couleur = Couleur()
font = Font()

fen.config(bg =couleur.fen_bg)


# Ecran 1
# Construire Ecran2
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

    fra_1.grid()
    fra_2.grid()
    fra_3.grid()
    fra_4.grid()


    # Frame 1
    titre_jeu = Label(
    fra_1, text='Bienvenue \n sur le jeu du pendu !',
    font=font.title1,
    bg=couleur.fen_bg, fg=couleur.title1)
    titre_jeu.grid(ipady=15)


    # Frame 2

    titre_reg = Label(fra_2, text='Règles du jeu', font=font.title2, bg=couleur.fen_bg, fg=couleur.tex)
    relge_1= Label(fra_2, text='* Le but du jeu consiste à deviner toutes les lettres', font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)
    regle_2=Label(fra_2, text =' Vous pouvez choisir la thématique de votre choix ', font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)
    regle_3= Label(fra_2, text=' Vous avez 9 essais *',font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)

    titre_reg.pack()
    relge_1.pack()
    regle_2.pack()
    regle_3.pack()


    # Frame 4
    bou_commencer = Button(fra_4, text="Commmencer", height=1, font=font.bou, bg=couleur.bou_bg, fg=couleur.bou_fg, command=ecran2)
    bou_commencer.pack()


# Ecran2
# Fonctions de Ecran2
def tirageThemeAstro():
    global mot_Tir
    global theme_Tir
    global nom_Theme_Tir

    # Tirage du mot : avec randint
    nom_Theme_Tir = "Astronomie"
    theme_Tir = dico[nom_Theme_Tir]
    num_ordre_mot = random.randint(0, len(theme_Tir)-1)
    mot_Tir = theme_Tir[num_ordre_mot]          # retourne type : str
    mot_Tir = mot_Tir.upper()
    # Ecran 3
    ecran3()

def tirageThemeFruLeg():
    global mot_Tir
    global theme_Tir
    global nom_Theme_Tir

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
    global nom_Theme_Tir

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
    global nom_Theme_Tir

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
    global nom_Theme_Tir

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

    #Création 2 frames
    fra_5 = Frame(fen, width=1000, height=119, bg=couleur.fen_bg)
    fra_6 = Frame(fen, width=1000, height=1, bg=couleur.fen_bg)
    fra_7 = Frame(fen, width=1000, height=471, bg=couleur.fen_bg)

    fra_5.pack()
    fra_6.pack()
    fra_7.pack()


    # Frame 5
    titre_choixTheme = Label(fra_5, text='Choisissez Un Thème', font=font.title2, bg=couleur.fen_bg, fg=couleur.title2)
    titre_choixTheme.pack(pady=20)

    # Frame 6 : réserver l'espace

    # Frame 7 : 5 Boutons des thèmes
    img_Astro = PhotoImage(file="astro.png")
    img_FruLeg = PhotoImage(file="fruitlegume.png")
    img_Etats = PhotoImage(file="etatsusa.png")
    img_MarVoi = PhotoImage(file="marquevoiture.png")
    img_Ani = PhotoImage(file="animaux.png")

    img_Button_Astro = Button(fra_7, text="Astronomie", image=img_Astro, command=tirageThemeAstro)
    img_Button_FruLeg = Button(fra_7, text="Fruits & Légumes", image=img_FruLeg, command=tirageThemeFruLeg)
    img_Button_Etats = Button(fra_7, text="Les Etats des USA", image=img_Etats, command=tirageThemeEtats)
    img_Button_MarVoi = Button(fra_7, text="Marques de voiture", image=img_MarVoi, command=tirageThemeMarVoi)
    img_Button_Ani = Button(fra_7, text="Animaux", image=img_Ani, command=tirageThemeAni)

    img_Button_Astro.place(x=80, y=20)
    img_Button_Astro.image = img_Astro
    img_Button_FruLeg.place(x=650, y=10)
    img_Button_FruLeg.image = img_FruLeg
    img_Button_Ani.place(x=390, y=105)
    img_Button_Ani.image = img_Ani
    img_Button_MarVoi.place(x=120, y=250)
    img_Button_MarVoi.image = img_MarVoi
    img_Button_Etats.place(x=690, y=240)
    img_Button_Etats.image = img_Etats



# Ecran 3
# Fonction de Eran 3

def renouStrAffi():
    global tiret_Label

    tiret_Label.destroy()

    str_Affi = ""
    for i in list_Essaies:
        if i =="*":
            str_Affi += "__"
        else:
            str_Affi += i + " "
        str_Affi += " "
    print(str_Affi)
    tiret_Label = Label(fra_9_tiret, text=str_Affi, font=font.tiret, bg=couleur.fen_bg)
    tiret_Label.place(x=50, y=30)

def deplaceBouton(valeurBouton):

# Afficher la bouton appuyer
    lettre_Incorrecte = Button(fra_10_lettres, text=valeurBouton, fg=couleur.lettre,
                font=font.lettre, width=2, borderwidth=4)
    lettre_Incorrecte.pack(side=LEFT, padx=4, pady=10)
    lettre_Incorrecte.config(state="disabled")


def hangman(compteur):
    global hg_Label

    """Incrémentation de l'image du pendu par essaie non concluant du joueur"""
    dico_Hg = {0:"hg0.png", 1:"hg1.png", 2:"hg2.png", 3:"hg3.png",4:"hg4.png",
    5:"hg5.png", 6:"hg6.png", 7:"hg7.png", 8:"hg8.png", 9:"hg9.png"}

    # Création d'un label pour y afficher l'image
    hg_Label.pack_forget()
    hangman_Image = PhotoImage(file=dico_Hg[compteur])

    # Appeler, redimensionner l'image et la mettre dans le tableau
    hg_Label =Label(fra_8_bonhomme, image=hangman_Image, borderwidth=0, highlightthickness=0)
    hg_Label.pack()
    hg_Label.image=hangman_Image


def gagne(compteur, list_BonResultat, list_Essaies):
    global gile_Label
    global fra_8_bonhomme

    if list_BonResultat == list_Essaies:
        ecran4()
        img_Bravo = PhotoImage(file='bravo.png')
        resultat_Image_Bravo = Label(fra_14, image=img_Bravo, borderwidth=0, highlightthickness=0)
        resultat_Image_Bravo.place(x=34, y=1)
        resultat_Image_Bravo.image=img_Bravo

        fra_8_bonhomme.destroy()
        fra_8_bonhomme = Frame(fen, width=382, height=600, bg='blue')
        fra_8_bonhomme.place(x=0, y=0)

##        img_Gile = PhotoImage(file='gile.png')
        img_Gile = PhotoImage(file='gile1.png')
        gile_Label = Label(fra_8_bonhomme, image=img_Gile, borderwidth=0, highlightthickness=0)
        gile_Label.pack()
        gile_Label.image=img_Gile


    elif (compteur !=0) and (compteur % 9 == 0):        # 0 % int = 0
        print("perdu")
        ecran4()
        img_Perdu = PhotoImage(file='perdu.png')
        resultat_Image_Perdu = Label(fra_14, image=img_Perdu, borderwidth=0, highlightthickness=0)
        resultat_Image_Perdu.place(x=34, y=1)
        resultat_Image_Perdu.image=img_Bravo
    else:
        pass



# numbre d'essaie incorrecte
compteur = 0

def appuyerBouton(index, valeurBouton):

    global list_BonResultat
    global list_Essaies
    global str_Affi
    global compteur

    print(valeurBouton)


    # Disparaître le bouton usé
    buttons_Liste[index].destroy()
    # Déactiver le bouton lettre
##    buttons_Liste[index].config(state="disabled", relief='sunken')

    # Boucle permettant d'afficher les lettres devinées correctes
    # à la place des tirets, sinon afficher le pendu et déplace la lettre
    if valeurBouton in list_BonResultat:                                # débuger 'else'
        for i in range(0, len(list_BonResultat)):
            if list_BonResultat[i] == valeurBouton :
                list_Essaies[i] = valeurBouton
                renouStrAffi()
    else :
        print("incorrecte")
        deplaceBouton(valeurBouton)
        compteur +=1


    # Afficher le graphique -le pendu
    print(compteur)
    hangman(compteur)
    gagne(compteur, list_BonResultat, list_Essaies)



# Interface Ecran 3
def ecran3():
    global fra_8_bonhomme
    global fra_9_tiret
    global fra_10_lettres
    global fra_11_clavier

    global str_Affi

    global list_BonResultat
    global list_Essaies

    global tiret_Label

    global buttons_Liste

    global hangman_Image
    global hg_Label

    fra_5.pack_forget()
    fra_6.pack_forget()
    fra_7.pack_forget()


    # Création des 4 frames
    fra_8_bonhomme = Frame(fen, width=382, height=600, bg='blue')
    fra_9_tiret = LabelFrame(fen, width=610, height=120, bg=couleur.fen_bg, text=nom_Theme_Tir.upper(), borderwidth=5, font = font.labelframe)
    fra_10_lettres = Frame(fen, width=618, height=120, bg=couleur.fen_bg)
    fra_11_clavier = Frame(fen, width=618, height=360, bg=couleur.fen_bg)

    fra_8_bonhomme.place(x=0, y=0)
    fra_9_tiret.place(x=382, y=25)
    fra_10_lettres.place(x=382, y=170)
    fra_11_clavier.place(x=382, y=250)


    # Frame 8 Bonhomme
    # Image Bonhomme
    hangman_Image = PhotoImage(file='hg0.png')
    hg_Label =Label(fra_8_bonhomme, image=hangman_Image, borderwidth=0, highlightthickness=0)
    hg_Label.pack()
    hg_Label.image=hangman_Image


    # Frame 9 Tiret

    # Lister qui contient les lettre du bon résultat
    list_BonResultat = []                 # liste bon résultat
    for i in mot_Tir:
        if i == "-" or i == " ":
            list_BonResultat.append("-")
        else:
            list_BonResultat.append(i)
    #(list_BonResultat)

    # String qui affiche le passage du jeu
    str_Affi = ""
    for i in list_BonResultat:
        if i=="-":
            str_Affi += i
        else:
            str_Affi += "__"
        str_Affi += "  "

    # Lister qui stocke les lettres essayées
    list_Essaies = []
    for i in list_BonResultat:
        if i=="-" or i==" ":
            list_Essaies.append("-")
        else:
            list_Essaies.append("*")


    tiret_Label = Label(fra_9_tiret, text=str_Affi, font=("Berlin Sans FB", 25), bg=couleur.fen_bg)
    tiret_Label.place(x=50, y= 30)


    # Frame 10 afficher les lettres essayées
    list_LettreEssayees = []


    # Frame 11 Clavier
    # Lister Azerty
    listAzerty = ["A","Z","E","R","T","Y","U","I","O","P",
                " ","Q","S","D","F","G","H","J","K","L","M",
                " "," ","W","X","C","V","B","N"]

    # Supprimer espace dans la listAzerty
    list_Tmp = []
    for i in listAzerty:
        if i != " ":
            list_Tmp.append(i)
        listAzerty = list_Tmp

    # Création 3 frames du clavier
    ligne1_Lettre = Frame(fra_11_clavier, bg=couleur.fen_bg)
    ligne1_Lettre.place(x=9, y=50)

    ligne2_Lettre = Frame(fra_11_clavier, bg=couleur.fen_bg)
    ligne2_Lettre.place(x=9, y=150)

    ligne3_Lettre = Frame(fra_11_clavier, bg=couleur.fen_bg)
    ligne3_Lettre.place(x=120, y=240)

    # Création boutons des lettre
    buttons_Liste = []
    # Ligne 1
    for i in range(10):
        lettre_Bouton = Button(ligne1_Lettre, text=listAzerty[i], fg=couleur.lettre,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda index=i, valeurBouton=listAzerty[i]:appuyerBouton(index, valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
        buttons_Liste.append(lettre_Bouton)

    # Ligne 2
    for i in range(10):
        lettre_Bouton = Button(ligne2_Lettre, text=listAzerty[10+i], fg=couleur.lettre,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda index =(10+i), valeurBouton=listAzerty[10+i]:appuyerBouton(index, valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
        buttons_Liste.append(lettre_Bouton)
    # Ligne 3
    for i in range(6):
        lettre_Bouton = Button(ligne3_Lettre, text=listAzerty[20+i], fg=couleur.lettre,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda index =(20+i),  valeurBouton=listAzerty[20+i]:appuyerBouton(index, valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
        buttons_Liste.append(lettre_Bouton)


# Eran 4
# Fonction nouveauMot()
def nouveauMot():
    global mot_Tir
    global compteur

    fra_13.destroy()
    fra_14.destroy()
##    fra_15.destroy()

    mot_Tir = random.choices(theme_Tir)
    mot_Tir = mot_Tir[0].upper()
    compteur = 0

    ecran3()

def changerTheme():
    global compteur

    fra_13.destroy()
    fra_14.destroy()
    fra_8_bonhomme.destroy()
##    fra_15.destroy()
    # Reinitialiser le compteur
    compteur = 0

    ecran2()


def ecran4():
    global fra_13
    global fra_14

    # Effacer les frame de l'éran 3
##    fra_8_bonhomme.destroy()
    fra_9_tiret.destroy()
    fra_10_lettres.destroy()
    fra_11_clavier.destroy()


    # Création 4 frames
##    fra_12 = Frame(fen, width=309, height=170, bg=couleur.fen_bg)     # supprimer
    fra_13 = Frame(fen, width=618, height=170, bg=couleur.fen_bg)
    fra_14 = Frame(fen, width=618, height=330, bg=couleur.fen_bg)
    fra_15 = Frame(fen, width=618, height=100, bg=couleur.fen_bg)

##    fra_12.place(x=382, y=0)
    fra_13.place(x=382, y=0)
    fra_14.place(x=382, y=170)
    fra_15.place(x=382, y=500)


    # Frame 12 : supprimer

    # Frame 13
    bon_Mot = "Le Bon Mot Est  :  " + mot_Tir
    bon_Mot_Label = Label(fra_13,
                        text=bon_Mot,
                        font=font.tex2,
                        fg=couleur.title2,
                        bg=couleur.fen_bg)
    bon_Mot_Label.place(x=30, y=50)


    # Frame 14
    # Voir fonction

    # Frame 15
    # 3 boutons
    nouveau_Mot_Bouton = Button(fra_15, text="Nouveau Mot", font=font.bou2, fg=couleur.bou_fg, command=nouveauMot)
    changer_Theme_Bouton = Button(fra_15, text="Changer Le Thème", font=font.bou2, fg=couleur.bou_fg, command=changerTheme)
    exit_Bouton = Button(fra_15, text = "Quitter", font=font.bou2, fg=couleur.bou_fg, command=fen.destroy)


    nouveau_Mot_Bouton.place(x=20, y=15)
    changer_Theme_Bouton.place(x=225, y=15)
    exit_Bouton.place(x=490, y=15)

def main():
    global dico

    # Création de la dictionnaires des mots des 5 thèmes
    dico = {}

    dico["Astronomie"] = ["Soleil","Terre","Mars","Jupiter","Saturne","Etoile","Lune","Astronaute","Copernic","Keppler",
    "Satellite" ,"Cosmos","Espace","Ciel","Nuage",
    "Astre","Galaxie","Eclipse", "Gravitation","Magnitude"]

    dico["Fruits et légumes"] = ["Banane","Kiwi","Pomme","Carotte","Oignon","Fraise","Navet","Concombre",
    "Pois","Avocat","Radis","Poire","Courgette","Tomate","Courge","Cornichon",
    "Mangue","Ananas","Poireau" ,"Abricot", "Cassis", "Cerise", "Figue", "Framboise", "Groseille",
    "Melon", "Mirabelle", "Mûre", "Myrtille", "Prune" , "Artichaut", "Aubergine",
    "Blette", "Brocolis", "Carotte"]

    dico["Etats USA"] = [ "Alabama", "Alaska","Arizona", "Arkansas", "Californie", "Colorado", "Connecticut", "Delaware", "Floride",
    "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "Nouveau-Mexique",
    "Hawai","New York", "Caroline du Nord", "Dakota du Nord", "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode-Island",
    "Caroline du Sud", "Dakota du Sud", "Tennessee", "Texas", "Utah", "Vermont", "Virginie" , "Washington",
    "Virginie occidentale", "Wisconsin" , "Wyoming" ]

    dico["Marques Auto"] = ["Lexus","Toyota","Porsche","Renault","Peugeot","Kia","Suzuki","Hyundai","Volskwagen","Audi","BMW" ,"Chevrolet","Nissan",
    "Mazda","Mercedes", "Volvo","Chrysler", "Jagua","Honda","Land Rover","Tesla" ,
    "Citroen","Fiat","Ferrari","Lamborghini","Seat","Skoda","Opel","Dacia"]

    dico["Animaux"] = ["Girafe", "Antilope", "Buffle", "Dromadaire", "Hippopotame", "Canard", "Ibis", "Spatule", "Aigrette",
    "Flamant" , "Gazelle", "Rat", "Cochon", "Hamster", "Souris",
    "Furet" , "Iguane", "Scorpion", "Perruche", "Perroquet", "Diamant", "Canaris", "Mainate", "Toucan", "Poule",
    "Dindon", "Paon", "Oie", "Canard"]

    # Enlever les mots qui contiennement plus que 12 lettres
    len_Max = 12
    for k in dico:
        list_tmp = []
        for m in dico[k]:
            if len(m) <= len_Max:
                list_tmp.append(m)
        dico[k] = list_tmp



    ecran1()
    fen.mainloop()

if __name__ == '__main__':
    main()
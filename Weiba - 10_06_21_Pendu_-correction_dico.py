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
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import easygui
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
fen.title = "Jeu Pendu"
fen.geometry("1000x600")
fen.resizable(width=False, height=False)

# Intanciation des classe Couleur
couleur = Couleur()
font = Font()

fen.config(bg =couleur.fen_bg)



# Ecran 1
# Contruire Ecran2
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
##    fra_1.grid_rowconfigure(1, weight=1)
##    fra_1.grid_columnconfigure(1, weight=1)


    # frame 1
    titre_jeu = Label(
    fra_1, text='Bienvenue \n sur le jeu du pendu !',
##    height=3,
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

# Ecran 2

##    img_Button_Astro = Button(fra_7, text="Astronomie", width=20, height=3, command=ecran3)
##    img_Button_FruLeg = Button(fra_7, text="Fruits & Légumes", width=20, height=3, command=ecran3)
##    img_Button_Etats = Button(fra_7, text="Les Etats des USA", width=20, height=3, command=ecran3)
##    img_Button_MarVoi = Button(fra_7, text="Marques de voiture", width=20, height=3, command=ecran3)
##    img_Button_Ani = Button(fra_7, text="Animaux", width=20, height=3, command=ecran3)



# Ecran2
# Fonctions de Ecran2
def tirageThemeAstro():
    global mot_Tir
    global theme_Tir

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

    #Création 2 frames
    fra_5 = Frame(fen, width=1000, height=119, bg=couleur.fen_bg)
    fra_6 = Frame(fen, width=1000, height=10, bg=couleur.fen_bg)
    fra_7 = Frame(fen, width=1000, height=471, bg=couleur.fen_bg)

    fra_5.pack()
    fra_6.pack()
    fra_7.pack()


    # Frame 5
    titre_choixTheme = Label(fra_5, text='Choisissez un Thème', font=font.title2, bg=couleur.fen_bg, fg=couleur.title2)
    titre_choixTheme.pack(pady=20)

    # Frame 6 : réserver l'espace

    # Frame 7 : 5 Boutons des thèmes

##    img_Astro = PhotoImage(file="bravo.png")
##    img_FruLeg = PhotoImage(file="bravo.png")
##    img_Etats = PhotoImage(file="bravo.png")
##    img_MarVoi = PhotoImage(file="bravo.png")
##    img_Ani = PhotoImage(file="bravo.png")
##
####img = PhotoImage(file="pendu.png")
####Button(root, text="Click me!", image=img, compound = LEFT).pack()
##
##    img_Button_Astro = Button(fra_7, image=img_Astro)
##    img_Button_FruLeg = Button(fra_7, image=img_FruLeg)
##    img_Button_Etats = Button(fra_7, image=img_Etats)
##    img_Button_MarVoi = Button(fra_7, image=img_MarVoi)
##    img_Button_Ani = Button(fra_7, image=img_Ani)

    img_Button_Astro = Button(fra_7, text="Astronomie", width=20, height=3, command=tirageThemeAstro)
    img_Button_FruLeg = Button(fra_7, text="Fruits & Légumes", width=20, height=3, command=tirageThemeFruLeg)
    img_Button_Etats = Button(fra_7, text="Les Etats des USA", width=20, height=3, command=tirageThemeEtats)
    img_Button_MarVoi = Button(fra_7, text="Marques de voiture", width=20, height=3, command=tirageThemeMarVoi)
    img_Button_Ani = Button(fra_7, text="Animaux", width=20, height=3, command=tirageThemeAni)


    img_Button_Astro.place(x=150, y=100)
    img_Button_FruLeg.place(x=600, y=100)
    img_Button_Etats.place(x=400, y=200)
    img_Button_MarVoi.place(x=250, y=350)
    img_Button_Ani.place(x=650, y=350)


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
            str_Affi += i
        str_Affi += " "
    print(str_Affi)
    tiret_Label = Label(fra_9_tiret, text=str_Affi, font=("Berlin Sans FB", 25), bg=couleur.fen_bg)
    tiret_Label.place(x=50, y= 50)


def deplaceBouton(valeurBouton):
# Afficher la bouton appuyer
##    lettre_Bouton.destroy()
    lettre_Incorrecte = Button(fra_10_lettres, text=valeurBouton, fg=couleur.lettre, bg=couleur.fen_bg,
                font=font.lettre, width=2, borderwidth=4)
    lettre_Incorrecte.pack(side=LEFT, padx=4, pady=10)


def gagne(compteur, list_BonResultat, list_Essaies):
    if list_BonResultat == list_Essaies:
        ecran4()
    elif (compteur !=0) and (compteur % 9 == 0):        # 0 % int = 0
        print("perdu")
        ecran4()
        resultat_Canvas = Label(fra_14, text="image Perdu", font=font.title1)
        resultat_Canvas.place(x=150, y=100)
    else:
        pass

# numbre d'essaie incorrecte
compteur = 0

def appuyerBouton(valeurBouton):

    global list_BonResultat
    global list_Essaies
    global str_Affi
    global compteur

    print(valeurBouton)

    # Boucle permettant d'afficher les lettres devinées correctes à la place des tirets, sinon afficher le pendu et déplace la lettre
    if valeurBouton in list_BonResultat:                                # débuger 'else'
        for i in range(0, len(list_BonResultat)):
            if list_BonResultat[i] == valeurBouton :
    ##            print("list_BonResultat[i]", list_BonResultat[i])
    ##            print("list_Essaies", list_Essaies)
                list_Essaies[i] = valeurBouton
    ##            print("list_Essaies", list_Essaies)
                renouStrAffi()
    else :
        print("incorrecte")
        deplaceBouton(valeurBouton)
        compteur +=1
##          afficher le graphique -le pendu


    print(compteur)
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

    fra_5.pack_forget()
    fra_6.pack_forget()
    fra_7.pack_forget()


    # Création des 4 frames
    fra_8_bonhomme = Frame(fen, width=382, height=600, bg='blue')
    fra_9_tiret = Frame(fen, width=618, height=120, bg=couleur.fen_bg)
    fra_10_lettres = Frame(fen, width=618, height=120, bg=couleur.fen_bg)
    fra_11_clavier = Frame(fen, width=618, height=360, bg=couleur.fen_bg)

    fra_8_bonhomme.place(x=0, y=0)
    fra_9_tiret.place(x=382, y=0)
    fra_10_lettres.place(x=382, y=120)
    fra_11_clavier.place(x=382, y=240)

##    fra_8_bonhomme.grid(row=0, column=0, columnspan=3)
##    fra_9_tiret.grid(row=0, column=1)
##    fra_10_lettres.grid(row=1, column=1)
##    fra_11_clavier.grid(row=2, column=1)



    # Frame 8 Bonhomme
    # Image Bonhomme
    """
    img_Bonhomme = PhotoImage(file="bravo.png")
    img_Canvas_Bonhomme = Canvas(fra_8_bonhomme, width=382, height=600)
    img_Canvas_Bonhomme.create_image(100, 100, image = img_Bonhomme)

    img_Canvas_Bonhomme.pack()
    ##    canvas1 = Canvas(frameimg,width=450, height=500, bg='#FFC2EE',bd=0,highlightthickness=0)
    ##    canvas1.create_image(250, 257, image=img)
    ##    canvas1.pack()
    """
    bonhomme = Label(fra_8_bonhomme, text="Je suis le bonhomme.", font=("Bauhaus 93", 20))
    bonhomme.place(x=50, y=300)


    # Frame 9 Tiret

    # liste qui contient les lettre du bon résultat
    list_BonResultat = []                 # liste bon résultat
    for i in mot_Tir:
        if i == "-" or i == " ":
            list_BonResultat.append("-")
        else:
            list_BonResultat.append(i)
    print(list_BonResultat)

    # String qui affiche le passage du jeu
    str_Affi = ""
    for i in list_BonResultat:
        if i=="-":
            str_Affi += i
        else:
            str_Affi += "__"
        str_Affi += "  "

    # Liste qui stocke les lettres essayées
    list_Essaies = []
    for i in list_BonResultat:
        if i=="-" or i==" ":
            list_Essaies.append("-")
        else:
            list_Essaies.append("*")

    # Solution '-' et ' ' non affichés
##    list_BonResultat = len(mot_Tir)
##    list_BonResultat = " __ "*len(mot_Tir)

    tiret_Label = Label(fra_9_tiret, text=str_Affi, font=("Berlin Sans FB", 25), bg=couleur.fen_bg)
    tiret_Label.place(x=50, y= 50)


    # Frame 10 afficher les lettres essayées
    list_LettreEssayees = []


    # Frame 11 Clavier
    # liste Azerty
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
    ligne1_Lettre.place(x=9, y=40)

    ligne2_Lettre = Frame(fra_11_clavier, bg=couleur.fen_bg)
    ligne2_Lettre.place(x=9, y=140)

    ligne3_Lettre = Frame(fra_11_clavier, bg=couleur.fen_bg)
    ligne3_Lettre.place(x=120, y=240)

    # Création boutons des lettre
    # ligne 1
    for i in range(10):
        lettre_Bouton = Button(ligne1_Lettre, text=listAzerty[i], fg=couleur.lettre, bg=couleur.fen_bg,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda valeurBouton=listAzerty[i]:appuyerBouton(valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
    # ligne 2
    for i in range(10):
        lettre_Bouton = Button(ligne2_Lettre, text=listAzerty[10+i], fg=couleur.lettre, bg=couleur.fen_bg,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda valeurBouton=listAzerty[10+i]:appuyerBouton(valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)
    # ligne 3
    for i in range(6):
        lettre_Bouton = Button(ligne3_Lettre, text=listAzerty[20+i], fg=couleur.lettre, bg=couleur.fen_bg,
                            font=font.lettre, width=2, borderwidth=4,
                            command=lambda valeurBouton=listAzerty[20+i]:appuyerBouton(valeurBouton))
        lettre_Bouton.pack(side=LEFT, padx=4, pady=10)


    next_gagne = Button(fra_11_clavier, text="Gagné", command=ecran4, font=("Bernard MT Condensed", 10) ,bg="yellow")
    next_gagne.place(x=500, y=300)

    next_perdu = Button(fra_11_clavier, text="Perdu", command=ecran4, font=("Bernard MT Condensed", 10) ,bg="yellow")
    next_perdu.place(x=550, y=300)

# Eran 4
# Fonction nouveauMot()
def nouveauMot():
    global mot_Tir

    fra_12.destroy()
##    fra_13.destroy()
##    fra_14.destroy()
##    fra_15.destroy()

    mot_Tir = random.choices(theme_Tir)
    mot_Tir = mot_Tir[0].upper()

    ecran3()

def changerTheme():

    fra_12.destroy()
##    fra_13.destroy()
##    fra_14.destroy()
##    fra_15.destroy()

    ecran2()


def ecran4():
    global fra_12
    global fra_14

    # éffacer les frame de l'éran 3
    fra_8_bonhomme.destroy()
    fra_9_tiret.destroy()
    fra_10_lettres.destroy()
    fra_11_clavier.destroy()

    # Rendre widget inactif, à voir si besoin
##    fra_8_bonhomme.config(state = DISABLED)
##    fra_9_tiret.config(state = DISABLED)
##    fra_10_lettres.config(state = DISABLED)
##    fra_11_clavier.config(state = DISABLED)



    # Initialisation l'écran 3
##    ecran3()

    # Création 4 frames
    fra_12 = Frame(fen, width=500, height=170, bg=couleur.fen_bg)
    fra_13 = Frame(fen, width=500, height=170, bg=couleur.fen_bg)
    fra_14 = Frame(fen, width=1000, height=330, bg=couleur.fen_bg)
    fra_15 = Frame(fen, width=1000, height=100, bg=couleur.fen_bg)

    fra_12.place(x=0, y=0)
    fra_13.place(x=500, y=0)
    fra_14.place(x=0, y=170)
    fra_15.place(x=0, y=500)


    # Frame 12
    resultat_Label = Label(fra_12,
                        text="Le bon mot est : ",
                        font=font.title2,
                        fg=couleur.title2,
                        bg=couleur.fen_bg)
    resultat_Label.place(x=40, y=50)


    # Frame 13
    bon_Mot_Label = Label(fra_13,
                        text=mot_Tir,
                        font=font.title2,
                        fg=couleur.title2,
                        bg=couleur.fen_bg)
    bon_Mot_Label.place(x=40, y=50)


    # Frame 14
##    bravo_img =
    resultat_Canvas = Label(fra_14, text="image Bravo", font=font.title1)
    resultat_Canvas.place(x=150, y=100)

    # Frame 15
    # 3 boutons
    nouveau_Mot_Bouton = Button(fra_15, text="Nouveau Mot", font=font.bou2, command=nouveauMot)
    changer_Theme_Bouton = Button(fra_15, text="Changer Le Thème", font=font.bou2, command=changerTheme)
    exit_Bouton = Button(fra_15, text = "Quitter", font=font.bou2, command=fen.destroy)


    nouveau_Mot_Bouton.place(x=60, y=15)
    changer_Theme_Bouton.place(x=400, y=15)
    exit_Bouton.place(x=850, y=15)

def main():
    global dico

    # Création de la dictionnaires des mots des 5 thèmes
    dico = {}

##    dico["Astronomie"] = ["aabbccd"]         # pour test

    dico["Astronomie"] = ["Soleil", "Planete","Terre","Venus","Mars","Jupiter","Saturne","Etoile"
    "Pulsar" , "Quasar","Supernova","Lune" ,"Lumiere","Astronaute","Galilee","Copernic","Keppler","Newton",
    "Satellite","Fusee" , "NASA" ,"Cosmos","Espace","Télescope","Ciel","Atmsophere","Nuage",
    "Vaisseau","Soucoupe","Amas","Anneau","Apex","Asteroide","Astre","Aube","Aurore","Boreale",
    "Azimiut","Orbite","Stellaire","Constellation","Crepuscule","Galaxie","Eclipse","Equateur",
    "Equinoxe","Geocentrique","Heliocentrique" , "Gravitation","Magnitude","Nebuleuse","Neutron",
    "Neutrino","Boson","Parallaxe","Pleiade","Precession" ,"Solstice","Zodiaque","Photon"]

    dico["Fruits et légumes"] = ["Banane","Kiwi","Pomme","Carotte","Celeri","Rave","Oignon","Fraise","Navet","Concombre",
    "Pois","Avocat","Radis","Peche","Poire","Brugnon","Courgette","Tomate","Courge","Cornichon",
    "Mangue","Ananas","Poireau" ,"Abricot", "Cassis", "Cerise", "Figue", "Framboise", "Groseille",
    "Melon", "Mirabelle", "Mure", "Myrtille", "Pasteque", "Peche", "Prune" , "Artichaut", "Aubergine",
    "Blette", "Brocolis", "Carotte", "Concombre", "Fenouil", "Feve", "Haricot vert", "Pomme de terre",
    "Topinambour","Rutababga" ,"Choux","Citrouille" ,"Potiron" ,"Mache" , "Batavia" , "Endive","Pourpier",
    "Groseille","Lentille","Clémentine","Mandarine","Noix"]

    dico["Etats USA"] = [ "Alabama", "Alaska","Arizona", "Arkansas", "Californie", "Colorado", "Connecticut", "Delaware", "Floride",
    "Hawai", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "Nouveau-Mexique"
    ,"New York", "Caroline du Nord", "Dakota du Nord", "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode-Island",
    "Caroline du Sud", "Dakota du Sud", "Tennessee", "Texas", "Utah", "Vermont", "Virginie" , "Washington",
    "Virginie occidentale", "Wisconsin" , "Wyoming" ]

    dico["Marques Auto"] = ["Lexus","Toyota","Porsche","Renault","Peugeot","Ligier","Toyota","Kia","Suzuki","Cadillac","Pontiac","Dodge","Hyundai",
    "Genesis","Lincoln" , "Acura","Volskwagen","Audi","BMW" ,"Chevrolet" , "Mitsubushi", "Ram", "Mini", "Subaru","Nissan",
    "Mazda","Mercedes","Infinity", "Volvo","Chrysler", "Jagua","Alfa Romeo","Honda","Land Rover","Tesla" ,"Buick",
    "Citroen","Fiat","Corvette","Ferrari","Lamborghini","Seat","Skoda","Opel","Dacia","Excalibur","Aston-Martin","Daihatsu","Daimler"
    "Lada","Matra","Lancia","Lotus","McLaren","Mega","Mazerati","Rover","Simca","Triumph","Saaab","Hummer","Cupra","Delorean","Autobianchi"]

    dico["Animaux"] = ["Girafe", "Zebre", "Ane", "Antilope", "Buffle", "Watusis", "Dromadaire", "Rhinocéros", "Eléphant", "Hippopotame", "Phacochere",
    "Potamochere", "Mouflon", "Ibex" ,"Autruche", "Pelican", "Cormoran", "Grue", "Cigogne", "Jabirus", "Marabout", "Tantale",
    "Pintade", "Outarde", "Calaos", "Mouette", "Dendrocygne", "Tadorne", "Canard", "Ibis", "Spatule", "Aigrette", "Héron",
    "Flamant" , "Oryx", "Addax", "Hippotrague", "Eland", "Gnou", "Bongo", "Nyala", "Koudou", "Cobe", "Sitatunga", "Blesbok",
    "Springbok", "Impala", "Gazelle", "Rat", "Cochon", "Hamster", "Chinchilla", "Dègue", "Gerbille", "Souris", "Putois",
    "Furet" , "Iguane", "Geckos", "Cameleon", "Scorpion", "Araignee", "Myriapode" , "Perruche", "Perroquet", "Diamant",
    "Canaris", "Mainate", "Toucan", "Poule", "Dindon", "Paon", "Oie", "Canard", "Herisson"]


    ecran1()
    fen.mainloop()

if __name__ == '__main__':
    main()

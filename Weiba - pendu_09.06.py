#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bahho
#
# Created:     09/06/2021
# Copyright:   (c) bahho 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


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


class Font:
    """stocker les polices de caractères"""
    def __init__(self):
        self.title1 = tkFont.Font(family="Bauhaus 93", size='60', weight="bold")
        self.title2 = tkFont.Font(family="Berlin Sans FB Demi", size='45', weight="bold")
        self.title3 = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.tex = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")
        self.bou = tkFont.Font(family="Berlin Sans FB Demi", size='40', weight="bold")
        self.bou2 = tkFont.Font(family="Berlin Sans FB Demi", size='25', weight="bold")


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
    regle_3= Label(fra_2, text='* A chaque fois que vous devinez une lettre, *',font=font.tex, bg=couleur.fen_bg, fg=couleur.tex)

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
##
##


#5 fonction tirages
def tirageThemeAstro():
    global mot_Tir
    global theme_Tir

    # Tirage du mot
    nom_Theme_Tir = "Astronomie"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Tir = random.choices(theme_Tir)
    mot_Tir = mot_Tir[0].upper()

    # Ecran 3
    ecran3()

def tirageThemeFruLeg():
    global mot_Tir
    global theme_Tir

    # Tirage du mot
    nom_Theme_Tir = "Fruits et légumes"
    theme_Tir = dico[nom_Theme_Tir]
    mot_Tir = random.choices(theme_Tir)
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


def ecran3():
    global fra_8_bonhomme
    global fra_9_tiret
    global fra_10_lettres
    global fra_11_clavier
    global fra_12_lettre_saisie

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
    list_Tiret = len(mot_Tir)
##    print(list)
    list_Tiret = " _ "*len(mot_Tir)
    tiret_affi = ""
    for i in list_Tiret:
        tiret_affi += i
        tiret_affi += "_"
    tiret_Label = Label(fra_9_tiret, text = list_Tiret, font=("Berlin Sans FB", 20), bg=couleur.fen_bg)
    tiret_Label.place(x=130, y = 50)


##    # Frame 10 lettres essaies
##    list_Lettres = mot_Tir
##    lettres_affi = ""
##    for i in list_Lettres:
##        lettres_affi += i
##        lettres_affi += " "
##    tiret_Label = Label(fra_10_lettres, text = lettres_affi, font=("Berlin Sans FB", 30), bg=couleur.fen_bg)
##    tiret_Label.place(x=130, y = 50)


    # Frame 11 Clavier

    next_gagne = Button(fra_11_clavier, text="Gagné", command=ecran4, font=("Bernard MT Condensed", 30) ,bg="yellow")
    next_gagne.place(x=300, y=250)

    next_perdu = Button(fra_11_clavier, text="Perdu", command=ecran4, font=("Bernard MT Condensed", 30) ,bg="yellow")
    next_perdu.place(x=430, y=250)

    #Frame 12 lettre saisie
    #Boucle permettant d'afficher les lettres devinées (correctes) à la place des tirets
##    for i in len(mot_Tir):
##        if mot_Tir(i) == fra_12_lettre_saisie :
##            list_Tiret[i] = fra_12_lettre_saisie
##            print(list_Tiret)
##        else :
##          afficher le graphique -le pendu
##







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
    bravo_canvas = Label(fra_14, text="je suis image Bravo", font=font.title1)
    bravo_canvas.place(x=150, y=100)

    # Frame 15
    # 3 boutons
    nouveau_Mot_Bouton = Button(fra_15, text="Nouveau Mot", font=font.bou2, command=nouveauMot)
    changer_Theme_Bouton = Button(fra_15, text="Changer le Thème", font=font.bou2, command=changerTheme)
    exit_Bouton = Button(fra_15, text = "Quitter", font=font.bou2, command=fen.destroy)


    nouveau_Mot_Bouton.place(x=60, y=15)
    changer_Theme_Bouton.place(x=400, y=15)
    exit_Bouton.place(x=850, y=15)

def main():
    global dico

    # Création de la dictionnaires des mots des 5 thèmes
    dico = {}

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

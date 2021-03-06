from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import easygui
import random
import unidecode

####################################################################################################################

class Couleur:

    def __init__(self):

        self.blue = "blue"
        self.a = "#d1c386"
        self.b = "#d1c386"
        self.c = "black"
        self.d = "#d1c386"
        self.e = "black"
        self.f = "black"
        self.g = "#3BB9FF"

class Font:

    def __init__(self):

        self.a = tkFont.Font(family = "Bauhaus 93"          , size = '60', weight = "bold")
        self.b = tkFont.Font(family = "Berlin Sans FB Demi" , size = '45', weight = "bold")
        self.c = tkFont.Font(family = "Berlin Sans FB Demi" , size = '25', weight = "bold")
        self.e = tkFont.Font(family = "Berlin Sans FB Demi" , size = '25', weight = "bold")
        self.f = tkFont.Font(family = "Berlin Sans FB Demi" , size = '25', weight = "bold")
        self.d = tkFont.Font(family = "Berlin Sans FB Demi" , size = '15', weight = "bold")

#########################################################################################################################

def Clavier():

    L1   = Frame(F7, bg = "#d1c386")
    L2   = Frame(F7, bg = "#d1c386")
    L3   = Frame(F7, bg = "#d1c386")

    for i in range(0,10):

        lettre_Bouton = Button(L1, text = alpha[i] , fg = couleur.g , font = font.f , width = 2 , borderwidth = 4 )
        lettre_Bouton.config(command =  lambda index = i , valeurBouton = alpha[i]:appuyerBouton(index, valeurBouton))

        lettre_Bouton.pack(side = LEFT , padx = 4 , pady = 10)
        buttons_liste.append(lettre_Bouton)

    for i in range(10,20):

        lettre_Bouton = Button(L2, text = alpha[i] , fg = couleur.g , font = font.f , width = 2 , borderwidth = 4 )
        lettre_Bouton.config(command =  lambda index = i , valeurBouton = alpha[i]:appuyerBouton(index, valeurBouton))

        lettre_Bouton.pack(side = LEFT , padx = 4 , pady = 10)
        buttons_liste.append(lettre_Bouton)

    for i in range(20,26):

        lettre_Bouton = Button(L3, text = alpha[i] , fg = couleur.g , font = font.f , width = 2 , borderwidth = 4 )
        lettre_Bouton.config(command =  lambda index = i , valeurBouton = alpha[i]:appuyerBouton(index, valeurBouton))

        lettre_Bouton.pack(side = LEFT , padx = 4 , pady = 10)
        buttons_liste.append(lettre_Bouton)

    # print(buttons_liste)

    L1.place(x = 9   , y = 40)
    L2.place(x = 9   , y = 140)
    L3.place(x = 120 , y = 240)

def ThemeAnimals():

    global WordTheme

    WordTheme = random.choice(list(dico["Animaux"])).upper()
    WordTheme = unidecode.unidecode(WordTheme)

    Screen2()

def ThemeAstronomie():

    global WordTheme

    WordTheme = random.choice(list(dico["Astronomie"])).upper()
    WordTheme = unidecode.unidecode(WordTheme)

    Screen2()

def ThemeFruitsLegumes():

    global WordTheme

    WordTheme = random.choice(list(dico["Fruits et L??gumes"])).upper()
    WordTheme = unidecode.unidecode(WordTheme)

    Screen2()

def ThemeStateUS():

    global WordTheme

    WordTheme = random.choice(list(dico["Etats USA"])).upper()
    WordTheme = unidecode.unidecode(WordTheme)

    Screen2()

def ThemeMarquesAuto():

    global WordTheme

    WordTheme = random.choice(list(dico["Marques Auto"])).upper()
    WordTheme = unidecode.unidecode(WordTheme)

    Screen2()

##############################################################################################################################

def Screen1():

    global F1, F2, F3, F4, R1, R2, R3

    F1 = Frame(fen, width = 1000 , height = 229 , bg = couleur.blue)
    F2 = Frame(fen, width = 1000 , height = 229 , bg = couleur.blue)
    F3 = Frame(fen, width = 700  , height = 75  , bg = couleur.blue)
    F4 = Frame(fen, width = 700  , height = 75  , bg = couleur.blue)

    F1.pack()
    F2.pack()
    F3.pack(pady = 25)
    F4.pack(pady = 25)

    T = Label(F1 , text = 'Bienvenue \n sur le jeu du pendu !', font = font.a , bg = couleur.blue , fg = couleur.a)
    T.pack(pady = 15)

    R1 = Label(F2 , text = ' Le jeu consiste ?? deviner les lettres du mot Myst??re.', font = font.e, bg = couleur.blue , fg = couleur.e)
    R2 = Label(F2 , text = ' Choisissez votre th??me, vous pouvez faire 9 erreurs.', font = font.e , bg = couleur.blue , fg = couleur.e)
    R3 = Label(F2 , text = ' A chaque fois que vous devinez une lettre, celle-ci s affiche.' , font = font.e , bg = couleur.blue , fg = couleur.e)

    R1.pack()
    R2.pack()
    R3.pack()

    Button_Astro  = Button(F3, text = "Astro"    ,  width = 8 , height = 2 , command = ThemeAstronomie    , bg = '#d1c386' , font = font.d)
    Button_FruLeg = Button(F3, text = "L??gumes"  ,  width = 8 , height = 2 , command = ThemeFruitsLegumes , bg = '#d1c386' , font = font.d)
    Button_Etats  = Button(F3, text = "USA"      ,  width = 8 , height = 2 , command = ThemeStateUS       , bg = '#d1c386' , font = font.d)
    Button_MarVoi = Button(F3, text = "Voitures" ,  width = 8 , height = 2 , command = ThemeMarquesAuto   , bg = '#d1c386' , font = font.d)
    Button_Ani    = Button(F3, text = "Animaux"  ,  width = 8 , height = 2 , command = ThemeAnimals       , bg = '#d1c386' , font = font.d)

    Button_Astro.place  ( x = 0   , y = 5 )
    Button_FruLeg.place ( x = 600 , y = 5 )
    Button_Etats.place  ( x = 300 , y = 5 )
    Button_MarVoi.place ( x = 150 , y = 5 )
    Button_Ani.place    ( x = 450 , y = 5 )

    endButt = Button(F4, text = "EXIT", height = 1, font = font.d , bg = couleur.d , fg = couleur.f , command = fen.destroy)
    endButt.pack()

def Screen2():

    global F5, F6, F7, F8, F9, R1, R2, R3, L1, L2, L3, C6
    global letter_disp
    global Lab5, buttons_liste, index, lettre_Bouton, alpha, valeurBoutton

    F1.pack_forget()
    F2.pack_forget()
    F3.pack_forget()
    F4.pack_forget()

    # ne pas mettre les definitons des frames dans les fonctions , on definit tout dans le screen 3

    F5   = Frame(fen , width = 618, height = 120 , bg = '#d1c386') # frame pour les tirets en milieu haut FRAME 9
    F6   = Frame(fen , width = 618, height = 250 , bg = '#d1c386') # frame pour le stockage des lettres incorrectes en bouttons
    F7   = Frame(fen , width = 618, height = 360 , bg = '#d1c386') # frame pour le clavier
    F8   = Frame(fen , width = 380, height = 90  , bg = 'blue'   ) # frame pour l'affichage du mot myst??re
    F9   = Frame(fen , width = 380, height = 90  , bg = 'blue'   ) # frame pour le winloose

    Clavier()

    GOODWORD = Label(F8, text = WordTheme , fg = "black" , bg = '#d1c386' ,  font = font.f)
    GOODWORD.place(x = 0, y = 10)

    DisplayLetter0()
    DisplayLetter()

    C6 = Canvas(F6 , width = 700 , height = 250 , bg = '#d1c386' , highlightthickness = 0 )
    C6.place(x = 10 , y = 0)

    Lab5 = Label(F5, text = letter_disp , font = ("Berlin Sans FB", 25) , bg = '#d1c386')

    F5.place(x = 382 , y = 0   ) # frame pour les tirets milieu haut du screen 2
    F6.place(x = 382 , y = 120 ) # frame pour les lettres incorrectes milieu du screen 2
    F7.place(x = 382 , y = 240 ) # frame pour le clavier
    F8.place(x = 0   , y = 0   ) # frame pour l'affichage du mot myst??re
    F9.place(x = 0   , y = 80  ) # frame pour l'affichage du winloose

    Lab5.place(x = 10 , y = 50) # label a mettre ?? la fin du screen 3 pour l'affichage des tirets en frame 9

def DisplayLetter0() : # affichage tous les tirets du mot myst??re pour le screen 3

    global Wordtheme

    for i in WordTheme:

        if i == "-" or i == " ":
            list_res.append(" ")
        else:
            list_res.append(i)

    print("mot mystere : " , list_res)

    return list_res

def DisplayLetter(): # affichage des lettres pour le screen 3 en frame 12

    global letter_disp

    for i in list_res:

        if i == "-":
            letter_disp += i
        else:
            letter_disp += "__"

        letter_disp += "  "

    for i in list_res:

        if i == "-" or i == " ":
            list_essais.append("-")
        else:
            list_essais.append("*")

    return letter_disp

#########################################################################################################################

def appuyerBouton(index, valeurBouton):

    global compteur , F5

    print("valeur bouton : " , valeurBouton)
    print("valeur index : "  , index)

    buttons_liste[index].config(state = "disabled", relief = 'sunken')

    # Boucle permettant d'afficher les lettres devin??es correctes ?? la place des tirets,
    # Sinon afficher le pendu et d??place la lettre

    if valeurBouton in list_res:

        for i in range(0, len(list_res)):

            if list_res[i] == valeurBouton :

                list_essais[i] = valeurBouton
                DisplayLetterTrue()
    else :

        deplaceBouton(valeurBouton)
        print("lettre ", valeurBouton , "incorrecte mise en frame 6 du screen 2")
        compteur += 1
        print(compteur)

    WinLoose()

def DisplayLetterTrue(): # affiche les lettres correctes en frame 9

    global F5, Lab5

    Lab5.destroy()

    letter_disp = ""

    for i in list_essais:

        if i =="*":
            letter_disp += "__"
        else:
            letter_disp += i
        letter_disp += " "

    print("lettre trouv?? : " , letter_disp)

    Lab5 = Label(F5, text = letter_disp , font = ("Berlin Sans FB", 25) , bg = '#d1c386')
    Lab5.place(x = 50 , y = 50) # label recr??e a chaque fois qu'une lettre est correcte

def deplaceBouton(valeurBouton):

    global F5

    LetterFalse = Button(C6, text = valeurBouton )
    LetterFalse.config(fg = couleur.g)
    LetterFalse.config(bg = couleur.blue)

    LetterFalse.config(font = font.f)
    LetterFalse.config(width = 2)
    LetterFalse.config(borderwidth = 4)

    LetterFalse.pack(side = LEFT , padx = 4 , pady = 10)

def WinLoose():

    global compteur, list_res, list_essais, F5, F6, F9

    if list_res == list_essais:

        LabRes = Label(F9, text = "Win" ,  font = font.f ,  bg = '#d1c386')
        LabRes.place(x = 0 , y =  30)

    elif compteur >= 9:
        print("perdu")
        LabRes = Label(F9, text = "Loose" ,  font = font.f , bg = '#d1c386')
        LabRes.place(x = 0 , y =  30)
    else:
        pass

def main():

    global dico

    dico = dict()

    dico["Astronomie"] = {"Soleil", "Plan??te","Terre","V??nus","Mars","Jupiter","Saturne","Etoile",
    "Pulsar" , "Quasar","Supernova","Lune" ,"Lumi??re","Astronaute","Galil????","Copernic","Keppler","Newton",
    "Satellite","Fus??e" , "NASA" ,"Cosmos","Espace","T??lescope","Ciel","Atmsoph??re","Nuage",
    "Vaisseau","Soucoupe","Amas","Anneau","Apex","Ast??roide","Astre","Aube","Aurore","Bor??ale",
    "Azimiut","Orbite","Stellaire","Constellation","Cr??puscule","Galaxie","Eclipse","Equateur",
    "Equinoxe","G??ocentrique","H??liocentrique" , "Gravitation","Magnitude","N??buleuse","Neutron",
    "Neutrino","Boson","Parallaxe","Pl??iade","Pr??cession" ,"Solstice","Zodiaque","Photon",
    "Absorption atmosph??rique" ,"Adaptation nocturne" , "Alb??do" , "Almucantar" , "Amas d?????toiles" ,
    "Amas globulaire" ,"Amas ouvert" , "Anneaux de Saturne" , "Ann??e-lumi??re" , "Annulaire" ,
    " Anticr??pusculaire" , "Apex" , "Aph??lie" , "APN" , "Apog??e" , "Apparition" , "Appulse" ,
    "Ascension droite", "Ast??risme" , "Ast??ro??de" , "Astre" , "Astrologie" , "Astronomie" , "Astrophysicien" ,
    "Aube" , "Aurore polaire" , "Axe" , "Azimut" , "Binaire ?? ??clipse" , "Bolide" , "Centre galactique" ,
    "C??ph??ide" , "Champ magn??tique" , "Classe spectrale" , "Com??te" , "Conjonction" , "Conjonction inf??rieure" ,
    "Conjonction sup??rieure" , "Constellation" , "Cr??puscule" , "Culminer" , "D??clinaison" , "Dernier Quartier" ,
    "Diagramme HR" , "Double optique" , "??clipse" , "??cliptique" , "??longation" , "??quateur" , "??quateur c??leste" ,
    "??quateur galactique" , "??quation du temps" , "??quinoxe" ,  "ESA" , "??toile du berger" , "Exoplan??te" , "Externe" ,
    "Galaxie" , "G??ante bleue" , "G??ante rouge" , "G??ocentrique" , "Gibbeuse" , "Gravitation" , "Greenwich" , "Hauteur" ,
    "H??liocentrique" , " Horizon vrai" , "Inclinaison" , "Inf??rieure" , "Interne" , "Jeune Lune" , "Limbe" , "Lumi??re cendr??e"
    , "Lumi??re zodiacale" , "Lunaison" , "Lune" , "Magnitude" ,"Magnitude absolue" , "Mar??es" , "M??ridien" , "M??t??orite" ,
    "Mouvement propre" , "Multiples" , "Naine blanche" , "Naine brune" , "Naine rouge" , "NASA" , "N??buleuse"  , "N??buleuse plan??taire" ,
    "Neutrons" , "N??ud" , "Nouvelle Lune" , "Obliquit??" , "Occultation" , "Occultation rasante" , "Opposition" , "Orbite" ,
    "Parallaxe" , "Parsec" , "P??nombre" , "P??rig??e" , "P??rih??lie" , "P??riodique", "Phases" , "Plan??te" , "Pl??iades" , "Pleine Lune" ,
    "P??le" , "Pollution lumineuse" , "Pr??cession" , "Premier Quartier" , "Quadrature" , "Radiant", "Rayons gamma" ,
    "R??manent de supernova" , "R??trogradation" , "R??volution" , "Rotation" , "Satellite" , "Seeing" , "S??l??n??" ,
    "SOHO" , "Solstice" , "Sonde" , "Station spatiale internationale" , "Stationnaire" , "Superg??ante" ,
    "Sup??rieure" , "Supernova" , "Synodique" ,"Syst??me plan??taire" , "Taux horaire au z??nith" , "Telluriques" ,
    "Temps universel" , "Terminateur" , "Topocentrique" , "Transit" , "Trou noir" , "Turbulence" , "Unit?? astronomique" ,
    "Variable" , "Vernal" , "Vieille Lune" , "Vision d??cal??e" , "VLT" , "Voie lact??e" , "Z??nith" , "Zodiaque" }

    dico["Fruits et L??gumes"] = {"Banane","Kiwi","Pomme","Carotte","C??leri","Rave","Oignon","Fraise","Navet","Concombre",
    "Pois","Avocat","Radis","P??che","Poire","Brugnon","Courgette","Tomate","Courge","Cornichon",
    "Mangue","Ananas","Poireau" ,"Abricot", "Cassis", "Cerise", "Figue", "Framboise", "Groseille",
    "Melon", "Mirabelle", "M??re", "Myrtille", "Past??que", "P??che", "Prune" , "Artichaut", "Aubergine",
    "Blette", "Brocolis", "Carotte", "Concombre", "Fenouil", "F??ve", "Haricot vert", "Pomme de terre",
    "Topinambour","Rutababga" ,"Choux","Citrouille" ,"Potiron" ,"Mache" , "Batavia" , "Endive","Pourpier",
    "Groseille","Lentille","Cl??mentine","Mandarine","Noix"}

    dico["Etats USA"] = {"Alabama", "Alaska","Arizona", "Arkansas", "Californie", "Colorado", "Connecticut", "Delaware", "Floride",
    "Hawa??", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan",
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "Nouveau Mexique",
    "Hawa??","New York", "Caroline du Nord", "Dakota du Nord", "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode Island",
    "Caroline du Sud", "Dakota du Sud", "Tennessee", "Texas", "Utah", "Vermont", "Virginie" , "Washington",
    "Virginie occidentale", "Wisconsin" , "Wyoming" }

    dico["Marques Auto"] = {"Lexus","Toyota","Porsche","Renault","Peugeot","Ligier","Toyota","Kia","Suzuki","Cadillac","Pontiac","Dodge","Hyundai",
    "Genesis","Lincoln" , "Acura","Volskwagen","Audi","BMW","Chevrolet" , "Mitsubushi", "Ram", "Mini", "Subaru","Nissan",
    "Mazda","Mercedes","Infinity", "Volvo","Chrysler", "Jaguar","Alfa Romeo","Honda","Land Rover","Tesla" ,"Buick",
    "Citroen","Fiat","Corvette","Ferrari","Lamborghini","Seat","Skoda","Opel","Dacia","Excalibur","Aston Martin","Daihatsu","Daimler",
    "Lada","Matra","Lancia","Lotus","McLaren","Mega","Mazerati","Rover","Simca","Triumph","Saaab","Hummer","Cupra","Delorean","Autobianchi"}

    dico["Animaux"] = {"Girafe", "Z??bre", "Ane", "Antilope", "Buffle", "Watusis", "Dromadaire", "Rhinoc??ros", "El??phant", "Hippopotame", "Phacoch??re",
    "Potamoch??re", "Mouflon", "Ibex" ,"Autruche", "P??lican", "Cormoran", "Grue", "Cigogne", "Jabirus", "Marabout", "Tantale",
    "Pintade", "Outarde", "Calaos", "Mouette", "Dendrocygne", "Tadorne", "Canard", "Ibis", "Spatule", "Aigrette", "H??ron",
    "Flamant" , "Oryx", "Addax", "Hippotrague", "Eland", "Gnou", "Bongo", "Nyala", "Koudou", "Cobe", "Sitatunga", "Blesbok",
    "Springbok", "Impala", "Gazelle", "Rat", "Cochon", "Hamster", "Chinchilla", "D??gue", "Gerbille", "Souris", "Putois",
    "Furet" , "Iguane", "Geckos", "Cam??l??on", "Scorpion", "Araign??e", "Myriapode" , "Perruche", "Perroquet", "Diamant",
    "Canaris", "Mainate", "Toucan", "Poule", "Dindon", "Paon", "Oie", "Canard", "H??risson"}

    Screen1()
    fen.mainloop()

fen = Tk()
fen.title("Jeu Pendu")
fen.geometry("1050x600")
fen.resizable(width = False, height = False)

couleur = Couleur()
font = Font()

fen.config(bg = couleur.blue)

# la variable compteur doit ??tre initialis?? et global car utilis??e dans la lambda function des touches du clavier

alpha = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]

compteur = 0

letter_disp = ""

list_res = []
list_essais = []
buttons_liste = []
list_LettreEssayees = []

if __name__ == '__main__':
    main()

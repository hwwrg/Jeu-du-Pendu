##----- Importation des Modules -----##

from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import tkinter.ttk as ttk
import tkinter.font as tkFont
from random import randrange
import random

# Dictionnaire

global dico

dico = dict()

dico["Astronomie"] = {"Soleil", "Planète","Terre","Vénus","Mars","Jupiter","Saturne","Etoile",
"Pulsar" , "Quasar","Supernova","Lune" ,"Lumière","Astronaute","Galiléé","Copernic","Keppler","Newton",
"Satellite","Fusée" , "NASA" ,"Cosmos","Espace","Télescope","Ciel","Atmsophère","Nuage",
"Vaisseau","Soucoupe","Amas","Anneau","Apex","Astéroide","Astre","Aube","Aurore","Boréale",
"Azimiut","Orbite","Stellaire","Constellation","Crépuscule","Galaxie","Eclipse","Equateur",
"Equinoxe","Géocentrique","Héliocentrique" , "Gravitation","Magnitude","Nébuleuse","Neutron",
"Neutrino","Boson","Parallaxe","Pléiade","Précession" ,"Solstice","Zodiaque","Photon"}

dico["Fruits et Légumes"] = {"Bananne","Kiwi","Pomme","Carotte","Céleri","Rave","Oignon","Fraise","Navet","Concombre",
"Pois","Avocat","Radis","Pêche","Poire","Brugnon","Courgette","Tomate","Courge","Cornichon",
"Mangue","Anannas","Poireau" ,"Abricot", "Cassis", "Cerise", "Figue", "Framboise", "Groseille",
"Melon", "Mirabelle", "Mûre", "Myrtille", "Pastèque", "Pêche", "Prune" , "Artichaut", "Aubergine",
"Blette", "Brocolis", "Carotte", "Concombre", "Fenouil", "Fève", "Haricot vert", "Pomme de terre",
"Topinambour","Rutababga" ,"Choux","Citrouille" ,"Potiron" ,"Mache" , "Batavia" , "Endive","Pourpier",
"Groseille","Lentille","Clémentine","Mandarine","Noix"}

dico["Etats USA"] = { "Alabama", "Alaska","Arizona", "Arkansas", "Californie", "Colorado", "Connecticut", "Delaware", "Floride",
"Hawaï", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan",
"Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "Nouveau-Mexique",
"Hawaï","New York", "Caroline du Nord", "Dakota du Nord", "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode-Island",
"Caroline du Sud", "Dakota du Sud", "Tennessee", "Texas", "Utah", "Vermont", "Virginie" , "Washington",
"Virginie occidentale", "Wisconsin" , "Wyoming" }

dico["Marques Auto"] = {"Lexus","Toyota","Porsche","Renault","Peugeot","Ligier","Toyota","Kia","Suzuki","Cadillac","Pontiac","Dodge","Hyundai",
"Genesis","Lincoln" , "Acura","Volskwagen","Audi","BMW" ,"Chevrolet" , "Mitsubushi", "Ram", "Mini", "Subaru","Nissan",
"Mazda","Mercedes","Infinity", "Volvo","Chrysler", "Jagua","Alfa Romeo","Honda","Land Rover","Tesla" ,"Buick",
"Citroen","Fiat","Corvette","Ferrari","Lamborghini","Seat","Skoda","Opel","Dacia","Excalibur","Aston-Martin","Daihatsu","Daimler",
"Lada","Matra","Lancia","Lotus","McLaren","Mega","Mazerati","Rover","Simca","Triumph","Saaab","Hummer","Cupra","Delorean","Autobianchi"}

dico["Animaux"] = {"Girafe", "Zèbre", "Ane", "Antilope", "Buffle", "Watusis", "Dromadaire", "Rhinocéros", "Eléphant", "Hippopotame", "Phacochère",
"Potamochère", "Mouflon", "Ibex" ,"Autruche", "Pélican", "Cormoran", "Grue", "Cigogne", "Jabirus", "Marabout", "Tantale",
"Pintade", "Outarde", "Calaos", "Mouette", "Dendrocygne", "Tadorne", "Canard", "Ibis", "Spatule", "Aigrette", "Héron",
"Flamant" , "Oryx", "Addax", "Hippotrague", "Eland", "Gnou", "Bongo", "Nyala", "Koudou", "Cobe", "Sitatunga", "Blesbok",
"Springbok", "Impala", "Gazelle", "Rat", "Cochon", "Hamster", "Chinchilla", "Dègue", "Gerbille", "Souris", "Putois",
"Furet" , "Iguane", "Geckos", "Caméléon", "Scorpion", "Araignée", "Myriapode" , "Perruche", "Perroquet", "Diamant",
"Canaris", "Mainate", "Toucan", "Poule", "Dindon", "Paon", "Oie", "Canard", "Hérisson"}

def creat_label(liste,frame):

    global F0,F1,F2,F3

    fontText = tkFont.Font(family = "Berlin Sans FB Demi", size ='18', weight = "bold")

    for infoel in liste:
        info = Label(frame, text = infoel, fg = 'black', bg = "#c6dcd4" , font = fontText)
        info.place(x=24)

def listAzerty():
    return ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]

def creat_button_clav(liste,frame):

    global listoption

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi", size = 19 )
    # fontExample.configure(underline = True)

    fgExample = "black"
    bgExample = "#b8945c"
    
    for infoel in liste:
        info = Button(frame, text = infoel, width = 2 , fg = fgExample , bg = bgExample , font = fontExample)
        info.pack(side = LEFT)

def decouper(texte):
    # Découpe le texte par morceau de 1 lettres
    decoupage = [texte[i:i+1] for i in range(0, len(texte), 1)]
    # Recrée la chaine avec un espace toutes les 3 lettres
    return " ".join(decoupage)

def wordThemeAnimals():

    for w in F4.winfo_children(): 
        w.destroy()

    wordTheme = random.choice(list(dico["Animaux"])).upper()

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi" , size = 20 )
    
    C4 = Canvas(F4 , width = 600, height = 90 , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )

    LabeAnim = Label(C4, text = decouper(wordTheme), fg = 'black', bg = "ivory" , font = fontExample)        
    LabeAnim.place(x = 5, y = 20)

    for i in range(0,len(wordTheme)):
        if wordTheme[i] ==" " or wordTheme[i] =="-":
            info = Label(C4, text = "   ", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )
        else:
            info = Label(C4, text = "___", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )

    C4.pack()
    F4.place(x = 300, y = 350)

def wordThemeAstronomie():

    for w in F4.winfo_children(): 
        w.destroy()

    wordTheme = random.choice(list(dico["Astronomie"])).upper()

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi" , size = 20 )

    C4 = Canvas(F4 , width = 600, height = 90 , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
        
    Labelastro = Label(C4, text = decouper(wordTheme), fg = 'black', bg = "ivory" , font = fontExample)        
    Labelastro.place(x = 5 , y = 20)

    for i in range(0,len(wordTheme)):
        if wordTheme[i] ==" " or wordTheme[i] =="-":
            info = Label(C4, text = "   ", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )
        else:
            info = Label(C4, text = "___", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )

    C4.pack()
    F4.place(x = 300, y = 350)

def wordThemeFruitsLegumes():

    for w in F4.winfo_children(): 
        w.destroy()

    wordTheme = random.choice(list(dico["Fruits et Légumes"])).upper()

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi" , size = 20 )

    C4 = Canvas(F4 , width = 600, height = 90 , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
        
    LabeFruts = Label(F4, text = decouper(wordTheme), fg = 'black', bg = "ivory" , font = fontExample)        
    LabeFruts.place(x = 5, y = 20)

    for i in range(0,len(wordTheme)):
        if wordTheme[i] ==" " or wordTheme[i] =="-":
            info = Label(C4, text = "   ", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )
        else:
            info = Label(C4, text = "___", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )

    C4.pack()
    F4.place(x = 300, y = 350)

def wordThemeStateUS():

    for w in F4.winfo_children(): 
        w.destroy()

    wordTheme = random.choice(list(dico["Etats USA"])).upper()

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi" , size = 20 )

    C4 = Canvas(F4 , width = 600, height = 90 , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
        
    LabeUS = Label(C4, text = decouper(wordTheme) , fg = 'black', bg = "ivory" , font = fontExample)        
    LabeUS.place(x = 5, y = 20)

    for i in range(0,len(wordTheme)):
        if wordTheme[i] ==" " or wordTheme[i] =="-":
            info = Label(C4, text = "   ", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )
        else:
            info = Label(C4, text = "___", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )

    C4.pack()
    F4.place(x = 300, y = 350)

def wordThemeMarquesAuto():

    for w in F4.winfo_children(): 
        w.destroy()

    wordTheme = random.choice(list(dico["Marques Auto"])).upper()

    fontExample = tkFont.Font(family = "Berlin Sans FB Demi" , size = 20 )

    C4 = Canvas(F4 , width = 600, height = 90 , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
        
    LabeAuto = Label(C4, text = decouper(wordTheme), fg = 'black', bg = "ivory" , font = fontExample)        
    LabeAuto.place(x = 5 , y = 20)

    for i in range(0,len(wordTheme)):
        if wordTheme[i] ==" " or wordTheme[i] =="-":
            info = Label(C4, text = "   ", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )
        else:
            info = Label(C4, text = "___", fg = 'black', bg = "ivory" , font = fontExample)      
            info.place( x = 5 + 40*i, y = 50 )

    C4.pack()
    F4.place(x = 300, y = 350)

def play():

    global listinfo
    global F0,F1,F2,F3,F6

    F0.pack_forget()
    F1.place(x = 70  , y = 30)
    F2.place(x = 200 , y = 475)
    F3.place(x = 200 , y = 527)
    F6.place(x = 30 , y = 100)
    C1.pack()

# fenetre principale

fen = Tk() # fenetre de travail courante
fen.title("Jeu Pendu")
fen.geometry("900x600")

fen.iconbitmap("photoapp.ico")
fen.config(bg = "#c6dcd4")

F0 = Frame(fen, bg = "#c6dcd4") # F0 pour le screen 0 feuille de présentation
F1 = Frame(fen, width = 535, height = 100 , bg = "black")
F2 = Frame(fen, width = 535, height = 50  , bg = "ivory") 
F3 = Frame(fen, width = 535, height = 50  , bg = "ivory") 
F4 = Frame(fen, width = 600, height = 60 , bg = "ivory")

F5 = Frame(fen, bg = "white")
F6 = Frame(fen, bg = "black")

fontTitre1 = tkFont.Font(family = "Bauhaus 93", size = '40', weight = "bold")
fontTitre2 = tkFont.Font(family = "Berlin Sans FB Demi", size ='30', weight ="bold")
fontText   = tkFont.Font(family = "Berlin Sans FB Demi", size ='15', weight ="bold")

titre_fen = Label(F0, text='Bienvenue \n sur Hangman 2021 !', font = fontTitre1, bg= "#c6dcd4", fg='#8b6738')

text_1 = Label(F0, text ='! Choisis un thème & devine les lettres qui compose le Mot Mystère !', font = fontText, bg = "#c6dcd4", fg ='black' )
text_2 = Label(F0, text ='! Dés que tu découvres une lettre celle-ci s affiche !', font = fontText, bg = "#c6dcd4", fg ='black')
text_3 = Label(F0, text ='! Sinon un élement du pendu apparait !', font = fontText, bg = "#c6dcd4", fg ='black')
text_4 = Label(F0, text ='! Tu as droit à 9 essais !', font = fontText, bg = "#c6dcd4", fg='black')

im = Image.open("C:/Users/Briche/Desktop/GRETA_2021/pendu3d.png")
img = ImageTk.PhotoImage(im, master = F0)

C = Canvas(F0 , width = im.size[0], height = im.size[1] , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
C.create_image(0,0, anchor = NW , image = img)

im1 = Image.open("C:/Users/Briche/Desktop/GRETA_2021/pendu3d.png")
img1 = ImageTk.PhotoImage(im1, master = F4)

C1 = Canvas(F6 , width = im.size[0], height = im.size[1] , bg = "#c6dcd4", bd = 0, highlightthickness = 0 )
C1.create_image(0,0, anchor = NW , image = img1)

im2 = Image.open("C:/Users/Briche/Desktop/GRETA_2021/lependubis.png")
logo2 = ImageTk.PhotoImage(im2, master = F5)

C2 = Canvas(F5, width = 130, height = 350 , bg = "#c6dcd4", bd = 0, highlightthickness = 0)
C2.create_image(60, 150, image = logo2) # centrage dans C2 de l'image   

titre_fen.pack()

text_1.pack()
text_2.pack()
text_3.pack()
text_4.pack()

b1 = Button(F0, text='A toi de jouer ! ', font = fontText, bg= "#c6dcd4", fg ="black" , command = play) 
b2 = Button(F0, text ="Quitter", font = fontText, bg = "#c6dcd4", fg ="black",  command = fen.destroy)

fontText = tkFont.Font(family = "Berlin Sans FB Demi", size ='13', weight ="bold")

banim    = Button(F1, text = "FAUNE  "          , fg = 'black', bg = "#cd9d64" ,  font = fontText , command = wordThemeAnimals       )
bastro   = Button(F1, text = "ASTRONOMIE"       , fg = 'black', bg = "#cd9d64" ,  font = fontText , command = wordThemeAstronomie    )
bfruts   = Button(F1, text = "FRUITS, LEGUMES"  , fg = 'black', bg = "#cd9d64" ,  font = fontText , command = wordThemeFruitsLegumes )
bstateus = Button(F1, text = "ETATS DES USA"    , fg = 'black', bg = "#cd9d64" ,  font = fontText , command = wordThemeStateUS       )
bauto    = Button(F1, text = "MARQUES AUTO"     , fg = 'black', bg = "#cd9d64" ,  font = fontText , command = wordThemeMarquesAuto   )

banim.pack(     side = LEFT     , padx = 5 , pady = 5)
bastro.pack(    side = LEFT     , padx = 5 , pady = 5)
bfruts.pack(    side = LEFT     , padx = 5 , pady = 5)
bstateus.pack(  side = LEFT     , padx = 5 , pady = 5)
bauto.pack(     side = LEFT     , padx = 5 , pady = 5)

b1.pack()
b2.pack()

C.pack()  # depend de F0
C2.pack() # dépend de F5

F0.pack(side = LEFT)
F5.place(x = 770, y = 10)

listeButtonClavier = listAzerty()
creat_button_clav(listeButtonClavier[0:13] ,F2)
creat_button_clav(listeButtonClavier[13:29],F3)

fen.mainloop()
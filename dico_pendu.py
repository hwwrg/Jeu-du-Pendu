#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Briche
#
# Created:     25/05/2021
# Copyright:   (c) Briche 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from tkinter import *
from PIL import*
from PIL import ImageTk, Image

dico = {"Astronomie":1,"Fruits & Légumes":2,"Etats des USA":3,"Marques de voiture":4,"Animaux":5}

dico["Astronomie"] = {"Soleil", "Planète","Terre","Vénus","Mars","Jupiter","Saturne","Etoile"
                        "Pulsar" , "Quasar","Supernova","Lune" ,"Lumière","Astronaute","Galiléé","Copernic","Keppler","Newton",
                        "Satellite","Fusée" , "NASA" ,"Cosmos","Espace","Télescope","Ciel","Atmsophère","Nuage",
                        "Vaisseau","Soucoupe","Amas","Anneau","Apex","Astéroide","Astre","Aube","Aurore","Boréale",
                        "Azimiut","Orbite","Stellaire","Constellation","Crépuscule","Galaxie","Eclipse","Equateur",
                        "Equinoxe","Géocentrique","Héliocentrique" , "Gravitation","Magnitude","Nébuleuse","Neutrons",
                        "Neutrino","Boson","Parallaxe","Pléiade","Précession" ,"Solstice","Zodiaque","Photon"}

dico["Fruits & Légumes"] = {"Bananne","Kiwi","Pomme","Carotte","Céleri","Rave","Oignon","Fraise","Navet","Concombre",
                            "Pois","Avocat","Radis","Pêche","Poire","Brugnon","Courgette","Tomate","Courge","Cornichon"
                            , "Mangue","Anannas","Poireau" ,"Abricot", "Cassis", "Cerise", "Figue", "Framboise", "Groseille",
                             "Melon", "Mirabelle", "Mûre", "Myrtille", "Pastèque", "Pêche", "Prune" , "Artichaut", "Aubergine",
                              "Blette", "Brocolis", "Carotte", "Concombre", "Fenouil", "Fève", "Haricot vert", "Pomme de terre"
                              ,"Topinambour","Rutababga" ,"Choux","Citrouille" ,"Potiron" ,"Mache" , "Batavia" , "Endive","Pourpier"
                              "Groseille","Lentille","Clémentine","Mandarine","Noix"}


dico["Etats des USA"] = { "Alabama", "Alaska","Arizona", "Arkansas", "Californie", "Colorado", "Connecticut", "Delaware", "Floride",
                           "Hawaï", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiane", "Maine", "Maryland", "Massachusetts", "Michigan",
                            "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "Nouveau-Mexique",
                            "Hawaï","New York", "Caroline du Nord", "Dakota du Nord", "Ohio", "Oklahoma", "Oregon", "Pennsylvanie", "Rhode Island",
                            "Caroline du Sud", "Dakota du Sud", "Tennessee", "Texas", "Utah", "Vermont", "Virginie" , "Washington",
                            "Virginie occidentale", "Wisconsin" , "Wyoming" }


dico["Marques de voiture"] = {"Lexus","Toyota","Porsche","Renault","Peugeot","Ligier","Toyota","Kia","Suzuki","Cadillac","Pontiac","Dodge","Hyundai",
                                "Genesis","Lincoln" , "Acura","Volskwagen","Audi","BMW" ,"Chevrolet" , "Mitsubushi" , "Ram", "Mini", "Subaru","Nissan",
                                "Mazda","Mercedes","Infinity", "Volvo","Chrysler", "Jagua","Alfa Romeo","Honda","Land Rover","Tesla" ,"Buick",
                               "Citroen","Fiat","Corvette","Ferrari","Lamborghini","Seat","Skoda","Opel","Dacia","Excalibur","Aston-Martin","Daihatsu","Daimler"
                               "Lada","Matra","Lancia","Lotus","McLaren","Mega","Mazerati","Rover","Simca","Triumph","Saaab","Hummer","Cupra","Delorean","Autobianchi"}



dico["Animaux"] = {"Girafe", "Zèbre", "Ane", "Antilope", "Buffle", "Watusis", "Dromadaire", "Rhinocéro", "Eléphant", "Hippopotame", "Phacochère",
                    "Potamochère", "Mouflon", "Ibex" ,"Autruche", "Pélican", "Cormoran", "Grue", "Cigogne", "Jabirus", "Marabout", "Tantale",
                    "Pintade", "Outarde", "Calaos", "Mouette", "Dendrocygne", "Tadorne", "Canard", "Ibis", "Spatule", "Aigrette", "Héron",
                    "Flamant" , "Oryx", "Addax", "Hippotrague", "Eland", "Gnou", "Bongo", "Nyala", "Koudou", "Cobe", "Sitatunga", "Blesbok",
                    "Springbok", "Impala", "Gazelle", "Rat", "Cochon", "Hamster", "Chinchilla", "Dègue", "Gerbille", "Souris", "Putois",
                    "Furet" , "Iguane", "Geckos", "Caméléon", "Scorpion", "Araignée", "Myriapode" , "Perruche", "Perroquet", "Diamant",
                    "Canaris", "Mainate", "Toucan", "Poule", "Dindon", "Paon", "Oie", "Canard", "Hérisson"}

# il faut relier un des dico a un theme
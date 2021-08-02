from tkinter import*

fen_4 = Tk()
fen_4.geometry("900x600")
fen_4.config(background="#FF8D34")

# création Frame 1, 2, 3, 4
F1 = Frame(fen_4, width=450, height=200, bg="blue", highlightthickness = 0, highlightbackground="red")
F2 = Frame(fen_4, width=450, height=200, bg="black", highlightthickness = 0, highlightbackground="red")
F3 = Frame(fen_4, width=900, height=300, bg="green", highlightthickness = 0, highlightbackground="red")
F4 = Frame(fen_4, width=900, height=100, bg="red", highlightthickness = 0, highlightbackground="red")

F1.place(x=0, y=0)
F2.place(x=450, y=0)
F3.place(x=0, y=200)
F4.place(x=0, y=500)



##F1 = Frame(fen_4, bg="blue", highlightthickness = 0, highlightbackground="red")
##F2 = Frame(fen_4, bg="green", highlightthickness = 0, highlightbackground="red")
##F3 = Frame(fen_4, bg="green", highlightthickness = 0, highlightbackground="red")
##F4 = Frame(fen_4, bg="red", highlightthickness = 0, highlightbackground="red")
##
##F1.place(x=100, y=100)
##F2.place(x=550, y=100)
##F3.place(x=400, y=300)
##F4.place(x=700, y=550)

####
### éléments dans frame 1
##bon_mot = Label(F1, text="Frame 1 : Le bon mot est : ")
##bon_mot.pack()
##
### éléments dans frame 2
##mot_res = Label(F2, text="Frame 2 : *test")
##mot_res.pack(side=RIGHT)
##
### éléments dans frame 3
##
##img = PhotoImage(file="bravo.png")
##imglabel = Label(F3, image=img)
##imglabel.grid()
##
### éléments dans frame 4
##recom = Button(F4, text="Frame 3 : Recommencer")
##recom.grid()
##

fen_4.mainloop()
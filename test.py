from tkinter import*

fen_4 = Tk()
fen_4.geometry("900x600")
fen_4.config(background="#FF8D34")

# création Frame 1, 2 et 3
F1 = Frame(fen_4, width=900, height=150, bg="blue", highlightthickness = 3, highlightbackground="red")
F2 = Frame(fen_4, width=900, height=380, bg="green", highlightthickness = 3, highlightbackground="red")
F3 = Frame(fen_4, width=900, height=100, bg="red", highlightthickness = 3, highlightbackground="red")

F1.place(x=0, y=0)
F2.place(x=0, y=150)
F3.place(x=0, y=500)


# éléments dans frame 1
bon_mot = Label(F1, text="Le bon mot est : ")
mot_res = Label(F1, text="*test")

bon_mot.grid(row=0, column=0)
mot_res.grid(row=0, column=1)


# éléments dans frame 2

img = PhotoImage(file="bravo.png")
imglabel = Label(F2, image=img)

imglabel.grid()

# éléments dans frame 3
recom = Button(F3, text="Recommencer")
recom.grid()


fen_4.mainloop()
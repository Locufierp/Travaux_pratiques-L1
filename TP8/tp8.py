from tkinter import *
import math

def tracer_rectangle(X, Y, couleur) :
    x1 = 1 + 10 * X
    y1 = 1 + 10 * Y
    x2 = x1 + 10
    y2 = y1 + 10
    ecran.create_rectangle(x1, y1, x2, y2, outline = couleurGrille, fill = couleur)

def tracer_ligne_verticale(X) :

def tracer_ligne_horizontale(Y) :
    pass
        
def tracer_ligne_oblique(x1, y1, x2, y2) :
    pass

def tracerAB() :
    pass

def initialiser_ecran() :
	for x in range(60):
		for y in range(80):
    			tracer_rectangle(x , y , couleurVide)

def placerA(event) :
    pass
    
def placerB(event) :
    pass

def d(x1, y1, x2, y2) :
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

def tracerC() :
    pass

# variables
xA = -1; yA = -1
xB = -1; yB = -1
couleurVide = 'white'
couleurGrille = 'grey'
couleurTraits = 'lightgrey'
couleurA = 'red'
couleurB = 'green'

# éléments graphiques
maFenetre = Tk()
maFenetre.geometry('1011x613')
maFenetre.resizable(height = False, width = False)
maFenetre.title("Prog - Algo L1 S1 - TP 8 - application de géométrie élémentaire")

ecran = Canvas(maFenetre, width = 801, height = 601, bg = 'white')
ecran.grid(row = 0, column = 0, padx = 5, pady = 5)

zoneDroite = Frame(maFenetre)
zoneDroite.grid(row = 0, column = 1, sticky = 'N')

BoutonTracerAB = Button(zoneDroite, width = 20, text = 'tracer (AB)', command = tracerAB)
BoutonTracerAB.grid(row = 0, column = 0, pady = 5, sticky = 'N')

BoutonTracerC = Button(zoneDroite, width = 20, text = 'tracer C(A, AB)', command = tracerC)
BoutonTracerC.grid(row = 1, column = 0, pady = 5, sticky = 'N')

BoutonEffacer = Button(zoneDroite, width = 20, text = 'effacer', command = initialiser_ecran)
BoutonEffacer.grid(row = 2, column = 0, pady = 5, sticky = 'N')

labelA = Label(zoneDroite, text = "A :", width = 20, fg = 'black', pady = 10, anchor = 'w')
labelA.grid(row = 3, column = 0, padx = 5)

labelB = Label(zoneDroite, text = "B :", width = 20, fg = 'black', pady = 10, anchor = 'w')
labelB.grid(row = 4, column = 0, padx = 5)

ecran.bind('<Button-1>', placerA)
ecran.bind('<Button-3>', placerB)

# lancement
initialiser_ecran()


# chargement de la fenêtre et mise en écoute des événements divers (ex : clic de souris)
maFenetre.mainloop()
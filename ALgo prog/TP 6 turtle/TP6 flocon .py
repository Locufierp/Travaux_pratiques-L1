import turtle
# la fonction r´e cursive qui trace un des 3 "cˆot´es" du flocon
def cote(n, c) :
    if n == 1 :
        t.forward(c)
    else :
        cote(n-1, c/4)
        t.left(90)
        cote(n-1, c/4)
        t.right(90)
        cote(n-1, c/4)
        t.right(90)
        cote(n-1, c/2)
        t.left(90)
        cote(n-1, c/4)
        t.left(90)
        cote(n-1, c/4)
        t.right(90)
        cote(n-1, c/4)
        
        
        
    
# programme principal
c = float(input("cˆot´e de base ? "))
n = int(input("quelle g´en´eration ? "))
t = turtle.Turtle()
t.up(); t.goto(-220, 100); t.down(); t.speed("fastest")

cote(n, c)
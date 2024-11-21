import turtle
"""
def spirale(n, c, a, coef):
    if n == 0 :
        t.down
        t.forward(c)
        t.up
        t.backward(c)
    else :
        t.forward(c)
        t.left(a)
        spirale(n-1,c* coef,a,coef)
"""
def spirale(n,c,a,coef):
    t.forward(c)
    if n > 1:
        t.left(a)
        spirale(n-1, c* coef , a , coef )
        
c = float(input("cˆot´e de base ? "))
n = int(input("quelle g´en´eration ? "))
a = int(input("quelle degre ? "))
coef = float(input("coef ? "))
t = turtle.Turtle()
t.up(); t.goto(-220, 100); t.down(); t.speed("fastest")

spirale(n, c, a, coef)


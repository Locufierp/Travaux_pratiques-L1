import turtle

def cercle(r) :
    t.up()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.down()
    t.circle(r)
    t.up()
    t.left(90)
    t.forward(r)
    t.right(90)
    t.down()
    
    
def generation(n, r, coef) :
    if n == 1:
        cercle(r)
    else:
        cercle(r)
        t.up()
        t.forward(r+r*coef)
        t.down()
        generation(n-1,r*coef,coef)


r = float(input("rayon de base ? "))
n = int(input("quelle g´en´eration ? "))
coef = float(input("coef ? "))
t = turtle.Turtle()
t.up(); t.goto(-300, 100); t.down(); t.speed("fastest")

generation(n, r, coef)
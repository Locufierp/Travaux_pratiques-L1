import turtle

def botanique(n,l, a, coef):
    if n == 0 :
        t.forward(n)
        t.backward(n)
    else :
        t.forward(n)
        botanique(n-1,l*coef,a,coef)
        t.right(2*a)
        botanique(n-1,l*coef,a,coef)
        t.left(a)
        t.backward(n)
        

l = float(input("cˆot´e de base ? "))
n = int(input("quelle g´en´eration ? "))
a = int(input("quelle degre ? "))
coef = float(input("coef ? "))
t = turtle.Turtle()
t.up(); t.goto(-220, 100); t.down(); t.speed("fastest"),left(90)

botanique(n,l , a , coef )
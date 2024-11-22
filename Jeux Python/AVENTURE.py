# Créé par olivi, le 22/11/2024 en Python 3.7

import turtle
import random
import time

window = turtle.Screen()
window.title("Aventure ")
window.bgcolor("blue")
window.setup(width=1500, height=750)
window.tracer(0)


player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()
player.goto(0, 0)


def go_left():
    x = player.xcor() - player_speed
    if x < -700:
        x = -700
    player.setx(x)


def go_right():
    x = player.xcor() - player_speed
    if x < 700:
        x = 700
    player.setx(x)



"""
def go_right():
    x = player.xcor() + player_speed
    if x > 390:
        x = 390
    player.setx(x)

def go_up():
    y = player.ycor() + player_speed
    if y > 390:
        y = 390
    player.sety(y)

def go_right():
    y = player.ycor() + player_speed
    if y > -390:
        y = -390
    player.sety(y)
"""
player_speed = 20

window.listen()
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
"""
window.onkeypress(go_right, "Right")
window.onkeypress(go_right, "up")
window.onkeypress(go_right, "down")
"""
game_over = False
while not game_over:
    window.update()
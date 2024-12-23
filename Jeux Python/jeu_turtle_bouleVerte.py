# Créé par olivi, le 22/11/2024 en Python 3.7

import turtle
import random
import time

window = turtle.Screen()
window.title("bouffe la boule verte")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.goto(0, -250)

score = 0

bestscore = 0



score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

bestscore_display = turtle.Turtle()
bestscore_display.speed(0)
bestscore_display.color("white")
bestscore_display.penup()
bestscore_display.hideturtle()
bestscore_display.goto(250, 260)
bestscore_display.write(f"Best Score: {bestscore}", align="center", font=("Arial", 18, "normal"))


def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))


def update_bestscore():
    global score
    bestscore = score > score + 1
    bestscore_display.clear()
    bestscore_display.write(f"Best Score: {bestscore}", align="center", font=("Arial", 18, "normal"))


player_speed = 20

bonuss = []
for _ in range(1):
    bonus = turtle.Turtle()
    bonus.shape("circle")
    bonus.color("green")
    bonus.penup()
    bonus.speed(0)
    bonus.goto(random.randint(-390, 390), random.randint(100, 300))
    bonuss.append(bonus)
bonus_speed =   1


obstacles = []
for _ in range(6):
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-390, 390), random.randint(100, 300))
    obstacles.append(obstacle)


obstacle_speed = 1


def go_left():
    x = player.xcor() - player_speed
    if x < -390:
        x = -390
    player.setx(x)

def go_right():
    x = player.xcor() + player_speed
    if x > 390:
        x = 390
    player.setx(x)


window.listen()
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")


game_over = False
while not game_over:
    window.update()

    for obstacle in obstacles:
        y = obstacle.ycor() - obstacle_speed
        if y < -300:
            y = random.randint(300, 300)
            obstacle.setx(random.randint(-390, 390))
        obstacle.sety(y)


        if player.distance(obstacle) < 20:
            game_over = True
            print("Game Over!")

    for bonus in bonuss[:]:  # Utilisation d'une copie pour éviter des erreurs lors de la suppression
        y = bonus.ycor() - bonus_speed
        if y < -300:  # Si le bonus sort de l'écran
            y = random.randint(300, 300)  # Remettre le bonus en haut
            bonus.setx(random.randint(-390, 390))
        bonus.sety(y)

        # Détection de collision avec le joueur
        if player.distance(bonus) < 20:
            bonus.goto(random.randint(-390, 390), random.randint(300, 400))  # Réapparaît en haut
            update_score()  # Mettre à jour le score






# Affichage du message de fin
end_message = turtle.Turtle()
end_message.color("white")
end_message.penup()
end_message.hideturtle()
end_message.write("Game Over!", align="center", font=("Arial", 24, "normal"))

# Fermer la fenêtre sur clic
window.mainloop()

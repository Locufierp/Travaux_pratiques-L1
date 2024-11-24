
# Créé par olivi, le 23/11/2024 en Python 3.7

import turtle

# Constants for screen size
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750
HALF_WIDTH = SCREEN_WIDTH // 2
HALF_HEIGHT = SCREEN_HEIGHT // 2

# Player speed
PLAYER_SPEED = 20

# Setup the initial screen
def create_screen():
    screen = turtle.Screen()
    screen.title("Aventure")
    screen.bgcolor("blue")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    return screen

window = create_screen()

# Create the player
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()
player.goto(0, 0)

# Movement functions
def go_left():
    player.setx(player.xcor() - PLAYER_SPEED)

def go_right():
    player.setx(player.xcor() + PLAYER_SPEED)

def go_up():
    player.sety(player.ycor() + PLAYER_SPEED)

def go_down():
    player.sety(player.ycor() - PLAYER_SPEED)

# Check if the player is out of bounds and create a new screen
def check_bounds():
    global window
    x, y = player.xcor(), player.ycor()

    # If out of bounds, recreate the screen
    if x < -HALF_WIDTH:  # Left exit
        recreate_screen(HALF_WIDTH - PLAYER_SPEED, y)
    elif x > HALF_WIDTH:  # Right exit
        recreate_screen(-HALF_WIDTH + PLAYER_SPEED, y)
    elif y > HALF_HEIGHT:  # Top exit
        recreate_screen(x, -HALF_HEIGHT + PLAYER_SPEED)
    elif y < -HALF_HEIGHT:  # Bottom exit
        recreate_screen(x, HALF_HEIGHT - PLAYER_SPEED)

# Function to recreate the screen
def recreate_screen(new_x, new_y):
    global window
    window.clear()  # Clear the current screen
    window.bye()    # Close the current screen
    window = create_screen()  # Create a new screen
    window.listen()  # Set up key listeners
    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")
    window.onkeypress(go_up, "Up")
    window.onkeypress(go_down, "Down")
    player.goto(0, 0)  # Position the player on the new screen

# Keyboard bindings
window.listen()
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")

# Game loop
game_over = False
while not game_over:
    window.update()
    check_bounds()

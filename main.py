import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("lightblue")
drawing_board.title("Catch The Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(1.5, 1.5, 2)
turtle.tracer(False)

counter=0
time_counter=20
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-30, 360)
score_writer.write(f"Sayaç: {counter}", font=("Arial", 20, "bold"))

time_writer = turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(-30, 320)
time_writer.write(f"Time: {time_counter}", font=("Arial", 20, "bold"))

game_over_writer = turtle.Turtle()
game_over_writer.hideturtle()

def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle_instance.penup()
    turtle_instance.goto(x, y)
    turtle.update()

def update_score():
    global counter
    counter += 1
    score_writer.clear()
    score_writer.write(f"Sayaç: {counter}", font=("Arial", 20, "bold"))

def update_time():
    time_writer.clear()
    time_writer.write(f"Time: {time_counter}", font=("Arial", 20, "bold"))

def countdown():
    global time_counter
    if time_counter > 0:
        time_counter -= 1
        update_time()
        drawing_board.ontimer(countdown, 1000)
    else:
        end_game()

def hideTurtle(x, y):
    if(time_counter > 0):
        turtle_instance.hideturtle()
        update_score()
        move_turtle()
        turtle_instance.showturtle()
        turtle.update()

def move_turtle_periodic():
    if time_counter > 0:  # süre bitmediyse
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle_instance.goto(x, y)
        turtle.update()
        drawing_board.ontimer(move_turtle_periodic, 1000)

def end_game():
    turtle_instance.hideturtle()
    game_over_writer.goto(0, 0)
    game_over_writer.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
    turtle.update()

move_turtle()
turtle.update()

turtle_instance.onclick(hideTurtle)

countdown()              # 1 saniyelik sayaç
move_turtle_periodic()

turtle.done()
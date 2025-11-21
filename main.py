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
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-30, 360)
score_writer.write(f"Sayaç: {counter}", font=("Arial", 20, "bold"))

time_writer = turtle.Turtle()
time_writer.hideturtle()
time_writer.penup()
time_writer.goto(-30, 320)
time_writer.write("Time: 0", font=("Arial", 20, "bold"))

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


def hideTurtle(x, y):
    turtle_instance.hideturtle()
    update_score()
    move_turtle()
    turtle_instance.showturtle()
    turtle.update()


move_turtle()

turtle_instance.onclick(hideTurtle)

turtle.done()
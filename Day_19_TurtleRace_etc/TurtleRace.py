import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=510, height=400)
screen.title("Welcome to the Daytona 500 Turtle Race!")
user_bet = screen.textinput("Turtle Race Day!", "Choose a contestant (Color): ").lower()

race_turtles = []
colors = ["red", "black", "blue", "purple", "orange", "green", "magenta"]
y_pos = [-150, -100, -50, 0, 50, 100, 150]


for turtle_index in range(0, 7):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.setposition(-230, y_pos[turtle_index])
    race_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for race_turtle in race_turtles:
        turtle_movement = random.randint(0, 10)
        race_turtle.forward(turtle_movement)
        if race_turtle.xcor() > 230:
            is_race_on = False
            turtle_winner = race_turtle.pencolor()
            if turtle_winner == user_bet:
                print(f"{turtle_winner.capitalize()} is the winner! You've won! :) ")
            else:
                print(f"{turtle_winner.capitalize()} is the winner! You've Lost.. :( ")


screen.exitonclick()


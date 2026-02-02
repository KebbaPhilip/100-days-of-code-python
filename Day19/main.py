from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a colour: ")

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-70, -40, -10, 20, 50, 80]

for turtle in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle] )
    all_turtles.append(new_turtle)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")

        random_distance = random.randint(1, 10)
        turtle.fd(random_distance)




screen.exitonclick()
from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        random_x = randint(-285, 285)
        random_y = randint(-285, 285)
        self.goto(random_x, random_y)





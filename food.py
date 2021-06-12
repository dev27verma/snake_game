from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        new_x = randint(-290,290)
        new_y = randint(-290,290)
        self.goto(new_x,new_y)
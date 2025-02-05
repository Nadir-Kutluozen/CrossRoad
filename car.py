import random
import turtle
from turtle import Turtle
from random import Random, randint
COLORS = ["#181e47","#25591a", "#660f62", "#8f253c","#997405","#ffffff", "#040a24" , "#5272ff", "#5272ff"]

def random_number_gen():
    return randint(-300, 320) + 5

class Car():
    def __init__(self):
        self.cars = []
    def create_car(self, level):
        ran_num = randint(1,6)
        if ran_num == 1:
            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            turtle.setposition(300, random_number_gen())
            turtle.shape("square")
            turtle.color(random.choice(COLORS))
            turtle.setheading(180)
            turtle.shapesize(2, 3)
            turtle.showturtle()
            self.cars.append(turtle)
        else:
            pass

    def move_left(self):
        for car in self.cars:
            car.forward(20)












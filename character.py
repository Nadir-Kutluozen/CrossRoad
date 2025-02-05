from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("#02520f")
        self.penup()
        self.goto(0,-320)
        self.setheading(90)
        self.shapesize(2)
        self.showturtle()


    def move_up(self):
        self.forward(20)

    def go_back(self):
        self.goto(0, -320)











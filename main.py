import time
from random import random, randint
from turtle  import Turtle, Screen

from car import Car
from character import Character

#screen that will be used for the game
screen = Screen()
screen.title("Cross Road")
screen.bgcolor("#f7b5ab")
screen.setup(500,700)
screen.listen()
screen.tracer(0)

turtle = Character()
game_is_on = True

a_car = Car()

#code goes here
 #initilzaing the car obj

screen.onkey(turtle.move_up,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    a_car.create_car()
    a_car.move_left()


    for car in a_car.cars:
        if car.distance(turtle) < 40:
            game_is_on = False
            print("gamer is over")
            #display game over

    if turtle.ycor() > 340:
        turtle.go_back()

        #level up and make the car faster each time




# cars pass
# if collapse:stop game, gameover, start from zero again
# if reach top: score++, reset pos, car goes faster


screen.exitonclick()




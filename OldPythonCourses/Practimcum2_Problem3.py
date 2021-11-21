# Question 3

import turtle
import random

runner = turtle.Turtle()
def move(x,y):
    direction = random.randint(1, 2)
    if direction == 1:
        runner.left(90)
    else:
        runner.right(90)
    runner.forward(50)

turtle.onscreenclick(move)

# -----------------------------------------
# Gage Hilyard
# CSCI 107, Assignment 3                   
# Last Updated: September 21, 2018
# -----------------------------------------
# Draws a Voltorb   
# -----------------------------------------

import turtle
import math

window = turtle.Screen()
window.bgcolor("green")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

#draws body
pen.pu()
pen.fillcolor("red")
pen.begin_fill()
pen.goto(0,-100)
pen.pd()
pen.circle(100)
pen.end_fill()

#draws bottom
pen.pu()
pen.goto(-100,0)
pen.seth(270)
pen.fillcolor("white")
pen.begin_fill()
pen.pd()
pen.circle(100,180)
pen.end_fill()
pen.seth(0)
pen.back(200)

#draws left eye
a=25
b=60
c= math.sqrt((a**2)+(b**2))
pen.pu()
pen.goto(-65,35)
pen.pd()
pen.fillcolor("white")
pen.begin_fill()
pen.right(25)
pen.forward(c)
pen.right(155)
pen.forward(b)
pen.right(90)
pen.forward(a)
pen.end_fill()

pen.pu()
pen.back(a)
pen.right(90)
pen.forward(b/2)
pen.left(90)
pen.fillcolor("black")
pen.pd()
pen.begin_fill()
pen.forward(10)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(5)
pen.end_fill()

#draws right eye
pen.pu()
pen.goto(65,35)
pen.pd()
pen.fillcolor("white")
pen.begin_fill()
pen.left(25)
pen.forward(c)
pen.left(155)
pen.forward(b)
pen.left(90)
pen.forward(a)
pen.end_fill()

pen.pu()
pen.backward(a)
pen.right(90)
pen.back(b/2)
pen.right(90)
pen.fillcolor("black")
pen.pd()
pen.begin_fill()
pen.backward(10)
pen.left(90)
pen.backward(5)
pen.left(90)
pen.backward(10)
pen.left(90)
pen.backward(5)
pen.end_fill()


window.exitonclick()

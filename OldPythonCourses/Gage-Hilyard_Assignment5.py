# -----------------------------------------
# Gage Hilyard                               
# CSCI 107, Assignment 5                   
# Last Updated: October 10, 2018                   
# -----------------------------------------
# Draws a Minecraft picture   
# -----------------------------------------

import turtle

tileSize = 40

window = turtle.Screen()
window.bgcolor("blue")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def drawSquare(x,y,fill,color):
    pen.pu()
    pen.fillcolor(fill)
    pen.pencolor(color)
    pen.begin_fill()
    pen.goto(x,y)
    pen.pd()
    for i in range(4):
        pen.forward(tileSize)
        pen.right(90)
    pen.end_fill()

def drawLeaves(x,y):
    drawSquare(x,y,"green","black")
    #draws smaller squares without using drawSquare function
    for i in range(2,4):
        pen.pu()
        pen.goto(x+tileSize/i,y-tileSize/i)
        pen.fillcolor("white")
        pen.pencolor("white")
        pen.pd()
        pen.begin_fill()
        for i in range(4):
            pen.forward(tileSize/8)
            pen.right(90)
        pen.end_fill()

#draws trunk
for i in range(4):
    drawSquare(tileSize,tileSize*i,"brown","black")

#draws first row of leaves
for i in range(-1,4):
    drawLeaves(tileSize*i,tileSize*4)
#draws second row of leaves
for i in range(-1,4):
    drawLeaves(tileSize*i,tileSize*5)
#draws thrid row of leaves
for i in range(0,3):
    drawLeaves(tileSize*i,tileSize*6)
#draws fourth row of leaves
for i in range(0,3):
    drawLeaves(tileSize*i,tileSize*7)
window.exitonclick()

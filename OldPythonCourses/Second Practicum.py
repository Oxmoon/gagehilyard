# Second Practicum
# Question 1

##import turtle
##import time
##window = turtle.Screen()
##polygon = turtle.Turtle()
##
##for side in range(10):
##    polygon.forward(25)
##    polygon.left(360/10)
##    time.sleep(0.1)

#Question 2

##def november_2018_holiday(day):
##    if day == 6 or day == 12 or day == 21 or day == 22 or day == 23:
##        return "true"
##    else:
##        return "false"
##
##for i in range(1,31):
##    print(i, november_2018_holiday(i))

# Question 3

import turtle

drawing = turtle.Turtle()
drawing.hideturtle()
drawing.speed(0)

def draw_triangle(triangle, top_x, top_y, side_length, triangle_color):
    triangle.penup()
    triangle.goto(top_x, top_y)
    triangle.pendown()
    triangle.pencolor("black")
    triangle.fillcolor(triangle_color)
    triangle.begin_fill()
    triangle.setheading(-60)
    for side in range(3):
        triangle.forward(side_length)
        triangle.right(120)
    triangle.end_fill()

def draw_row(turtle, x, y, side_length, number, color):
    for i in range(1, number):
        draw_triangle(turtle, x+(i*side_length), y, side_length, color)

draw_row(drawing, -150, 0, 30, 10, "orange")

draw_row(drawing, -135, 26, 30, 9, "red")

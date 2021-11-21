# Question 1
import turtle

def draw_circle(my_turtle, x, y, diameter, dot_color):
    my_turtle.hideturtle()
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.dot(diameter, dot_color)

circle = turtle.Turtle()
draw_circle(circle, 0, 0, 50, "red")
draw_circle(circle, -100, 200, 75, "blue")

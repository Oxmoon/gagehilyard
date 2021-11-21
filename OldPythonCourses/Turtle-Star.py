import turtle


size = int(input("Enter pen size: "))
turtle_color = input("Enter the turtle color: ")
window_color = input("Enter the window color: ")

window = turtle.Screen()
window.bgcolor(window_color)

points = 5
angle = 180 - (180/points)

star = turtle.Turtle()
star.hideturtle()
star.pensize(size)
star.color(turtle_color)
star.goto(-50,0)

for i in range(points) :
    star.forward(100)
    star.right(angle)

window.exitonclick()

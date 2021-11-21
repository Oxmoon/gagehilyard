import turtle

sides = int(input("Enter the number of sides of the polygon: "))
length = int(input("Enter the length of the side of a polygon: "))
shape_color = input("Enter the fill color of the polygon: ")

window = turtle.Screen()

polygon = turtle.Turtle()
polygon.hideturtle()
polygon.color(shape_color)
polygon.fillcolor(shape_color)

total_angle = (sides - 2) * 180

polygon.begin_fill()
for side in range(sides):
    print(x)
    polygon.forward(length)
    polygon.right(180 - total_angle /sides)
polygon.end_fill()

window.exitonclick()

# Question 1
##number_asterisks = int(input("Enter the number of asterisks: "))
##asterisks = "*" * number_asterisks
##print(asterisks)

# Question 2

import turtle

length = int(input("Enter an even interger between 50 and 500: "))

window = turtle.Screen()
window.bgcolor("gold")

plus = turtle.Turtle()
plus.hideturtle()
plus.pensize(20)
plus.color("blue")

plus.backward(length/2)
plus.forward(length)
plus.backward(length/2)
plus.left(90)
plus.forward(length/2)
plus.backward(length)

window.exitonclick()

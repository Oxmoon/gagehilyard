# Practicum Question 1

##number = input("Enter an interger from 1 to 9: ")
##number = int(number)
##
##for i in range(1, number+1):
##    print(str(i).rjust(i))

# Practicum Question 2

##import turtle
##
##legs = input("Enter number of legs: ")
##legs = int(legs)
##
##sprite = turtle.Turtle()
##window = turtle.Screen()
##sprite.hideturtle()
##sprite.color("green")
##
##for leg in range(legs):
##    sprite.forward(20)
##    sprite.backward(20)
##    sprite.left(360/legs)
##
##window.exitonclick()

# Practicum Question 3

##a = float(input("Enter a: "))
##b = float(input("Enter b: "))
##
##x = -b/a
##
##print("The equation ax + b = 0 when x=", x)

# Class Activity

name = input("Enter name: ")
width = int(input("Enter the field width: "))

dashes = ""
for i in range(width - 4):
    dashes = dashes + "-"

banner = "+ " +dashes +" +"
name_line = "|"+name.center(width-2)+"|"
print(banner)
print(name_line)
print(banner)

# or you could do [ "-" * (width-4) ] instead of a for loop

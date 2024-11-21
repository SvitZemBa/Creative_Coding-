import turtle
import math
import random

colors = ["blue", "green", "red"]

turtle.speed(0)

#for step in colors:
#    print(step)
#    turtle.color(step)
#    turtle.forward(70)
#    turtle.left(120)

turtle.forward(120)
turtle.left(300)
turtle.forward(70)
turtle.left(120)
turtle.forward(50)

for step in range (5):
    turtle.forward(120)
    turtle.left(300)
    turtle.forward(70)
    turtle.left(120)
    turtle.forward(50)     

step_count = 0
while step_count < 5:
    turtle.forward(25)
    turtle.forward(15)
    angle = step_count * 13
    turtle.left(angle)
    print(angle)
    step_count += 1

turtle.exitonclick()
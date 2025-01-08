import turtle as tu
import random as ra

def draw_circle (diameter):
    tu.pendown()
    tu.color(ra.random(), ra.random(), ra.random())
    tu.circle(diameter/2)
    tu.penup()

def draw_sierpinski(diameter, depth):
    if depth ==0:
        draw_circle(diameter)
    else:
        diameter *=0.5
        depth -= 1
        for i in range(3):
            draw_sierpinski(diameter, depth)
            if i == 0:
                tu.left(60)
                tu.forward(diameter)
                tu.right(60)
            elif i == 1:
                tu.right(60)
                tu.forward(diameter)
                tu.left(60)
            else:
                tu.right(180)
                tu.forward(diameter)
                tu.right(180)
tu.speed(0)
tu.bgcolor(0,0,0)
draw_sierpinski(400,5)
tu.exitonclick()

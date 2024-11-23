import turtle as tu
import random as ra

tu.bgcolor(0, 0, 0)
tu.speed("fast")
tu.pensize(3)
tu.color(1, 1, 1)

def maybe_change_color ():
    tu.color(ra.random(), ra.random(), ra.random())

def go_up ():
    tu.setheading(90)
tu.onkey (go_up,"w")
tu.onkey (go_up, "Up")

def go_left ():
    tu.setheading(180)
tu.onkey (go_left,"a")
tu.onkey (go_left, "Left")

def go_right ():
    tu.setheading(0)
tu.onkey (go_right,"d")
tu.onkey (go_right,"Right")

def go_down ():
    tu.setheading(270)
tu.onkey (go_down,"s")
tu.onkey (go_down,"Down")

def go_ontimer ():
    tu.forward(20)
    tu.ontimer(go_ontimer,1000)
    maybe_change_color ()
tu.ontimer(go_ontimer,1000)

tu.listen()
tu.mainloop()
tu.exitonclick()


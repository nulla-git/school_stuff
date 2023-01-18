# Blake Reneau 17/1/2023
# example of turtle listening for events

import turtle
import random

Xpos = 0
Ypos = 0
tim = turtle.Turtle()
tim.speed(1)
tim.circle(45)
tim.penup()
tim.setheading(270)
tim.setpos(((Xpos + 45), (Ypos + 45)))
tim.pendown()
tim.forward(45)
tim.left(90)
tim.circle(60, 180)
tim.forward(80)
tim.circle(60, 90)
tim.forward(30)
tim.circle(60, 90)
tim.forward(60)

def up():
    tim.clear()
    tim.penup()
    Xpos = 0
    Ypos = 0
    Ypos += 50
    tim.setpos(((Xpos), (Ypos)))
    tim.pendown()
    tim.circle(45)
    tim.penup()
    tim.setpos(((Xpos + 45), (Ypos + 45)))
    tim.pendown()
    tim.setheading(270)
    tim.pendown()
    tim.forward(45)
    tim.left(90)
    tim.circle(60, 180)
    tim.forward(80)
    tim.circle(60, 90)
    tim.forward(30)
    tim.circle(60, 90)
    tim.forward(60)

turtle.listen()
turtle.onkey(up, "Up")


turtle.mainloop()




# Blake Reneau 01/19/23
# drawing a snowflake with turtle

import turtle
from turtle import *
import random

j = turtle.Turtle()
j.speed(9)
snowflakes = 0

while snowflakes <= 10:
    snowflakes += 1
    flakeShape = random.randrange(0,3)
    xPos = random.randrange(0, 201)
    yPos = random.randrange(0, 201)
    j.penup()
    j.setpos(xPos, yPos)
    if flakeShape == 0:
        inc_1 = 0
        j.penup()
        j.forward(100)
        j.left(90)
        j.pendown()
        j.circle(100)
        j.penup()
        j.setpos(xPos, yPos)
        j.pendown()
        while inc_1 < 8:
            inc_1 += 1
            j.forward(100)
            j.back(50)
            j.right(22.5)
            j.forward(50)
            j.back(50)
            j.right(135)
            j.forward(50)
            j.back(50)
            j.right(45)
            j.forward(50)
            j.back(50)
            j.right(135)
            j.forward(50)
            j.back(50)
            j.setpos(xPos, yPos)
            j.left(22.5)

        j.right(22.5)

        inc_2 = 0
        while inc_2 < 8:
            inc_2 += 1
            j.forward(100)
            j.back(100)
            j.right(45)

        j.setpos(xPos, yPos)
        j.setheading(0)
        j.forward(50)
        j.left(90)
        j.circle(50)
    else: flakeShape > 0
    break
#working on this...
'''    elif flakeShape == 1:
        inc_1 = 0
        j.penup()
        j.forward(100)
        j.left(90)
        j.pendown()
        j.circle(100)
        j.penup()
        j.setpos(xPos, yPos)
        j.forward(50)
        j.right(90)
        j.circle(50)
'''













input()

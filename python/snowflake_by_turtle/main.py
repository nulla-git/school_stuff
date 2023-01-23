# Blake Reneau 01/19/23
# drawing a snowflake with turtle

import math
import turtle
from turtle import *
import random

j = turtle.Turtle()
j.speed(-50)
snowflakes = 0

while snowflakes <= 19:
    snowflakes += 1
    flakeShape = random.randrange(0,3)
    print(flakeShape)
    xPos = random.randrange(-200, 201)
    yPos = random.randrange(-200, 201)
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
        continue
    elif flakeShape == 1:
        inc_1 = 0
        j.penup()
        j.setheading(90)
        j.forward(100)
        j.left(90)
        j.pendown()
        j.circle(100)
        j.penup()
        j.setpos(xPos, yPos)
        j.forward(50)
        j.left(90)
        j.pendown()
        j.circle(50)
        j.right(90)
        j.penup()
        j.forward(50)
        j.right(135)
        j.pendown()
        j.forward(140)
        for x in range(0, 3):
            j.right(90)
            j.forward(140)
        j.setheading(0)
        j.forward(200)
        j.back(100)
        for x in range(0, 8):
            j.right(45)
            j.forward(100)
            j.back(100)
        continue
    else: flakeShape == 2
    for h in range(0, 4):
        j.pendown()
        j.forward(100)
        for i in range(0, 4):
            j.circle(20)
            j.circle(-20)
            j.back(25)
        j.right(90)
    j.forward(100)
    j.right(135)
    for g in range(0, 4):
        j.forward(math.sqrt(20000))
        j.right(90)
    continue

input()

# Blake Reneau 1/11/23
# random shape generator with turtle
import turtle
import random

colors = ["red", "blue", "yellow", "green", "orange", "black"]

circler = turtle.Turtle()
rand_drawer = turtle.Turtle()
rand_drawer.pensize(5)

# just goofin around here
circler.pensize(5)
circler.color("green", "red")
circler.begin_fill()
circler.circle(50)
circler.end_fill()

rand_drawer.speed(0)

for x in range(5):
    randColor = random.randrange(0, len(colors))
    rand_drawer.penup()
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    rand_drawer.color(colors[randColor], colors[random.randrange(0, len(colors))])
#0 is square, 1 is triangle, 2 is circle
    shape = random.randrange(0, 3)
    rand_drawer.setpos((rand1, rand2))
    if shape == 0:
        rand_drawer.pendown()
        rand_drawer.begin_fill()
        rand_drawer.setheading(90)
        rand_drawer.forward(50)
        rand_drawer.left(90)
        rand_drawer.forward(50)
        rand_drawer.left(90)
        rand_drawer.forward(50)
        rand_drawer.left(90)
        rand_drawer.forward(50)
        rand_drawer.end_fill()
    if shape == 1:
        rand_drawer.pendown()
        rand_drawer.begin_fill()
        rand_drawer.setheading(0)
        rand_drawer.forward(30)
        rand_drawer.left(135)
        rand_drawer.forward(40)
        rand_drawer.left(135)
        rand_drawer.forward(25)
        rand_drawer.end_fill()
    if shape == 2:
        rand_drawer.pendown()
        rand_drawer.begin_fill()
        rand_drawer.circle(50)
        rand_drawer.end_fill()


input()

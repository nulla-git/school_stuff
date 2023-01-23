import turtle

myPen = turtle.Turtle()

myPen.speed(50)

myPen.color("teal")

myPen.left(90)

for i in range (0,8):
    myPen.forward(100)
    for j in range (0, 4):
        myPen.circle(5-j)
        myPen.circle(-5+j)
        myPen.forward(-20)

    myPen.forward(-20)
    myPen.left(45)


myPen.color("turquoise")
myPen.forward(-20)
myPen.right(90)
myPen.circle(20)
myPen.left(90)
myPen.forward(20)
myPen.left(22.5)

for i in range (0,8):
    myPen.forward(140)
    for j in range (0,6):
        myPen.circle(10-j)
        myPen.circle(-10+j)
        myPen.forward(-20)
    myPen.forward(-20)
    myPen.left(45)

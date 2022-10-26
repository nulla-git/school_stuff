#Blake Reneau 10/26/2022
#triangle perimeter calculator using classes (why?)

class Sides:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calc(self):
        total = self.side1 + self.side2 + self.side3
        return total

sides = Sides(5, 10, 15)

perimeter = sides.calc()

print("The area of the triangle is " + str(perimeter) + " centimeters")

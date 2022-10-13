#Blake Reneau 10/13/2022
#example of how functions/subroutines can be used.

def add(foo):
    total = foo + 5
    print(total)

def sub(foo):
    total = foo - 5
    print(total)

def mult(foo):
    total = foo * 5
    print(total)

def div(foo):
    total = foo / 5
    print(total)

choice = int(input("Input 1 to add a number to 5, 2 to subtract 5 from, 3 to multiply by five, or 4  to divide five (use any other number to quit): "))
i = 0

while 5 > choice > 0:
    i += 1
    if i > 1:
        choice = int(input("Input 1 to add a number to 5, 2 to subtract 5 from, 3 to multiply by five, or 4  to divide five (use any other number to quit): "))
    number = int(input("number to use? "))
    if choice == 1:
        add(number)
        continue
    elif choice == 2:
        sub(number)
        continue
    elif choice == 3:
         mult(number)
         continue
    elif choice == 4:
        div(number)
        continue
    else: 5 > choice > 0
    break

#Blake Reneau 10/13/2022
#example of how functions/subroutines can be used.

def add(foo,bar):
    total = foo + bar
    print(total)

def sub(foo,bar):
    total = foo - bar
    print(total)

def mult(foo,bar):
    total = foo * bar
    print(total)

def div(foo,bar):
    total = foo / bar
    print(total)

choice = int(input("Input 1 to add two numbers, 2 to subtract 2 numbers, 3 to multiply by two numbers, or 4 to divide two numbers (use any other number to quit): "))
i = 0

while 5 > choice > 0:
    i += 1
    if i > 1:
        choice = int(input("Input 1 to add two numbers, 2 to subtract 2 numbers, 3 to multiply by two numbers, or 4 to divide two numbers (use any other number to quit): "))
    number1 = int(input("1st number to use: "))
    number2 = int(input("2nd number to use: "))
    if choice == 1:
        add(number1,number2)
        continue
    elif choice == 2:
        sub(number1,number2)
        continue
    elif choice == 3:
         mult(number1,number2)
         continue
    elif choice == 4:
        div(number1,number2)
        continue
    else: 5 > choice > 0
    break

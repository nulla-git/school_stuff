# 11/29/22 Blake Reneau
# Ask the user for three numbers and return the smallest and largest value.

num1 = int(input("I need a number: "))
num2 = int(input("and another... : "))
num3 = int(input("and another... : "))

numbers = []
numbers.insert(0, num1)
numbers.insert(0, num2)
numbers.insert(0, num3)
numbers.sort()

print("the smallest number is " + str(numbers[0]) )
print("the middle number is " + str(numbers[1]) )
print("the largest number is " + str(numbers[2]) )

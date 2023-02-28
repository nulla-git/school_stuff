# Blake Reneau 2/27/23
# random times table quiz
import os
import random
from fractions import Fraction

# I don't neeeeed this it's just a nicety
os.system('clear')

i = 0
correctCount = 0
questions = int(input("how many questions?  "))
answer = 0

while i < questions:
    i += 1
    #question type
    qtype = random.randrange(0, 4)
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)

    if qtype == 0:
        correct = num1 + num2
        answer = int(input("what is " + str(num1) + " plus " + str(num2) + "? "))
    if qtype == 1:
        correct = num1 - num2
        answer = float(input("what is " + str(num1) + " minus " + str(num2) + "? "))
    if qtype == 2:
        correct = num1 * num2
        answer = int(input("what is " + str(num1) + " times " + str(num2) + "? "))
    if qtype == 3:
        correct = num1 / num2
        answer = (input("what is " + str(num1) + " divided by " + str(num2) + "? "))
        #cheat if you want lol
        answer = Fraction(answer)
        answer = float(answer)

    if answer == correct:
        print("correct!")
        correctCount += 1
    if answer != correct:
       print("incorrect!")

score = (correctCount / questions)
print("test score: " + str(score))


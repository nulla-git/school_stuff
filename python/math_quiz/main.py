# Blake Reneau 2/24/23
# random times table quiz
import os
import random

os.system('clear')

i = 0
correctCount = 0
questions = int(input("how many questions?  "))


while i < questions:
    i += 1
    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    correct = num1 * num2
    answer = int(input("what is " + str(num1) + " times " + str(num2) + "? "))

    if answer == correct:
        print("correct!")
        correctCount += 1
    if answer != correct:
       print("incorrect!")

score = (correctCount / questions)
print("test score: " + str(score))


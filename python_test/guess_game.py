#Blake Reneau 12/05
#simple guessing game
import random

number = (random.randrange(1,20))

while True:
    guess = int(input("guess the number: "))
    if guess > number:
        print("too high!")
    if guess < number:
        print("too low!")
    if guess == number:
        print("you win!")
        break

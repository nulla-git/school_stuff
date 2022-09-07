number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is? "))

if guess < number:
     print("Never mind")
if guess > number:
     print("Never mind")
if guess == number:
     print("Well done")
if guess != number:
     print("Bad luck")

#Blake Reneau 3/6/2023
#Quote of the day program
import random
import os

os.system('clear')
question_type = random.randrange(0, 4)
num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
quotes = open("quotes.txt", "r")
with quotes as fp:
    #value of variable is equal to the amount of lines, of which each line
    #has a value of one.
    num_lines = sum(1 for line in fp)
quotes = open("quotes.txt", "r")
print(num_lines)
quote_pick = random.randrange(0, num_lines)
print(quote_pick)

print(quotes.readlines()[8])

print("####################")
print("# Quote of the day #")
print("####################")
print(quotes.readlines()[quote_pick])
quotes.close

print("###########################")
print("# Spanish word of the day #")
print("###########################")
words = open("spanish_words.txt", "r")
print(words.readlines()[quote_pick])
words.close

print("########################")
print("# Daily Math Challenge #")
print("########################")

if question_type == 0:
    print(str(num1) + "+" + str(num2) + "?")
elif question_type == 1:
    print(str(num1) + "-" + str(num2) + "?")
elif question_type == 2:
    print(str(num1) + "*" + str(num2) + "?")
elif question_type == 3:
    print(str(num1) + "/" + str(num2) + "?")

print("########################")
print("# Add Your Own Quote   #")
print("########################")
append_text = input("Input Here: ")
quote_append = open("quotes.txt", "a")
quote_append.write("\n")
quote_append.write(append_text)
quote_append.close





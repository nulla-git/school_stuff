# Blake Reneau 04/03/23
# random quiz over goal totals
import random

goal_list = open("goals.txt", "r")
countries = []

for line in goal_list:
    rawData = line.split(";")
    country = rawData[1]
    if country not in countries:
        countries.append(country)

goal_list.close()

print(countries)
country1 = random.choice(countries)
country2 = random.choice(countries)
country1_goals = 0
country2_goals = 0

goal_list = open("goals.txt", "r")

for lines in goal_list:
    rawData = lines.split(";")
    country = rawData[1]
    if country == country1:
        country1_goals += 1
    else: country == country2
    country2_goals +=1

choice = input("between " + country1 + " and " + country2 + ", which team scored more goals? (input country with a capital letter) ")
choiceTrue = ((choice == country1 and country1_goals > country2_goals) or
              (choice == country2 and country2_goals > country1_goals))

if choiceTrue == True:
    print("Correct!")
else: choiceTrue == False
print("Incorrect!")

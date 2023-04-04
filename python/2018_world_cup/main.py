# Blake Reneau  03/29/23
# get information about goals from the 2018 football/soccer world cup
import os

os.system('clear')
goal_list = open("goals.txt", "r")
print("2018 world cup goal index")
print("A: number of goals scored by country")
print("B: number of goals scored by a player")
print("C: players who scored for a country")
print("D: number of goals from all countries")
print("E: number of goals scored during first half")
print("F: number of goals scored during second half")
print("G: number of goals scored during overtime")
print("H: goals scored for each country")
print("I: Country with most goals")
print("J: Player with most goals")
print("X: exit")
choice = input("choose: ")
if choice == "A" or choice == "B" or choice == "C":
    global countryOrPlayer
    countryOrPlayer = input("what country or player? (spell the name EXACTLY, as with a capital) ")
if choice == "C":
    print("players who scored for " + countryOrPlayer + ":")
if choice == "D":
    print("Goals scored: " + (str(sum(1 for line in open('goals.txt')))))
goals = 0
countryScores = {}

for line in goal_list:
    data = line.split(";")
    player = data[0]
    country = data[1]
    minute = int(data[2])
    if choice == "A" and countryOrPlayer == country:
        goals += 1
    if choice == "B" and countryOrPlayer == player:
       goals += 1
    if choice == "C" and countryOrPlayer == country:
        print(player)
    if choice == "E" and minute <= 45:
        goals += 1
    if choice == "F" and minute <= 90:
        goals += 1
    if choice == "G" and minute >= 90:
        goals += 1
    if choice == "H":
        if country in countryScores:
            countryScores.update({country: 0})
            print(countryScores)
            countryScores[country] += 1
        else:
            countryScores[country] += 1
            


if goals > 0:
    print("Goals scored: " + str(goals))


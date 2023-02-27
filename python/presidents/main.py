# Blake Reneau 2/15/23
# A program to list the current, previous, and next president of a year.
import os

os.system('clear')

years = []
names = []
yearInput = int(input("Enter a year between 1789 and 2025 to get the previous, current, and next president of that year: "))
presidents = open("presidents.txt", "r")

increment = 0
yearincrement = 0

for rawdata in presidents:
    data = rawdata.split(";")
    name = data[0]
    beginningYear = int(data[1])
    endingYear = int(data[2])
    names.append(name)
    years.append(beginningYear)
    years.append(endingYear)
    if yearInput <= endingYear and yearInput >= beginningYear:
        print(names[increment-1] + ": from " + str(years[yearincrement-2]) + " to " + str(years[yearincrement]))
        print(name + ": from " + str(beginningYear) + " to " + str(endingYear) )
        continue
    yearincrement +=2
    increment += 1
    if yearInput < endingYear:
        print(name + ": from " + str(beginningYear) + " to " + str(endingYear) )
        break

# Blake Reneau 03/22/23
# Example of the birthday paradox
import datetime
import random

#function to give random date between two dates.
def randomDate():
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2023,12,31)
    delta = end - start
    randomDays = random.randint(0,delta.days)
    randomDate = start + datetime.timedelta(days=randomDays)
    return randomDate

#list of names
names = ["John", "Jane", "Steve", "Alex", "Bob", "Bill", "Jennifer", "Jim", "Jack", "Jill", "Gilgamesh", "Bryan", "Luke", "Josh", "Emily", "Tasha", "Anabelle", "Lucy", "Rose", "The Doctor", "Max", "Teo", "Amy", "Elliot", "Harold", "Ram", "Cletus", "Apple", "FancySetup", "stone", "Raven", "Mary"]

total = 0
tests = 10

for k in range(0,tests):
    print("\n" + "---------------------")
    birthdayList = []
    
    message = ""
    for i in range(0,len(names)):
        birthDate = randomDate()
        birthDay = birthDate.strftime('%d %b')
        for j in range(1,len(birthdayList)):
            if birthdayList[j] == birthDay:
                message = message + names[i] + " and " + names[j] + " share the same birthday: " + birthDay
                
        birthdayList.append(birthDay)
        print(names[i] + " - Birthday: " + birthDay)

    if message == "":
        print("No students from this class share the same birthday.")
    else:
        print(message)
        total = total + 1
        print("---------------------")

print("\n" + "\n" + "Overall result after " + str(tests) + " tests: " + str((total*100/tests)) + "%")

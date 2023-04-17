# Blake Reneau 17/04/2023
# Days before or after calculator
from time import sleep
import calendar
from datetime import *

#now = datetime.now()
now = date.today()
print("today is " + now.strftime("%A, %b %dnd/th/rd, %Y"))

dateInput = input("what date do you want to know how far into the future/past it is? (FORMAT IS DD/MM/YYYY) ")
dateList = dateInput.split("/")
day = int(dateList[0])
month = int(dateList[1]) 
year = int(dateList[2])
finalDate = date(year,month,day)
dateDifference = (finalDate - now).days
print("the difference in days is exactly " + str(dateDifference) + " days.")

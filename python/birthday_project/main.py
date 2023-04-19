# Blake Reneau 04/18/2023
# Birthday info? i guess?
from datetime import *
import calendar

now = date.today()
nowMonthDay = [now.month, now.day]
dateInput = input("what is your birthday? (DD/MM/YYYY format) ")
dateSplit = dateInput.split("/")
day = int(dateSplit[0])
month = int(dateSplit[1]) 
year = int(dateSplit[2])
birthday = date(year,month,day)
birthdayMonthDay = [month, day]
nextBirthday = date((now.year + 1), month, day)
print(nextBirthday)
dayDifference = (now - birthday).days
nextBirthdayDifference = (nextBirthday - now).days
yearDifference = (now.year - birthday.year)
print("you are " +str(yearDifference) + " years old.")
print("you were born on a " + str(calendar.day_name[datetime.weekday(birthday)]))
print("you have been alive for " + str(dayDifference) + " days")
print("your next birthday is in " + str(nextBirthdayDifference) + " days")
if nowMonthDay == birthdayMonthDay:
    print("today is your birthday! happy birthday!")

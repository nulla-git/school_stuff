# Blake Reneau 04/12/23
# written to show coherency with date module
import calendar
from datetime import *

now = datetime.now()
print("today is " + now.strftime("%A, %b %dnd/rd/th, %Y"))

travel_time = float(input("how many days forward, a positive number, or backwards, a negative number,\nwould you like to travel in time? "))
deltaDate = date.today() + timedelta(travel_time)
print("the date is now " + str(deltaDate) + " on a " + str(calendar.day_name[datetime.weekday(deltaDate)]))

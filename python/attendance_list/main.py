#I didn't write most of this, my teacher is having
#me write this to learn.
import os
os.system('clear')

print("############################")
print("#                          #")
print("#        Class Roll        #")
print("#                          #")
print("############################")
print("")
print("Valid Codes:")
print("   /  - Present")
print("   M  - Medical Absence")
print("   T  - School Trip")
print("   A  - Authorized Absence")
print("   X  - No reason provided")
print("")
validCodes = ["/","M","T","A","X"]

#Open classlist file in read mode
classlist = open("classlist.txt", "r")

#Open attendance file in (over)write mode
attendance = open("attendance.txt", "w")

for pupil in classlist:
    fields = pupil.split(";")
    firstname = fields[0]
    lastname = fields[1]
    code = input(firstname + " " + lastname + "? ")
    #check if a valid code is entered
    while not code in validCodes:
        print("Invalid code - try again.")
        code = input(firstname + " " + lastname + "? ")

    #store code with pupil's name
    attendance.write(code + " - " + firstname + " " + lastname + "\n")

#close the file in order to poen and print the file contents later
attendance.close()

print()
print("--------------------------")
print()
print("Attendance Report")

print()

attendance = open("attendance.txt", "r")
print(attendance.read())

print(">>>The End.")

#close both files
classlist.close()
attendance.close()

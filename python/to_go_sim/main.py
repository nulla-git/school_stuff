# Blake Reneau 04/21/2023
# to go menu simulator that refrences a text file
import os

os.system('clear')
rawMenuData = open("menu.txt", "r")
codeList = []
itemList = {}
for line in rawMenuData:
    splitData =line.split(";")
    code = splitData[0]
    menuItem = splitData[1]
    price = splitData[2] 
    codeList.append(code)
    itemList.update({menuItem: price})

print("welcome to Peppino's Pizzeria")                      
print("yes we do get regularly sued for false advertising")


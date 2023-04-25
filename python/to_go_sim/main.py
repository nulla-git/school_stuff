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
print("no, we do not serve pizza.\nyes, we do get regularly sued for false advertising")
total = float(0)
request = input("enter the code for the item you want: ")
finished = False
firstRun = True
# ok this is a little complicated so i'll go ahead and explain.
# 
while finished == False:
    if firstRun == False:
        request = input("what else do you want (enter code)? ") 
    itemPosition = codeList.index(request)
    itemListKeys = list(itemList.keys())
    keyNameOfItem = ((list(itemListKeys))[itemPosition])
    costOfItem = itemList[keyNameOfItem]
    print(str(keyNameOfItem) + ": $" + str(costOfItem))
    total += float(costOfItem)
    print("new total: $" + str(round(total, 2)))
    wantAnother = input("do you want to order anything else? (Y/N) ")
    if wantAnother == "Y" or wantAnother == "y":
        firstRun = False 
    if wantAnother == "N" or wantAnother =="n":
        finished = True


print("Your toal comes out to $" + str(round(total, 2)))
print("thank you for not suing us when we told you our name is a lie")

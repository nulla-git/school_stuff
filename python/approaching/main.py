# me, today, right now
# i am rapidly approaching your location
import os
import time
os.system('clear')

def me():
    milesFromYourHouse = 20
    while True:
        print((" " * milesFromYourHouse) + "@@")
        time.sleep(0.05)
        #os.system('clear')
        milesFromYourHouse -= 1
        if milesFromYourHouse // 3:
            print(((" " * (milesFromYourHouse + 1))) + "@")
        if milesFromYourHouse < 0:
            break
    
me()

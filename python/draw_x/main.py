# Blake Reneau 04/02/2023
# draw a large ascii x
import time

def drawX():
    size = 11
    mutSize = 10
    i = 0
    while size > mutSize:
        print((" " * i ) + "x" + (" " * (mutSize * 2)) + "x" + (" " * i))
        mutSize -= 1
        i += 1
        time.sleep(0.2)
        if mutSize == 0:
            print((" " * i) + "x")
            break
        #elif -mutSize > mutSize:
            #print("x" + (" " * mutSize) + "x")
            #mutSize +=1


drawX()


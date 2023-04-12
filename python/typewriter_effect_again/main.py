#typing text effect
import time,os,sys

def typingPrint(text, speed):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
        
#calls typingPrint method found on line 3
#Text = what is found between the "" below; Example: >>> Welcome! >>>
typingPrint(">>> Welcome! >>>\n", 0.05)


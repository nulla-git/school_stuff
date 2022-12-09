import time,os,sys

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    value = input()
    return value

os.system("clear")

typingPrint("***********************************************************\n")
typingPrint("*                                                         *\n")
typingPrint("*                                                         *\n")
typingPrint("*                                                         *\n")
typingPrint("*                                                         *\n")
typingPrint("*           welcome to untitled basic text game           *\n")
typingPrint("*         use one or two words to describe what you want  *\n")
typingPrint("*         to do.                                          *\n")
typingPrint("*                                                         *\n")
typingPrint("*                                                         *\n")
typingPrint("***********************************************************\n")

decision_notValid = False
while True:
    decision = typingInput("what do you want to do? ")
    if decision == 'look' or decision == 'look around' or decision == 'explore':
        decision_notValid = False
        typingPrint("you are in a prison cell with an open door.")
        time.sleep(4)
        os.system("clear")
        continue
    if decision == 'escape' or decision == 'walk out' or decision == 'go out' or decision == 'get out' or decision == 'walk outside' or decision =='leave':
        typingPrint("you win!")
        time.sleep(4)
        os.system("clear")
        break
    decision_notValid = True
    if decision_notValid == True:
        typingPrint("invalid choice!")
        time.sleep(4)
        os.system("clear")

for character in 'thank you for playing!\ncredits: blake reneau\n':
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)
time.sleep(4)
os.system("clear")

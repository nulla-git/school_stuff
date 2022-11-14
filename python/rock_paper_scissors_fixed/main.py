#blake reneau 11/10/22
#"fixing" a rock paper scissors game
import random

start = input("would you like to play rock paper scissors? ")
if start == "no":
    quit()
maxPoints = int(input("excluding draws of course, first to how many wins? "))
print("maxPoints: " + str(maxPoints))
cpuPoints = 0
playerPoints = 0

print("rock is 1, paper is 2, scissors is 3.")
while playerPoints < maxPoints and cpuPoints < maxPoints:
    cpuChoice = random.randrange(1, 3)
    print("alright then, rock paper scissors...")
    playerChoice = int(input("shoot! (input your answer): "))
    playerWin = ((playerChoice == 2 and cpuChoice == 1) or
                 (playerChoice == 3 and cpuChoice == 2) or
                 (playerChoice == 1 and cpuChoice == 3))
    print("playerWin: " + str(playerWin))
    print("")
    if playerChoice == cpuChoice:
        print("cpu chose " + str(cpuChoice) + ", draw.")
        continue
    elif playerWin == True:
        playerPoints = playerPoints + 1
        cpuPoints == cpuPoints + 1
        print("you win")
        print("current standings:")
        print("player: " + str(playerPoints))
        print("cpu: " + str(cpuPoints))
        input("press enter to continue...")
        continue
    else: playerWin == False
    cpuPoints += 1
    print("cpu chose " + str(cpuChoice))
    print("you lost")
    print("current standings:")
    print("player: " + str(playerPoints))
    print("cpu: " + str(cpuPoints))
    input("press enter to continue") continue

if playerWin == True:
    print("in total....")
    print("the cpu won " + str(cpuPoints) + " rounds...")
    print("and you won " + str(playerPoints) + " rounds, meaning you won.")
elif playerWin == False:
    print("in total....")
    print("the cpu won " + str(cpuPoints) + " rounds...")
    print("and you only won " + str(playerPoints) + " rounds, meaning you lost.")

#blake reneau 11/04/22
#team manager
import random

foo = open("players.txt", "r")
bar = open("teams.txt", "r")
players = []
teams = []
players = foo.read().splitlines()
teams = bar.read().splitlines()
player_amount = len(players)
team_amount = len(teams)
teamA = []
teamB = []

while player_amount > 0:
    player_num = random.randrange(0, player_amount)
    print("selected player: " + players[player_num])
    selected_player = players[player_num]
    players.remove(selected_player)
    player_amount = len(players)
    print("player amount: " + str(player_amount))
    teamSelector = random.randrange(0, 1)
    if teamSelector == 0 and len(teamA) < 6:
        teamA.append(selected_player)
        print("player team: A")
        continue
    else: teamSelector == 1 and len(teamA) < 6
    teamB.append(selected_player)
    print("player team: B")
    continue

print("players in team A: " + str(teamA))
print("players in team B: " + str(teamB))

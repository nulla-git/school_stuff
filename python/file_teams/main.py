#blake reneau 11/04/22
#team manager
import random
import pandas

foo = open("players.txt", "r")
bar = open("teams.txt", "r")
players = []
teams = []
players = foo.read().splitlines()
teams = bar.read().splitlines()
player_amount = len(players)
team_amount = len(teams)
playersInTeam = (player_amount // team_amount)
Red_team = []
Blue_team = []
Yellow_team = []
Green_team = []
Orange_team = []
Purple_team = []

while player_amount > 0:
    player_num = random.randrange(0, player_amount)
    print("selected player: " + players[player_num])
    selected_player = players[player_num]
    players.remove(selected_player)
    player_amount = len(players)
    print("player amount: " + str(player_amount))
    team_num = random.randrange(0, team_amount)
    team_name = teams[team_num]
    print("team name: " + str(team_name))
    if (team_name) < playersInTeam:
        relected_player.insert(str(team_name))
        print(str(team_name))

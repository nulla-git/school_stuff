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
playersInTeam = (player_amount // team_amount)
red = []
blue = []
yellow = []
green = []
orange = []
purple = []

while player_amount > 0:
    player_num = random.randrange(0, player_amount)
    print("selected player: " + players[player_num])
    selected_player = players[player_num]
    players.remove(selected_player)
    player_amount = len(players)
    print("player amount: " + str(player_amount))
    team_num = random.randrange(0, team_amount)
    team_name = teams[team_num]
    print("team name: " + team_name)
#    if pointer < 2
#    selected_player.insert(pointer)
    

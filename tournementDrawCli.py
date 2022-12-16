import random
from datetime import datetime


###########################
# Entry Players and Points
###########################
PLAYERS = {
    'PlayerA': {
        'points': 1,
        'wins': 0,
        },
    'PlayerB': {
        'points': 2,
        'wins': 0,
        },
    'PlayerC': {
        'points': 2,
        'wins': 0,
        },
    'PlayerD': {
        'points': 4,
        'wins': 0,
        },
    'PlayerE': {
        'points': 5,
        'wins': 0,
        },
    'PlayerF': {
        'points': 6,
        'wins': 0,
        },
    'PlayerG': {
        'points': 7,
        'wins': 0,
        },
    'PlayerH': {
        'points': 8,
        'wins': 0,
        },
    'PlayerI': {
        'points': 9,
        'wins': 0,
        }
    }
###########################
###########################
###########################

def inital_text():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("TournementDrawTime: ", current_time)

    players_lst = list(PLAYERS.keys())
    print("-" * 60)
    print(players_lst)
    print("-" * 60)
    print("")


def selectRemovePlayer():
    player = random.choice(players_lst)
    players_lst.remove(player)
    return player


def getTournementDraw1v1():
    while len(players_lst) > 1:
        player1 = selectRemovePlayer()
        player2 = selectRemovePlayer()

        print(
            player1 + "(" + str(PLAYERS.get(player1).get('points')) + ")" + " vs. " + 
            player2 + "(" + str(PLAYERS.get(player2).get('points')) + ")" 
            )
        print("")


def getTournementDraw2v2():

    while len(players_lst) > 3:
        player1 = selectRemovePlayer()
        player2 = selectRemovePlayer()
        player3 = selectRemovePlayer()
        player4 = selectRemovePlayer()

        print(
            player1 + "(" + str(PLAYERS.get(player1).get('points')) + ")" + " & " + 
            player2 + "(" + str(PLAYERS.get(player2).get('points')) + ")" + " vs. " + 
            player3 + "(" + str(PLAYERS.get(player3).get('points')) + ")" + " & " + 
            player4 + "(" + str(PLAYERS.get(player4).get('points')) + ")" 
            )
        print("")


def printPlayerRanks(valueKey='points'):

    print("  Highest: " + valueKey)
    print("-" * 18)
    rankPlayers_dct = PLAYERS.copy()
    place = 1

    while len(rankPlayers_dct) > 0:
        best_player = max(rankPlayers_dct, key=rankPlayers_dct.get(valueKey))
        print("  " + str(place) + ". " + best_player + " (" + str(rankPlayers_dct.get(best_player).get(valueKey)) + ")" )
        rankPlayers_dct.pop(best_player)
        place += 1
    print("-" * 18)
    print("")


def show_complete_score():
    players_lst = list(PLAYERS.keys())
    print("free: ", players_lst)
    print("")
    print("-" * 60)
    for p in PLAYERS:
        print(p + " " + str(PLAYERS.get(p)))
    print("-" * 60)
    print("")


inital_text()
###########################
# Select function
###########################
#getTournementDraw2v2()
getTournementDraw1v1()
#printPlayerRanks()
###########################
show_complete_score()

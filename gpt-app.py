from flask import Flask, render_template, request
import random

app = Flask(__name__)

PLAYERS = {
    'PlayerA': {
        'points': 1,
        },
    'PlayerB': {
        'points': 2,
        },
    'PlayerC': {
        'points': 2,
        },
    'PlayerD': {
        'points': 4,
        },
    'PlayerE': {
        'points': 5,
        },
    'PlayerF': {
        'points': 6,
        },
    'PlayerG': {
        'points': 7,
        },
    'PlayerH': {
        'points': 8,
        },
    'PlayerI': {
        'points': 9,
        }
    }

def select_remove_player(players_lst):
    player = random.choice(players_lst)
    players_lst.remove(player)
    return player

def get_tournament_draw(num_players):
    players_lst = list(PLAYERS.keys())
    matches = []
    while len(players_lst) >= num_players:
        match = []
        for i in range(num_players):
            player = select_remove_player(players_lst)
            match.append((player, PLAYERS[player]['points']))
        matches.append(match)
    return matches

@app.route('/')
def home():
    return render_template('gpt-home.html', players=PLAYERS)

@app.route('/tournament', methods=['POST'])
def tournament():
    num_players = int(request.form['num_players'])
    matches = get_tournament_draw(num_players)
    return render_template('gpt-tournament.html', matches=matches, players=PLAYERS)

if __name__ == '__main__':
    app.run()
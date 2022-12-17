from flask import Flask, render_template, redirect, request
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy, session
import os
import random


RPLAYER_ID_LST = []
COMPETITION_MODE = ""
SORT_PLAYERS = "points-desc"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(app.root_path, 'main.db')

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

fa = FontAwesome(app)

"""
Task
- id :int
- name : str
- complete :bool
"""
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    #def __init__(self, id, name, complete):
    #    self.id = id
    #    self.name = name
    #    self.complete = complete

    def __repr__(self):
        return f'<Task {self.name}>'

"""
Task
- id : int
- name : str
- wins : int
- points : int
- ranks : int
"""
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wins = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    ranks = db.Column(db.Integer, default=0)

    # def __init__(self, id, name, wins, points, ranks):
    #     self.id = id
    #     self.name = name
    #     self.wins = wins
    #     self.points = points
    #     self.ranks = ranks

    def __repr__(self):
        return f'<Player [{self.id}, {self.name}, {self.wins}, {self.points}]>'

"""
Tournament1on1
- id :int
- name : str
- complete :bool
"""
class Tournament1vs1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lap = db.Column(db.Integer)
    playerAID = db.Column(db.Integer)
    playerBID = db.Column(db.Integer)

    # def __init__(self, id, player1ID, player2ID):
    #     self.id = id
    #     self.player1ID = player1ID
    #     self.player2ID = player2ID

    def __repr__(self):
        return f'<Tournament1on1 {self.id}>'

"""
Tournament2on2
- id :int
- name : str
- complete :bool
"""
class Tournament2vs2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lap = db.Column(db.Integer)
    player1ID = db.Column(db.Integer)
    player2ID = db.Column(db.Integer)
    player3ID = db.Column(db.Integer)
    player4ID = db.Column(db.Integer)

    ## def __init__(self, id, player1ID, player2ID, player3ID, player4ID):
    ##     self.id = id
    ##     self.player1ID = player1ID
    ##     self.player2ID = player2ID
    ##     self.player3ID = player3ID
    ##     self.player4ID = player4ID

    def __repr__(self):
        return f'<Tournament2on2 {self.name}>'



#with app.app_context():
#    db.create_all()


@app.route('/')
def index():
    global SORT_PLAYERS

    tasks = Task.query.order_by(Task.id.asc()).all()
    complete_tasks = Task.query.filter_by(complete=True).count()

    if SORT_PLAYERS == "points-desc":
        players = Player.query.order_by(Player.points.desc()).all()
    elif SORT_PLAYERS == "names-asc":
        players = Player.query.order_by(Player.name.asc()).all()
    else:
        players = Player.query.order_by(Player.id.asc()).all()

    players_count = Player.query.filter_by(name=True).count()
    return render_template('index.html',
        tasks=tasks,
        players=players,
        players_count=players_count,
        complete_tasks=complete_tasks,
        rplayer_id_lst=RPLAYER_ID_LST,
        competition_mode=COMPETITION_MODE
    )


@app.route('/add', methods=["POST"])
def create_task():
    task = request.form.get('task')

    new_task = Task(name=task)

    db.session.add(new_task)

    db.session.commit()

    return redirect('/')


@app.route('/complete/<int:id>/')
def complete_task(id):
    task_to_update = Task.query.get(id)

    task_to_update.complete = True

    db.session.commit()

    return redirect('/')


@app.route('/delete/<int:id>/')
def delete_task(id):
    task_to_delete = Task.query.get(id)

    db.session.delete(task_to_delete)

    db.session.commit()

    return redirect('/')


@app.route('/add_player', methods=["POST"])
def create_player():
    player = request.form.get('player')

    new_player = Player(name=player)

    db.session.add(new_player)

    db.session.commit()

    return redirect('/')

@app.route('/delete_player/<int:id>/')
def delete_player(id):
    player_to_delete = Player.query.get(id)

    db.session.delete(player_to_delete)

    db.session.commit()

    return redirect('/')

@app.route('/save_points/<int:id>/<int:points>/', methods=["POST"])
def save_points(id, points):
    player_to_update = Player.query.get(id)

    player_to_update.wins = request.form.get('wins')
    player_to_update.points = request.form.get('points')
    db.session.add(player_to_update)
    db.session.commit()
    return redirect('/')

@app.route('/rcompetition_draw1vs1/')
def rcompetition_draw1vs1():
    global COMPETITION_MODE
    global RPLAYER_ID_LST

    print("Start rcompetition_draw1vs1")
    players = Player.query.order_by(Player.name.asc()).all()
    #print(len(players))
    RPLAYER_ID_LST = random_draw1vs1(players)
    for rplayer_id in RPLAYER_ID_LST:
        print("id= ", str(rplayer_id), ", name=", str(Player.query.get(rplayer_id)))
    print(RPLAYER_ID_LST)
    COMPETITION_MODE = "1vs1"

    return redirect('/')

@app.route('/rcompetition_draw2vs2/')
def rcompetition_draw2vs2():
    global COMPETITION_MODE
    global RPLAYER_ID_LST

    print("Start rcompetition_draw2vs2")
    players = Player.query.order_by(Player.name.asc()).all()
    #print(len(players))
    RPLAYER_ID_LST = random_draw1vs1(players)
    for rplayer_id in RPLAYER_ID_LST:
        print("id= ", str(rplayer_id), ", name=", str(Player.query.get(rplayer_id)))
    print(RPLAYER_ID_LST)
    COMPETITION_MODE = "2vs2"

    return redirect('/')


def random_draw1vs1(players):
    RPLAYER_ID_LST = [p.id for p in players]
    #print(rplayer_lst)
    if len(RPLAYER_ID_LST) > 1:
        random.shuffle(RPLAYER_ID_LST)
    else:
        print("Not enough Player")
    print(RPLAYER_ID_LST)
    return RPLAYER_ID_LST

def random_draw2vs2(players):
    RPLAYER_ID_LST = [p.id for p in players]
    #print(RPLAYER_ID_LST)
    if len(RPLAYER_ID_LST) > 3:
        random.shuffle(RPLAYER_ID_LST)
    else:
        print("Not enough Player")
    #print(RPLAYER_ID_LST)
    return RPLAYER_ID_LST

@app.route("/sort_players" , methods=['GET', 'POST'])
def sort_players():
    global SORT_PLAYERS

    selected = request.form.get('select_sort_players')
    SORT_PLAYERS = str(selected)
    print(SORT_PLAYERS)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, request
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
import os


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
        return f'<Player {self.name}>'

"""
Tournament1on1
- id :int
- name : str
- complete :bool
"""
class Tournament1on1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lap = db.Column(db.Integer)
    player1ID = db.Column(db.Integer)
    player2ID = db.Column(db.Integer)

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
class Tournament2on2(db.Model):
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
    tasks = Task.query.order_by(Task.id.desc()).all()
    complete_tasks = Task.query.filter_by(complete=True).count()
    return render_template('index.html', tasks=tasks, complete_tasks=complete_tasks)


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


if __name__ == "__main__":
    app.run(debug=True)

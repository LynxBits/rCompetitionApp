from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///main.db', echo = True)
meta = MetaData()

task = Table(
   'task', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

players = Table(
   'players', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('wins', Integer, default=0),
    Column('points', Integer, default=0),
    Column('ranks', Integer, default=0)
)

tournament1on1 = Table(
    'tournament1on1', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('lap', Integer),
    Column('player1ID', Integer),
    Column('player2ID', Integer),
)

tournament2on2 = Table(
    'tournament2on2', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('lap', Integer),
    Column('player1ID', Integer),
    Column('player2ID', Integer),
    Column('player3ID', Integer),
    Column('player4ID', Integer),
)

meta.create_all(engine)
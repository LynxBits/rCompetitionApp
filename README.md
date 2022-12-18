# rCompetition App
This is a simple application built with Flask for easy Competition (Tournement) organisation.

The script tournementDrawCli.py is a easy to use standalone cli-tool to draw a round randomly by handwritten list.

The Flask application is a web tool with the same functionality of the cli-tool.
# Flask App - Python - rCompetition
Install requirements for Python==3.9.13:

```
pip install -r requirements.txt
```

Run the file to create the database

```
python create_all_db.py
```

Run app with

```
app.py
```

## Docker - Flask App

Build:

```
docker image build -t flask_docker_rcompetition .
```

Run:

```
docker run -p 5000:5000 -d flask_docker_rcompetition
```
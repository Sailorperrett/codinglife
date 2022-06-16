from flask import flask
import rhino3dm import

app = flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from sailor '

from flask import Flask  


app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello world</h2>'

@app.route("/<name>")
def indexpersonalize(name):
    return f'<h1>Hello {name}</h2>'






from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    from bootstrap import template
    return template("Hello, World!")


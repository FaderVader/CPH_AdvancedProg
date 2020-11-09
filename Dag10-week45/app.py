from flask import Flask, url_for, request
app = Flask(__name__)

from ehtml import *

@app.route("/")
def hello_world():
    return html(lang="en")[
      head,
      body[
        h1["Hello, World!"],
        create_main_content(),
        p["this is a cool edsl"]
      ]
    ].render()

def create_main_content():
    return div(_class="main-content")[
        p["this is the main content"]
    ]

@app.route("/user")
def user_site():
    return f"This is the user site"

@app.route("/api")
def api():
    return { "api" : "this is my api" }

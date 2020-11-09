from flask import Flask
# import ehtml as h
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hej Verden'

@app.route("/jvh")
def jvh():
    return "Jakob Viggo Hansen - nu med flaske"

@app.route('/api')
def api():
    return {'key': "value", 'key2': "value2"}


@app.route("/html")
def hello_world2():
    return h.html[
        h.head,
        h.body[
            h.h1(_class="title")
            [
                "Hello, world!"
            ]
        ]
    ]
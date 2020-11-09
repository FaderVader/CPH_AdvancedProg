--- 
title: Avanceret Programmering (Uge 45)
author: Christian Gram Kalhauge (CKL)
aspectratio: 43
theme: Copenhagen
colortheme: seahorse
monofont: Menlo
headers-includes: |
  \usepackage{absmath}
  \usepackage[utf8]{inputenc}
  \usepackage{inconsolata}
---


# Programing Language Theory

## General Purpose Programming Language

- A language in which you can write all possible programs.

- Examples?

## How would we know (Turing Completeness)

- If we can implement a Turing Machine, we can run all programs.

- https://www.python-course.eu/turing_machine.php

## With great powers comes great problems (Halting Problem)

```python
def check_if_halts(a : program, b : input):
    ...

def be_evil(program):
    while check_if_halts(program, program):
        continue

# What does it return?
check_if_halts(be_evil, be_evil)
```

## Domain Specific Language

- Limit the power of the language

- But, make it easier to specify and analyse the domain.

- Examples?


## Downsides

- Requires special parsers


## Embeded Domain Sepcific Languages (eDSL)

- Exploiting the syntax of the host language we can embed a new language.

- It can vary from looking like an API to a full - fledged perversion of the
programming lanugage.


## Example 1 (funcparser)

https://github.com/kalhauge/funcparser/

```python
def setup(
        verbose: Counter('v')=0, 
        logfile: FileType('w')=sys.stdout
        ):
    print('Hello', verbose, logfile)

parse_args(setup, [], '-vv --logfile /tmp/log.txt'.split())
```


## Example 2 (flask)

https://flask.palletsprojects.com/en/1.1.x/quickstart/

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```


## Example 3 (html)

```python
import ehtml as h

@app.route("/")
def hello_world():
    return h.html[
        h.head,
        h.body[
            h.h1(_class="title")[
              "Hello, world!"
            ]
        ]
    ]
```


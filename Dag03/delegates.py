#!/usr/bin/env python3

import random

def simple_greeting(name):
    return f"{name} - hello!"

def time_greeting(name):
    from datetime import datetime
    return f"{name} - It's {datetime.now()}"

def my_greeting(name):
    return f"{name} - brain-phase"


greetings = [ simple_greeting
            , time_greeting,
            my_greeting
            ]

name = input('Say your name:')

greeting = random.choice(greetings)
print(greeting.__call__(name))
# for greeting in greetings:
#     print(greeting.__call__(name))
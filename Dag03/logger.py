#!/usr/bin/env python3

from datetime import datetime

def logger(file):
    def inner(msg, level="INFO"):
        pass

log = logger(sys.stdout); 

log("Hello, World!")
log("Second log", level="DEBUG")


# 1. Make sure that the log prints the 'msg'

# 2. Include the info level

# 3. Also add a timestamp

# 4. Make sure you print to the file.

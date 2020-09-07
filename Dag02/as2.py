from datetime import datetime
import sys

def logger(file):
    
    def inner(msg, level="INFO"):
        pass
    
    return inner

log = logger(sys.stdout);

# Add time and debug level to the log.

log("Hello, World!")
# 19:45 -- INFO  -- Hello, World!

log("Second log", level="DEBUG")
# 19:45 -- DEBUG -- Hello, World!
from contextlib import contextmanager

from time import time

class Timer:
    
    def __enter__(self):
        # fill self.start with the time
        
    def __exit__(self, type, value, traceback):
        # fill self.stop with the time
     
timer = Timer()
with timer:
    sum(range(1000000))
    
print(timer.delta)
    
# 1. fill out __enter__ and __exit__

# 2. write a @property delta that calculates the delta between start and stop

# 3. use the timer to time the other assignemnts. 
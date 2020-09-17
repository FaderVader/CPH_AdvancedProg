
from functools import wraps

class CallCounter:
    def __init__(self, function, count = 0):
        self._function = function
        self.count = count

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self._function(*args, **kwargs)

    def refresh(self):
        tmp = self.count
        self.count = 0
        return tmp


def count_calls(fn):
    return wraps(fn)(CallCounter(fn))

def dynamic(function):
    # Right now we do nothing.. This is not cool
    return function


@dynamic 
@count_calls
def fib(n): 
    if n < 2: return n 
    else: return fib(n - 1) + fib(n - 2)

for n in [1, 2, 3, 5, 10, 20, 30]:
    print(f"n = {n:>3}: fib(n) = {fib(n):>10} in {fib.refresh():>10} calls.")


# This combines a lot of things we have learned.

# 1. Run the program.

# 2. Figure out why the fib method is so slow.

# 3. Fill out the wrapper function 'dynamic'. Since the fib function is pure, we can 
#    save the results of running the function from it's inputs.
#    fib(0) is always 0 
#    fib(1) is always 1
#    ...
#    Instead of calling fib(0) return results[0] instead.


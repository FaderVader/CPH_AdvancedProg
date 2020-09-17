def add_one(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs) + 1
    return inner

@add_one  # decorator -> use composition to wrap function in other function
def const(number):
    return number

print(const(10))
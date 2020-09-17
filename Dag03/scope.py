var = 1

def prnt1():
    print(var)
    # var = 2 # forbidden -

prnt1()

def prnt2():
    global var
    var = 2 # not forbidden -
    print(var)

prnt2()
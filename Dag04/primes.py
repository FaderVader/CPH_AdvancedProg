def nats(n=0):
    while True:
        yield n
        n += 1

def primes(numbers):
    from itertools import takewhile
    from math import sqrt
    shive = []
    for number in numbers:
        limited = takewhile(lambda x: x <= sqrt(number), shive)
        if any(number % s == 0 for s in limited): continue
        shive.append(number)
        yield number

for prime in primes(nats(2)):
    print(prime)
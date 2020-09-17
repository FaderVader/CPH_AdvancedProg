"https://stackoverflow.com/questions/34698842/why-is-the-fibonacci-sequence-big-o2n-instead-of-ologn"

def dynamic(function):
    results = dict()
    def inner(n):
        try:
            return results[n]
        except KeyError:
            results[n] = function(n)
            # print(f'Now generating new key for {n} - dict length now: {len(results)}')
            return results[n]
    return inner

@dynamic
def fib(n): 
    if n < 2: return n 
    else: return fib(n - 1) + fib(n - 2)

print(fib(300)) # calling the decorated fib

# invoking fib from a iteration
def fibGenerator(n):
    i = 0
    while i <= n:
         yield fib(i)
         i = i+1

for i in fibGenerator(3000):
    print(f'FibGenerator: {i}')

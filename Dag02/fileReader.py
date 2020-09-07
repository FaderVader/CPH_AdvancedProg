with open("example.txt") as f:
    print(f"First line = {f.readline()!r}") #each readline moves line-pointer forward
    print([len(line) for line in f])        #so we only get 2 results here

with open("example.txt") as f:
    print([len(line) for line in f])

with open("example.txt") as f:
    for line in f:
        print(repr(line))

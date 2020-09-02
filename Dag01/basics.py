"First Line doesn't need comment#"

True, False # bool literals
1, 1.0 #numbers
'c#', "Hej" #string

#comments - but this one does need it because it comes after 1. line of death

str(1) + "Hello"

print('Hello', 1, 2)

#list [mutable]
y = [1, 2, 3]
print(y[1]) #2 (index 0 fra start)
print(y[-3]) # 1 (index -1 fra slut)

print(y.pop(0))
print(f'length: {len(y)}')

y.append(4)

for x in y:
    print(x)

#tuples (immutable)
x = (1, 2, 3)
print(f'tuple: {x}')

x2 = x
# x2[0] = 'first' # illegal operation - tuples are immutable - lists are not!

for e in x:
    print(e)

for e in x2:
    print(e)

# sets {unordered}
myTuple = ('a', 'b', 'c')
mySet = {1, 2, myTuple}

for elem in mySet:
    print(f'element of set: {elem}')

for i,l in enumerate(mySet):
    print(f'Index: {i}, value: {l}')

for l in reversed(range(0, 5, 2)):
    print(l)


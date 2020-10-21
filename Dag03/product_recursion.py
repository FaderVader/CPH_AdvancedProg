# non-recursive summing
numbers = [1 , 5, 10, 3]

def getProduct(numbers):
    if len(numbers) < 1: # simply a guard clause
        return 0

    product = numbers[0]
    for number in numbers:
        product = product * number
    return product

print(getProduct(numbers))
###############################

# recursive headache I
def sumof(numbers):
    if not numbers: return 0 # guard clause but also endpoint of recursion: now go back up the stack
    head, *rest = numbers # head is assigned first item, rest is now one item shorter
    return head + sumof(rest) # recurse but also exitpoint from last operation in stack

print(f'Sum of: {sumof(numbers)}')
####################################

# recursive II
def getPositives(numbers, acc=[]):
    if  len(numbers) < 1: 
        return # bounce back up the stack from here
    else:
        head, *rest = numbers
        if head>0: acc.append(head)
        getPositives(rest, acc)
        return acc #exitpoint from last operation in stack

numbers = [-10, 12, 3 , -4]
result = getPositives(numbers)
print(f'Only the positive vibes: {result}')

# more recursion with python 
# Sodoku solver: https://www.youtube.com/watch?v=G_UYXzGuqvM  (computerphile)

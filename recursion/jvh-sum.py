def sum_ints(lst):
    if lst == []: return 0
    s = lst.pop()
    return s + sum_ints(lst)

lst = [1, 2, 3, 4, 5]
print(sum_ints(lst))


def list_from_list(count): # POC only - we're building a list from a list ;-)
    def inner(lst):
        if lst == []: return []
        return lst[:1] + inner(lst[1:])
    lst = [*range(count)]
    return inner(lst)

print(list_from_list(3))


def rev_list_from_list(lst): 
    if lst == []: return []
    return lst[-1:] + rev_list_from_list(lst[:-1])

lst = [*range(3)]
print(rev_list_from_list(lst))


def list_from_number(count): # descending value
    if count == 0: return []
    return [count] + list_from_number(count - 1)

print(list_from_number(3))


def list_from_number2(max, start = 0): # increasing value
    if start > max: return []
    return [start] + list_from_number2(max, start+1)

print(list_from_number2(10, 5))


def factorial(start):
    if start == 1: return 1
    return start * factorial(start-1)

print(factorial(4))

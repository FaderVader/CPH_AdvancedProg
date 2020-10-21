"https://www.youtube.com/watch?v=eqo2LxRADhU (The Coding Train)"

def quicksort(lst, start, end):
    if start >= end: return

    index = partition(lst, start, end)
    quicksort(lst, start, index-1)
    quicksort(lst, index+1, end)
    return lst

def partition(lst, start, end): # https://youtu.be/eqo2LxRADhU?t=494 (partition function)
    pivotIndex = start
    pivotValue = lst[end]
    for i in range(start, end, 1):
        if lst[i] < pivotValue:
            lst[i], lst[pivotIndex] = lst[pivotIndex], lst[i] # swap
            pivotIndex += 1
    lst[end], lst[pivotIndex] = lst[pivotIndex], lst[end] # swap 
    return pivotIndex

lst = [-2, 3, 5, 12, 1, -5, 4, 7, 8, 13]
print(quicksort(lst, 0, len(lst)-1))
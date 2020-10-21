"https://www.youtube.com/watch?v=kFeXwkgnQ9U (Derrick Sherrill)"

def quicksort(lst):
    """
    Sorts a list using a merge sort

    >>> quicksort([])
    []
    >>> quicksort([1])
    [1]
    >>> quicksort([5, 2])
    [2, 5]
    >>> quicksort([5, 2, 3])
    [2, 3, 5]
    >>> quicksort([1, 12, 23, 12, 3, 2, 23, 41])
    [1, 2, 3, 12, 12, 23, 23, 41]
    """
    if len(lst) < 2: return lst
    lst_lower = []
    lst_higher = []

    pivot = lst.pop()
    for item in lst:
        if item < pivot:
            lst_lower.append(item)
        else:
            lst_higher.append(item)

    return quicksort(lst_lower) + [pivot] + quicksort(lst_higher)

lst = [-2, 3, 5, 12, 1, -5, 4, 7, 8, 13]
print(quicksort(lst))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

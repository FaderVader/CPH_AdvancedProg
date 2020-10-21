from issorted import issorted

def bubblesort(lst):
    """ Computes a bubble-sort

    >>> bubblesort([5, 2, 3])
    [2, 3, 5]
    >>> bubblesort([])
    []
    >>> bubblesort([1])
    [1]
    """
    if len(lst) < 2:
        return lst

    changed = True
    while changed:
        changed = False
        for i in range(1, len(lst)):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                changed = True
    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()

result = bubblesort([4, 3, 10, 2, 1])
print(result)
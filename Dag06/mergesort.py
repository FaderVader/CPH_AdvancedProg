from merge import merge

def mergesort(lst):
    """
    Sorts a list using a merge sort

    >>> mergesort([])
    []
    >>> mergesort([1])
    [1]
    >>> mergesort([5, 2])
    [2, 5]
    >>> mergesort([5, 2, 3])
    [2, 3, 5]
    >>> mergesort([1, 12, 23, 12, 3, 2, 23, 41])
    [1, 2, 3, 12, 12, 23, 23, 41]

    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

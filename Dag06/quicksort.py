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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

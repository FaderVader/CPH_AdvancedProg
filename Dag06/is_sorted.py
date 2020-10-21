def issorted(lst):
    """Check if a list is sorted # 
    
    >>> issorted([])
    True
    
    >>> issorted([3])
    True

    >>> issorted([3, 5, 2])
    False

    >>> issorted([7, 9, 13])
    True
    
    >>> issorted([7, 22, 13])
    False

    """

    if len(lst) <= 1:       # intial edge case
        return True

    last_seen, *rest = lst
    for i in rest:          # iterate over elements in list
        if last_seen <= i:
            last_seen = i
        else:
            return False    # any case fails all elements
    return True             # all elements conform to condition

# this helps us test the code, is only run if we
# run the module:
if __name__ == '__main__':
    import doctest
    doctest.testmod()


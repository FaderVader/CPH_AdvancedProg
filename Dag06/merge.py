def merge(xs, ys): # implicit initial condition : arg-lists are each sorted internally
    """ Merges two sorted lists

    >>> merge([], [])
    []
    >>> merge([], [1,2])
    [1, 2]
    >>> merge([1,2], [])
    [1, 2]
    >>> merge([1,3], [2,4])
    [1, 2, 3, 4]
    """

    # define a method to merge the arg-lists
    if not xs:
        return ys
    if not ys:
        return xs
    
    x, *xs_ = xs
    y, *ys_ = ys
    if x < y: return [x] + merge(xs_, ys)
    else: return [y] + merge(xs, ys_)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# list_a = [1, 2, 3, 7]
# list_b = [4, 5, 6]
# list_ab = merge(list_a, list_b)
# print (list_ab)

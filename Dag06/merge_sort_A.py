def merge_sort(lst): # keep splitting list until all elements are in discreet lists

    if len(lst) <= 1: return lst

    mid = len(lst)//2
    l_part = lst[:mid]
    r_part = lst[mid:]

    merge_sort(l_part)
    merge_sort(r_part)

    i = j = k = 0

    while i < len(l_part) and j < len(r_part):
        if l_part[i] < r_part[j]:
            lst[k] = l_part[i]
            i += 1
        else:
            lst[k] = r_part[j]
            j += 1
        k += 1

    while i < len(l_part):
        lst[k] = l_part[i]
        i += 1
        k += 1

    while j < len(r_part):
        lst[k] = r_part[j]
        j += 1
        k += 1

    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod()

data = [3, 4, 1, 6, 2, 9, 7, 5, 10, 8]
result = merge_sort(data)
print(result)

data = []
result = merge_sort(data)
print(result)

data = [1]
result = merge_sort(data)
print(result)
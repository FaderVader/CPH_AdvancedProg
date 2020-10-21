def merge_sort(lst):
    if len(lst) <= 1: return lst

    middle = len(lst)//2
    left = lst[:middle]
    right = lst[middle:]
    left = merge_sort(left)
    right = merge_sort(right)

    values = []

    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            values.append(left[0])
            left.pop(0)
        else:
            values.append(right[0])
            right.pop(0)
    
    for l in left:
        values.append(l)

    for r in right:
        values.append(r)

    return values

data = [3, 4, 1, 6, 2, 9, 7, 5, 10, 8]
result = merge_sort(data)
print(result)
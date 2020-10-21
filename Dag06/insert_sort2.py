"https://stackoverflow.com/questions/18070565/recursive-insertion-sort-in-python"

"recursive version"

def insertOne(element, lst):
    if len(lst) == 0:
        return [element]
    elif element < lst[0]:
        return [element] + lst
    else:
        return lst[0:1] + insertOne(element, lst[1:])

def insert_sort(lst):
    if len(lst)<2:
        return lst
    else:
        return insertOne(lst[0], insert_sort(lst[1:]))

data = [3, 1, 7, 6, 5]
result = insert_sort(data)
print(result)
"https://www.youtube.com/watch?v=byHi41L9vTM (Derrick Sherrill)"

"Iterative version"

def insert_sort(lst):
    indexing_length = range(1, len(lst)) # skip the first element
    
    for i in indexing_length:
        value_to_sort = lst[i]

        while lst[i-1] > value_to_sort and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]  # swap positions
            i = i - 1
    
    return lst

lst = [-2, 3, 5, 12, 1, -5, 4, 7, 8, 13]
print(insert_sort(lst))
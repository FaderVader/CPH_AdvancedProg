from merge import merge
# imports merge.py in this directory

def merge_sort(lst):
    if len(lst) <= 1: return lst

    mid = len(lst)//2
    l_part = lst[:mid]
    r_part = lst[mid:]

    merge_sort(l_part)
    merge_sort(r_part)

    return merge(merge_sort(l_part), merge_sort(r_part))

data = [3, 4, 1, 6, 2, 9, 7, 5, 10, 8]
result = merge_sort(data)
print(result)

# helpers: 
# https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
# https://en.wikipedia.org/wiki/Merge_sort
# https://stackabuse.com/merge-sort-in-python/
"https://www.youtube.com/watch?v=DnvWAd-RGhk"

"iterative solution"

def binary_search(lst, item):
    begin_index = 0
    end_index = len(lst)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = lst[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1        
        else: 
            begin_index = midpoint + 1

    return None # item does not exist in list

sorted_lst = [-5, -2, 1, 3, 4, 5, 7, 8, 12, 13]
print(binary_search(sorted_lst, 8))
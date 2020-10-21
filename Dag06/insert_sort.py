"https://stackabuse.com/insertion-sort-in-python/"

"Iterative version"

def insert_sort(lst):
    for index in range(1, len(lst)):
        currentValue = lst[index] 
        currentPosition = index

        while currentPosition > 0 and lst[currentPosition - 1] > currentValue:
            lst[currentPosition] = lst[currentPosition - 1]
            currentPosition = currentPosition - 1
        
        lst[currentPosition] = currentValue
    return lst
                

data = [3, 1, 7, 6, 5]
result = insert_sort(data)
print(result)
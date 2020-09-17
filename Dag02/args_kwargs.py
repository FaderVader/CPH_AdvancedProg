"https://www.geeksforgeeks.org/args-kwargs-python/"

def print_everything(*args):    #like javascript rest-operator (used to pass a non-key worded, variable-length argument list)
    for count, thing in enumerate(args):
        print(f'{count}. {thing}')

print_everything('apple', 'banana', 'cabbage')
####################################################

def table_things(**kwargs):   # keyworded, variable-length argument list.
    for name, value in kwargs.items():
        print(f'{name} = {value}')

table_things(apple = 'fruit', cabbage = 'vegetable')
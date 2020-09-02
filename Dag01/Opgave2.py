"Reverse Polish notation calc"

# Setup
numberStack = []
newNumber = True
allowedOperators = ('+', '-', '*', '/')

# define functions
def AddNumberToStack(number):
    actualNumber = int(number)
    numberStack.append(actualNumber)


def PerformOperation(operator):
    if len(numberStack) < 1:
        return 

    if len(numberStack) < 2:
        valueA = numberStack[-1]
        AddNumberToStack(valueA)
        return valueA

    valueA = numberStack[-1]
    valueB = numberStack[-2]

    if operator == '+':
        result = valueA + valueB

    elif operator == '-':
        result = valueA - valueB

    elif operator == '*':
        result = valueA * valueB

    elif operator == '/':
        result = valueA / valueB

    else:
        return

    AddNumberToStack(result)
    return result


def EvalOperator(argument):
    if argument in allowedOperators:
        result = PerformOperation(argument)
        PrintStack(argument, result)
    else:
        AddNumberToStack(argument)


def PrintStack(operator, result):
    print(f'The result of {operator} on the stack is: {result}')
    if len(numberStack) > 1:
        print(f'Current stack: {numberStack[-1]}, {numberStack[-2]} ')

# Main loop
while newNumber:
    newNumber = input("Number or operator: ")

    if not newNumber:
        break

    EvalOperator(newNumber)
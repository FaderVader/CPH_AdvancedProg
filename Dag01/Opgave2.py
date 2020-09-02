"Reverse Polish notation calc"

numberStack = []
newNumber = True

while newNumber:
    newNumber = input("Number or operator: ")

    if not newNumber:
        break

    #if newNumber in ("+", "-")
    numberStack.append(int(newNumber))

    for number in numberStack:
        print(number)

    stackLength = len(numberStack)

    if stackLength > 1:
        valueA = numberStack[-1]
        valueB = numberStack[-2]
        print(f'ValueA: {valueA}, valueB: {valueB}')
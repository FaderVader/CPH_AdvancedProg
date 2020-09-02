"Reverse Polish notation calc"

# Setup
numberStack = []
userInput = True
LINE_WIDTH = 40
LAST_IN_STACK = -1
SECONDLAST_IN_STACK = -2
allowedOperators = ('+', '-', '*', '/')
header = '+---------------- stack ---------------+'

# define functions
def AddNumberToStack(number):
    actualNumber = float(number)
    numberStack.append(actualNumber)
    return


def PerformOperation(operator):
    if len(numberStack) < 1:
        return 

    if len(numberStack) < 2:
        valueA = numberStack[LAST_IN_STACK]
        AddNumberToStack(valueA)
        return valueA

    valueA = numberStack[LAST_IN_STACK]
    valueB = numberStack[SECONDLAST_IN_STACK]

    if operator == '+':
        result = valueA + valueB

    elif operator == '-':
        result = valueA - valueB

    elif operator == '*':
        result = valueA * valueB

    elif operator == '/':
        result = valueB / valueA

    else:
        return

    AddNumberToStack(result)
    return result


def EvalInput(argument):
    if argument in allowedOperators:
        result = PerformOperation(argument)
        return result
    else:
        AddNumberToStack(argument)


def BuildDisplayLine(operator, result):
    if len(numberStack) == 0:
        return '|'+ ' '*(LINE_WIDTH-2) + '|'

    if len(numberStack) == 1:
        stackDump = f'|{numberStack[LAST_IN_STACK]}'

    if len(numberStack) > 1:
        stackDump = f'|{numberStack[SECONDLAST_IN_STACK]}, {numberStack[LAST_IN_STACK]}'

    padRepeatCount = LINE_WIDTH - (len(stackDump)+1) # +1 because eol char |
    padding = ' '*padRepeatCount
    completeLine = f'{stackDump}'+padding+'|' 
    return completeLine


# Main loop
while userInput:
    userInput = input(header + ' ')

    if not userInput:
        break

    result = EvalInput(userInput)
    header = BuildDisplayLine(userInput, result)

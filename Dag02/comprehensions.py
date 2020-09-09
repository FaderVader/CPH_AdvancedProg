output = [i for i in [0,1,2,3,4] if i % 2 == 0]
# print(f'{type(output)}: {output}') # list: 0, 2, 4

output = {i % 2 for i in range(4)}
# print(f'{type(output)}: {output}') # set: 0, 1

output = {i: i % 2 for i in range(4)} # {i, i%2} = {key, value}
# print(f'{type(output)}: {output}') # 

loremIpsum = []
sortedLorem = []
sortedLoremDict = {}
with open('loremipsum.txt') as f:
    for line in f:        
        loremIpsum = line.split()
        result = [len(word) for word in loremIpsum]
        # print(f'{type(result)}: {result}')
        result = {len(word) for word in loremIpsum}
        # print(f'{type(result)}: {result}')

        dictResult = {word: len(word) for word in loremIpsum}
        for key, value in dictResult.items():
            # print(key, value)
            combinedItem = key + '|' + str(value)
            sortedLorem.append(combinedItem)
    sortedLorem.sort(key=lambda x: x.lower())
    # print(' '.join(sortedLorem))

    test = 'accumsan|8'
    w1 = test.split('|')[0] # get the first element of the split

    acceptedMinimum = 10
    sortedLoremDict = {pair.split('|')[0]: pair.split('|')[1] for pair in sortedLorem}
    maxLength = [int(pair.split('|')[1]) for pair in sortedLorem if int(pair.split('|')[1]) >= acceptedMinimum] # 
    maxLength.sort(reverse=True)
    max = int(maxLength[0])
    for key, value in sortedLoremDict.items():
        padding = ' '*(max-len(key))
        print(repr(key), padding, repr(value))
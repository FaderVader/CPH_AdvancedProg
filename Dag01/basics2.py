#######################################
# lists - ordered - allows duplicates #
#######################################
list1 = ['alpha', 'beta', 'gamma']
list2 = ['tree', 'beta', 'flower']

print(list1[1])
list1.extend(list2)
list1.sort()
print(set(list1))

###############################
# tuples - ordered, immutable #
###############################
list1 = ('alpha', 'beta', 'gamma')
list2 = ('tree', 'beta', 'flower')

print(list2[2])
# list2[2] = 'bird' # illegal: tuples are immutable
list3=list(list2) # workaround
list3[2]='bird'
list2 = tuple(list3)
print(list2)
print(list2.index('bird')) #2

sentence = 'This is a sentence'
words = sentence.split(' ')
print(len(words)) # expect 4

##################################
# set - unordered - unique items #
##################################
list1 = {'alpha', 'beta', 'gamma'}
list2 = {'tree', 'beta'}
list2.add('flower')
print(f'set, difference: {list1.difference(list2)}')
print(f'set, intersection: {list1.intersection(list2)}')
list1.update({'lion', 'mig'})
print(list1)
combinedSets = list1.union(list2)

###############
# dictionarys #
###############
thisDict = {
	"key": "value",
	"a": "alfa",
	2: "beta"
}

otherDict = dict(key1 = 'value1', two = 2, key3 = 'three')

print(thisDict[2])
print(thisDict['key'])

value = thisDict.get('a')
handleNotFound = thisDict.get('unknown', 'default') # if key not found, return fallback value

print(value) # alfa
thisDict[2] = 'gamma'
for key in thisDict:
    print(f'Dictionery key {key} has value: {thisDict[key]}')

thisDict['new key']="new value"

for key, value in thisDict.items():
    print(f'2: Dict key {key} has {value}')

allValues = thisDict.values()
for value in allValues:
    print(f' values only: {value}')

if 'key' in thisDict:
    print('Found the "key" you wanted')


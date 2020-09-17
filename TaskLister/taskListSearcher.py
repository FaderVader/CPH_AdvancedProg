from csv import DictReader

print('Search the list of services and processes. Choose:')
userChoice = input('1: find service   - 2: find any ')

# Search for service 
def FindService():
    serviceSearchTerm = input("Service Search Term: ")
    serviceSearchTerm = serviceSearchTerm.lower()
    with open('tasklist.csv') as t:
        for row in DictReader(t):
            if serviceSearchTerm in row["Services"].lower(): 
                print(row)

# process unique, with list of attached services
# sort dict-key alphabetically 
def FindAny():
    aggregatedTaskList = {}
    with open('tasklist.csv') as t:
    # t = ReadFile()
        for row in DictReader(t):
            exeFile = row['Image Name']
            if exeFile in aggregatedTaskList:
                oldItems = aggregatedTaskList[exeFile]

                newItem = row['Services']
                oldItems.append(newItem) # add to list
                tempSet = set(oldItems) # remove duplicates
                oldItems = list(tempSet) # back to list-form

                aggregatedTaskList[exeFile] = oldItems
            else: 
                newList = [row['Services']]
                aggregatedTaskList[exeFile] = newList
        return aggregatedTaskList

def DoSearch(taskList):
    searchTerm = input("Input search-term: ")
    for exeFile, services in taskList.items():
        if searchTerm in exeFile:
            print(f'{searchTerm} was found in process {exeFile} with attached services {services}') 

        # must loop over all items in services to search for match
        for service in services:
            if searchTerm.lower() in service.lower():
                print(f'{searchTerm} was found in process {exeFile} with attached services {services}') 


if userChoice == '1':
    FindService()
elif userChoice == '2':
    taskList = FindAny()
    DoSearch(taskList)
else:
    print("Choice not recognized")
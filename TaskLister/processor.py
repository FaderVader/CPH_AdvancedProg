from csv import DictReader

# Search for service 
# serviceSearchTerm = input("Service Search Term: ")
# serviceSearchTerm = serviceSearchTerm.lower()
# with open('tasklist.csv') as t:
#     for row in DictReader(t):
#         if serviceSearchTerm in row["Services"].lower(): # == 'Dell Customer Connect':
#             print(row)

# process unique, with list of attached services
# sort dict-key alphabetically 
with open('tasklist.csv') as t:
    aggregatedTaskList = {}

    for row in DictReader(t):
        exeFile = row['Image Name']
        if exeFile in aggregatedTaskList:
            oldValue = aggregatedTaskList[exeFile]
            aggregatedTaskList[exeFile] = oldValue + ', ' + row['Services']  
        else: 
            aggregatedTaskList[exeFile] = row['Services'] 

    
    for key, value in aggregatedTaskList.items():
        print(key, value)
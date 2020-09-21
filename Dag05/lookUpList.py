# list of tuples{key, value}

class LookupList:
    def __init__(self):
        self._list = []
    
    def get(self, key):
        for set in self._list:  
            if set[0] == key:   # compare to the first element of the tuple
                return set

    def put(self, key, value):
        # will stack all new sets on top, allows duplicates
        # element = (key, value)
        # self._list.append(element)

        # will not allow duplicates
        for (i, (key2, value2)) in enumerate(self._list):
            if key2 == key:
                self._list[i] = (key,value)
                break
        else:
            self._list.append((key, value))

l = LookupList()
l.put('Lagkage', '200 kalorier')
l.put('Brunsviger', '2000 kalorier')
l.put('Lagkage', '10.000 kalorier')

found = l.get('Lagkage')[1] # [1] = get the value from the tuple
print(found)

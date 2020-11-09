"https://brilliant.org/wiki/tries/"

class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                newNode = Node()
                newNode.key = currentWord[0]
                if len(currentWord) == 1:
                    newNode.value = value
                currentNode.children[currentWord[0]] = newNode
                currentNode = newNode
                currentWord = currentWord[1:]
        
    def lookUp(self, word):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                return "Not in trie"
        if currentNode.value is None:
            return "None"
        return currentNode.value

    def printAllNodes(self):
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            node = nodes.pop(0)
            print(f'Key: {node.key}, value: {node.value}')


def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.insert(word, value)
    return trie

word_dict = {"ERR": "Fatal", "WRN": "Warning", "INF": "Information", "ERRO": "Also fatal"}
trie = makeTrie(word_dict)
trie.printAllNodes()
print(trie.lookUp('INF'))
print(trie.lookUp('ERRO'))

        
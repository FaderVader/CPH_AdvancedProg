"https://www.youtube.com/watch?v=7XmS8McW_1U - Trie Data Structure - Beau teaches JavaScript"

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node()

    def add(self, word, value):
        def inner(word, node):
            if len(word) == 0:
                node.value = value
                return
            elif word[0] not in node.children:
                newNode = Node(word[0])
                node.children[word[0]] = newNode
                return inner(word[1:], newNode)
            else:
                return inner(word[1:], node.children[word[0]])
        return inner(word, self.root)

    def find(self, word):
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                return None
        return currentNode.value    
        
            

def makeTrie(words):
    trie = Trie()
    for word, value in words.items():
        trie.add(word, value)
    return trie

word_dict = {"ERR": "Fatal", "WRN": "Warning", "INF": "Information", "Test": 12, "ERRO": "Also fatal"}
trie = makeTrie(word_dict)

for key in word_dict:
    print(trie.find(key))
# print(trie.find('not'))




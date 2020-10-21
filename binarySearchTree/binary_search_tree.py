"https://www.youtube.com/watch?v=ZNH0MuQ51m4"
"Coding Train js version of binary search"

"https://www.youtube.com/watch?v=5cU1ILGy6dM + https://codepen.io/beaucarnes/pen/ryKvEQ?editors=0012"
"Binary Search Tree - Beau teaches JavaScript" 

import random

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def searchTree(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            elif node.left != None:
                return self.searchTree(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = Node(data)
                return
            elif node.right != None:
                return self.searchTree(data, node.right)
        else:
            return None

    def add(self, data):
        node = self.root
        if node == None:
            self.root = Node(data)
            return
        else: 
            return self.searchTree(data, node)

    def removeNode(self, node, value):
        if node is None: return None
        
        if value == node.data:
            if node.left is None and node.right is None: # node has no children 
                return None
            
            if node.left is None: # node has no left child 
                return node.right

            if node.right is None: # node has no right child 
                return node.left

            # node has two children 
            tempNode = node.right
            while tempNode.left != None:
                tempNode = tempNode.left
            node.data = tempNode.data
            node.right = self.removeNode(node.right, tempNode.data)
            return node

        elif value < node.data:
            node.left = self.removeNode(node.left, value)
            return node

        else:
            node.right = self.removeNode(node.right, value)
            return node

    def remove(self, value):
        self.root = self.removeNode(self.root, value)

    def isPresent(self, value):
        current = self.root
        while current != None:
            if current.data == value:
                return True
            if current.data < value:
                current = current.right
            else: 
                current = current.left
        return False
    
    def findMin(self):
        current = self.root
        while current.left != None:
            current = current.left
        return current.data

    def findMax(self):
        current = self.root
        while current.right != None:
            current = current.right
        return current.data

    def minHeight(self, node = None):
        if node is None:
            node = self.root

        def findMinHeight(node): 
            if node == None:
                return -1
            
            left = findMinHeight(node.left)
            right = findMinHeight(node.right)

            if left < right:
                return left + 1
            else: 
                return right + 1
        return findMinHeight(node)

    def maxHeight(self, node = None):
        if node is None:
            node = self.root

        def findMaxHeight(node):
            if node is None:
                return -1

            left = findMaxHeight(node.left)
            right = findMaxHeight(node.right)

            if left > right:
                return left + 1
            else:
                return right + 1
        
        return findMaxHeight(node)

    def isBalanced(self):
        return self.minHeight() >= self.maxHeight()-1
    

        
bst = BST()
node_count = 40000
for number in range(node_count):
    number = random.randint(1, 300000)
    bst.add(number)

min = bst.findMin()
max = bst.findMax()
found = bst.isPresent(max+1)

if bst.isPresent(10):
    bst.remove(10)
found = bst.isPresent(10)

print(bst.minHeight())
print(bst.maxHeight())
print(bst.isBalanced())

print('done')
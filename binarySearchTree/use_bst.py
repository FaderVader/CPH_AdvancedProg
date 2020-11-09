from binarySearchTree import Node, BST
import random

bst = BST()

# this sequence is just random numbers:
# node_count = 40000
# for number in range(node_count):
#     number = random.randint(1, 300000)
#     bst.add(number)

# this sequence tests for ability to determine balanced vs un-balanced:
numbers = [9, 4, 17, 3, 6, 22, 5, 7, 20]
for number in numbers:
    bst.add(number)
    
print(f'Tree is balanced: {bst.isBalanced()}') # false
bst.add(10)
print(f'Tree is balanced: {bst.isBalanced()}') # true

min = bst.findMin()
max = bst.findMax()
found = bst.isPresent(max+1)
found_recurse = bst.isPresent_recursive(max)
print(f'Found {max+1} by iteration: {found}')
print(f'Found {max} by recursion: {found_recurse}')

# if bst.isPresent(10):
#     bst.remove(10)
# found = bst.isPresent(10)

print('MinHeight of tree is {}'.format(bst.minHeight()))
print('Maxheight if tree is {}'.format(bst.maxHeight()))
print(f'Tree is balanced: {bst.isBalanced()}')

print(f'in order: \t{bst.inOrder()}')
print(f'pre order: \t{bst.preOrder()}')
print(f'post order: \t{bst.postOrder()}')
print(f'level order: \t{bst.levelOrder()}')

print('done')
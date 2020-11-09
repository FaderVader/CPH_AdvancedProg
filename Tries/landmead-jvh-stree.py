"""
https://nbviewer.jupyter.org/gist/BenLangmead/6665861
JVH: didn't work - I can't insert the pointers to files in terminator
"""

class SuffixTree(object):
    
    class Node(object):
        def __init__(self, lab):
            self.lab = lab # label on path leading to this node
            self.out = {}  # outgoing edges; maps characters to nodes
    
    def __init__(self):
        self.root = self.Node(None)

    def stripLabel(self, input, new_tail):
        index = input.find('$')
        if index < 0: return input

        stripped_input = input[:index]
        old_tail = input[index:]
        tails = old_tail +  new_tail
        return stripped

    def addLine(self, lineContent, client, file, lineNumber):

        # JVH: devise intelligent method of added references to lines
        terminator = '$'
        pointer = f'{client}-{file}-{lineNumber}{terminator}'
        lineContent += terminator

        # self.root.out[lineContent[0]] = self.Node(lineContent) # trie for just longest suf

        # add the rest of the suffixes, from longest to shortest
        for i in range(0, len(lineContent)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(lineContent):
                if lineContent[j] in cur.out:
                    child = cur.out[lineContent[j]]

                    # strip pointer off label
                    # prepare concatenated label for later insertion
                    stripped_label = child.lab
                    index = stripped_label.find('$')
                    new_pointer = ''
                    if index > -1:
                        stripped_label = child.lab[:index+1]
                        old_pointer = child.lab[index+1:]
                        new_pointer = old_pointer + pointer
                        child.lab = stripped_label

                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    k = j+1 
                    while k-j < len(stripped_label) and lineContent[k] == stripped_label[k-j]:
                        k += 1
                    if k-j == len(stripped_label):
                        child.lab = child.lab + new_pointer
                        cur = child # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = stripped_label[k-j], lineContent[k]

                        # create “mid”: new node bisecting edge
                        new_label = stripped_label[:k-j] #+ '$' + new_pointer
                        mid = self.Node(new_label)  
                        mid.out[cNew] = self.Node(lineContent[k:] + new_pointer) 

                        # original child becomes mid’s child
                        child.lab = child.lab + new_pointer
                        mid.out[cExist] = child

                        # original child’s label is curtailed
                        child.lab = stripped_label[k-j:] + new_pointer

                        # mid becomes new child of original parent
                        cur.out[lineContent[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    index = lineContent.find('$')
                    new_node = lineContent[j:]
                    # if index > -1:
                    #     stripped_line = lineContent[j:index]
                    #     old_pointer = lineContent[index:]
                    #     new_pointer = old_pointer + pointer
                    #     new_node = stripped_line + new_pointer
                    cur.out[lineContent[j]] = self.Node(new_node) 
    
    def followPath(self, s):
        """ Follow path given by s.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, offset) where 'node' is child and
            'offset' is label offset.  If we finish on a node, return (node,
            None). """
        cur = self.root
        i = 0
        while i < len(s):
            c = s[i]
            if c not in cur.out:
                return (None, None) # fell off at a node
            child = cur.out[s[i]]
            lab = child.lab
            j = i+1
            while j-i < len(lab) and j < len(s) and s[j] == lab[j-i]:
                j += 1
            if j-i == len(lab):
                cur = child # exhausted edge
                i = j
            elif j == len(s):
                return (child, j-i) # exhausted query string in middle of edge
            else:
                return (None, None) # fell off in the middle of the edge
        return (cur, None) # exhausted query string at internal node
    
    def hasSubstring(self, s):
        """ Return true iff s appears as a substring """
        node, off = self.followPath(s)
        if node is not None:
            index = node.lab.find('$')
            pointer = node.lab[index:]
            return pointer
        else:
            return None
    
    # Do we need this method ?
    def hasSuffix(self, s):
        """ Return true iff s is a suffix """
        node, off = self.followPath(s)
        if node is None:
            return False # fell off the tree
        if off is None:
            # finished on top of a node
            if '$' in node.out:
                # return '$' in node.out
                return node.out
        else:
            # finished at offset 'off' within an edge leading to 'node'
            return node.lab[off:]


stree = SuffixTree()
# stree.addLine('123123123', 'client', 'date', 12)
stree.addLine('there would have been a time for such a word', 'client', 'date', 12)
stree.addLine('there would have been a time for such a word', 'client1', 'date1', 14)
# stree.addLine('there would have been a time', 'client10', 'date10', 140)
# stree.addLine('[INF] @ApplicationLoaderHelper, environment var: "PROCESSOR_ARCHITECTURE": "AMD64" (SiteSelector.Domain.Processes.ProcessHandler) (1999c767)', 'client2', 'date2', 15)
# stree.addLine('[INF] @ApplicationLoaderHelper, environment var: "PROCESSOR_ARCHITECTURE": "AMD64" (SiteSelector.Domain.Processes.ProcessHandler) (1999c767)', 'client3', 'date3', 16)
# print(stree.hasSubstring('INF'))
print(stree.hasSubstring('would'))
from collections import namedtuple
from itertools import chain
import abc

def suffixes(string): 
    return [ (i, string[i:]) for i, _  in enumerate(string)]

def longest_prefix(xs, ys):
    for i, (x, y) in enumerate(zip(xs,ys)):
        if (x != y): return xs[0:i]
    return min(xs, ys, key=len)


class Node(namedtuple("Node", "children")):
    def lcp(self, other):
        for j, (pfx, child) in enumerate(self.children):
            lcp = longest_prefix(pfx, other)
            if lcp: return (j, lcp)
        return (-1, "")

    def __iter__(self):
        return chain.from_iterable(
                ((prf + x, i) for (x, i) in child)
                if isinstance(child, Node)
                else [(prf, child)]
             for prf, child in self.children)

class SuffixTree:
    """ A SuffixTree, is a special Trie which can be used to list positions in
    the list.
    """

    def __init__(self, root=None): 
        self.root    = root

    def add(self, string): 
        root = Node([]);
        for i, suff in reversed(suffixes(string)):
            node = root;
            while suff:
                (j, lcp) = node.lcp(suff)
                if lcp:
                    (pfx, child) = node.children[j]
                    if lcp != pfx: 
                        child = Node([(pfx[len(lcp):], child)])
                        node.children[j] = (lcp, child)
                    node = child
                    suff = suff[len(lcp):]
                else: 
                    node.children.append((suff, i))
                    suff = None

            self.root = root
            print(self.root)
        return self

    def search(self, pattern): 
        pref, node = "", self.root
        search = pattern
        while search:
            (j, lcp) = node.lcp(search)
            if lcp: 
                (pref, node) = node.children[j]
                search = search[len(lcp):]
                if search and lcp != search:
                    return

        yield from ((pattern + pref[len(lcp):] + x, i) for (x, i) in node)

    def __repr__(self): 
        return f"SuffixTree(root={self.root!r})"


if __name__ == "__main__":
    from pprint import pprint
    sf = SuffixTree().add("helllo")
    pprint(sf.root.children)
    for x in sf.search("ll"):
        print(x)

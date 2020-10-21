from collections import namedtuple


class BinTree:
    """
    A binary tree.

    >>> b = BinTree()
    >>> b
    BinTree(None)

    >>> b[2] = "b"
    >>> b[1] = "x"
    >>> b[3] = "c"
    >>> b[1] = "a"
    >>> list(b)
    [(1, 'a'), (2, 'b'), (3, 'c')]

    >>> b.pprint()
        - None
      + 1 = a
        - None
    + 2 = b
        - None
      + 3 = c
        - None


    >>> b.bfpprint()
    |                            2=b                             |
    |             1=a                           3=c              |
    |      None           None           None           None     |
    """

    Node = namedtuple("Node", "key value sml lrg")

    def __init__(self, root=None):
        self.root = root

    def __setitem__(self, key, value):
        def setit(node):
            if node is None:
                return BinTree.Node(key, value, None, None)
            elif key == node.key:
                return BinTree.Node(key, value, node.sml, node.lrg)
            elif key < node.key:
                return BinTree.Node(node.key, node.value, setit(node.sml), node.lrg)
            else:
                return BinTree.Node(node.key, node.value, node.sml, setit(node.lrg))

        self.root = setit(self.root)

    def __iter__(self):
        # in order
        def iterx(node):
            if not node is None:
                yield from iterx(node.sml)
                yield (node.key, node.value)
                yield from iterx(node.lrg)

        return iterx(self.root)

    def pprint(self):
        UNPRINTED = 0
        AFTER_SMALLER = 1
        AFTER_LARGER = 2
        Zipper = namedtuple("Zipper", "parent node depth state")

        zipper = Zipper(None, self.root, 0, UNPRINTED)
        while zipper:
            if zipper.state == UNPRINTED:
                node = zipper.node
                if node:
                    zipper = Zipper(
                        zipper._replace(state=AFTER_SMALLER),
                        node.sml,
                        depth=zipper.depth + 1,
                        state=UNPRINTED,
                    )
                else:
                    print("  " * zipper.depth + "- None")
                    zipper = zipper.parent
            elif zipper.state["state"] == AFTER_SMALLER:
                print("  " * indent + "+", zipper.node.key, "=", zipper.node.value)
                zipper = Zipper(
                    zipper._replace(state=AFTER_LARGER),
                    zipper.node.lrg,
                    depth=zipper.depth + 1,
                    state=UNPRINTED,
                )
            else:
                zipper = zipper.parent

    def bfpprint(self):
        level = [(self.root, 60)]
        new_level = []

        all_is_empty = False
        while not all_is_empty:
            print("|", end="")
            old_level, level = level, []
            all_is_empty = True
            for (node, size) in old_level:
                if node is None or node == "":
                    print(str(node).center(size), end="")
                    level.append(("", size))
                else:
                    all_is_empty = False
                    level.append((node.sml, size // 2))
                    level.append((node.lrg, size - size // 2))
                    print(f"{node.key}={node.value}".center(size), end="")
            print("|")

    def __repr__(self):
        return f"BinTree({self.root!r})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

--- 
title: Avanceret Programmering (Uge 44)
author: Christian Gram Kalhauge (CKL)
aspectratio: 43
theme: Copenhagen
colortheme: seahorse
monofont: Menlo
headers-includes: |
  \usepackage{absmath}
  \usepackage[utf8]{inputenc}
  \usepackage{inconsolata}
---


# Weighted Graphs

## What is a Weighted Graph

- A Graph is a set of verticies with edges between them, where there 
are distances on the edges.


```{.graphviz width=75% .center}
digraph { 
  rankdir=LR;
  a ->  b [ label = "3" ];
  b -> c [ label = "4" ];
  b -> x [ label = "2" ]; 
  x -> d [ label = "3" ];
  c -> a [ label = "2" ];
}
```

## Representation (Matrix) 

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1 [ label = 2 ]
}
```

```python
>>> graph = [ [ None, 2 ] 
...         , [ None, None]
...         ]

```

### An edge from 0 to 1.
```python
>>> graph[0][1]
2

```

### No edge from 1 to 0.
```python
>>> graph[1][0]

```

## Representation (Adjecency List)

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1 [ label = 2];
}
```

```python
>>> graph = [ { 1: 2 } # Out edges to 1
...         , { } # No out edges
...         ]

```

### An edge from 0 to 1.
```python
>>> graph[0].get(1, None)
2

```

### No edge from 1 to 0.
```python
>>> graph[1].get(2, None)

```

## Representation (Derived)

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1 [label=2];
}
```

```python
>>> from collections import namedtuple
>>> Edge = namedtuple("Edge", "node dist")
>>> def edgesof(frm):
...     if frm == 0:
...         yield Edge(node=1, dist=2)

```

### An edge from 0 to 1.
```python
>>> [ e for e in edgesof(0) if e.node == 1]
[Edge(node=1, dist=2)]

```

### No edge from 1 to 0.
```python
>>> [ e for e in edgesof(1) if e.node == 1]
[]

```

## Example (Map)

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  node [ fontsize=8, shape=circle, fixedsize=true, width=0.3];
  DK [label="DK"]
  SE [label="SE"]
  NO [label="NO"]

  DK -> SE [ label=2.1 ];
  DK -> NO [ label=5.1 ];
  SE -> DK [ label=1.8 ];
  SE -> NO [ label=1.2 ];
  NO -> SE [ label=1.1 ];
  NO -> DK [ label=5.3 ];
}
```

```python
>>> directions = {
...   "DK": [ Edge("SE", 2.1), Edge("NO", 5.1)],
...   "SE": [ Edge("DK", 1.8), Edge("NO", 1.2)],
...   "NO": [ Edge("SE", 1.1), Edge("NO", 5.3)],
... }

```

## Shortest Path? (Breath First Search)

```python
>>> def bfs(edgesof, start, end):
...     parent, fringe = {}, [(None, start)]
...     while not end in parent:
...         if not fringe: return None
...         (frm, to) = fringe.pop(0);
...         if to in parent: continue
...         parent[to] = frm
...         for e in edgesof(to):
...             fringe.append((to, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> bfs(directions.get, "DK", "NO")
['DK', 'NO']

```

## Let's remove the smallest item?

```python
>>> def popmin(lst, key=None):
...     a = min(lst)
...     lst.remove(a)
...     return a

```

## Shortest Path? (Breath First Search)

```python
>>> def bfs(edgesof, start, end):
...     parent, fringe = {}, [(None, start)]
...     while not end in parent:
...         if not fringe: return None
...         (frm, to) = fringe.pop(0);
...         if to in parent: continue
...         parent[to] = frm
...         for e in edgesof(to):
...             fringe.append((to, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> bfs(directions.get, "DK", "NO")
['DK', 'NO']

```

## Shortest Path! (Best First Search)

```python
>>> def Bfs(edgesof, start, end):
...     parent, fringe = {}, [(0, None, start)]
...     while not end in parent:
...         if not fringe: return None
...         d, p, v = popmin(fringe);
...         if v in parent: continue
...         parent[v] = p
...         for e in edgesof(v):
...             fringe.append((d + e.dist, v, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> Bfs(directions.get, "DK", "NO")
['DK', 'SE', 'NO']

```

## Time complexity

- Every node gets visited
- Every node is in the fringe
- $O(|V|^2)$



## Heap (A cool tree)

```python
>>> import heapq as H
>>> h = []
>>> H.heappush(h, 2)
>>> H.heappush(h, 1)
>>> H.heappop(h)
1
>>> H.heappop(h)
2

```

## Heap (A cool tree)

- `heappush` insert $O(1)$
- `heappop` delete min $O(\log N)$

- https://docs.python.org/3.8/library/heapq.html
- https://en.wikipedia.org/wiki/Fibonacci_heap

## Heapsort

```python
>>> def heapsort(l):
...     h = []
...     for i in l:
...         H.heappush(h, i)
...     return [H.heappop(h) for i in range(len(h))]

>>> heapsort([9, 4, 5, 2, 6, 7, 1, 3, 8])
[1, 2, 3, 4, 5, 6, 7, 8, 9]

```

## Shortest Path! (Best First Search)

```python
>>> def Bfs(edgesof, start, end):
...     parent, fringe = {}, [(0, None, start)]
...     while not end in parent:
...         if not fringe: return None
...         d, p, v = popmin(fringe);
...         if v in parent: continue
...         parent[v] = p
...         for e in edgesof(v):
...             fringe.append((d + e.dist, v, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> Bfs(directions.get, "DK", "NO")
['DK', 'SE', 'NO']

```

## Shortest Path (Dijkstra)

```python
>>> def dijkstra(edgesof, start, end):
...     parent, fringe = {}, [(0, None, start)]
...     while not end in parent:
...         if not fringe: return None
...         d, p, v = H.heappop(fringe);
...         if v in parent: continue
...         parent[v] = p
...         for e in edgesof(v):
...             H.heappush(fringe, (d + e.dist, v, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> dijkstra(directions.get, "DK", "NO")
['DK', 'SE', 'NO']

```

## Time Complexity


- $\Theta((|V| + |E|) \log |V|)$


## We know better

- https://www.youtube.com/watch?v=g024lzsknDo

## Shortest Path (Dijkstra)

```python
>>> def dijkstra(edgesof, start, end):
...     parent, fringe = {}, [(0, None, start)]
...     while not end in parent:
...         if not fringe: return None
...         d, p, v = H.heappop(fringe);
...         if v in parent: continue
...         parent[v] = p
...         for e in edgesof(v):
...             H.heappush(fringe, (d + e.dist, v, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> dijkstra(directions.get, "DK", "NO")
['DK', 'SE', 'NO']

```

## Shortest Path (A*)

```python
>>> def astar(edgesof, start, end, h):
...     parent, fringe = {}, [(h(start), 0, None, start)]
...     while not end in parent:
...         if not fringe: return None
...         _, d, p, v = H.heappop(fringe);
...         if v in parent: continue
...         parent[v] = p
...         for e in edgesof(v):
...             H.heappush(fringe, (d + e.dist + h(v), d + e.dist, v, e.node))
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path
>>> astar(directions.get, "DK", "NO", lambda x: 0)
['DK', 'SE', 'NO']

```

## Shortest Path (A*)

The heuristic is admissable if $h(x) < dist(x)$

- $h(x)$ the shortest posible distance to the target


# Trie


## String search

- $O(|N| * |M|)$ 
- $|N|$ is the length of the file
- $|M|$ is the length of the prefix

```python
>>> def find(key):
...     with open("shakespeare.txt") as f:
...         if key in f.read():
...             return True
...     return False 

```

## PP

```python
>>> import pprint 
>>> pp = pprint.PrettyPrinter(width=32, sort_dicts=True).pprint

```

## Trie

```python
>>> class Trie:
...    VALUE = ""
...    def __init__(self, root=None):
...        self.root = root or {}
...    def add(self, str, value):
...        node = self.root
...        for c in str:
...            node = node.setdefault(c, {})
...        node[Trie.VALUE] = value
...    def find(self, str):
...        node = self.root
...        for c in str:
...            node = node[c]
...        return node[Trie.VALUE]

```

## Trie (cont.)

```python
>>> t = Trie()
>>> t.add("hej", 1)
>>> pp(t.root)
{'h': {'e': {'j': {'': 1}}}}
>>> t.add("haj", 2)
>>> pp(t.root)
{'h': {'a': {'j': {'': 2}},
       'e': {'j': {'': 1}}}}
>>> t.add("he", 3)
>>> pp(t.root)
{'h': {'a': {'j': {'': 2}},
       'e': {'': 3,
             'j': {'': 1}}}}

```

## Trie (cont.)

```python
>>> t.find("hej")
1
>>> t.find("ha")
Traceback (most recent call last):
  ...
KeyError: ''

```

## Trie (find_all)

```python
>>> def all(node, prefix=""):
...     for c, v in node.items():
...         if c == "":
...            yield (prefix, v)
...         else:
...            yield from all(v, prefix + c)

```

## Trie (find_all)

```python
>>> def find_all(self, key):
...     node = self.root
...     for c in key:
...         node = node[c]
...     yield from all(node)

>>> list(find_all(t, "h"))
[('ej', 1), ('e', 3), ('aj', 2)]

>>> list(find_all(t, "he"))
[('j', 1), ('', 3)]

```

## Trie

- https://en.wikipedia.org/wiki/Trie


## Suffix Trie

- Add all sufficies to the trie 
- https://en.wikipedia.org/wiki/Suffix_tree

## Compressed Trie (Radix Tree)

- Suffix Tree is $O(N^2)$ memory see $a^nb^n$
- Edges can be strings instead of only chars.
- https://en.wikipedia.org/wiki/Radix_tree
- https://www.youtube.com/watch?v=hLsrPsFHPcQ


## Ukkonen's algorithm

- Updateing the suffix tree front to back.
- https://en.wikipedia.org/wiki/Ukkonen%27s_algorithm
- https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english/9513423#9513423

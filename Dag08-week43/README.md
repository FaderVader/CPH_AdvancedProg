--- 
title: Avanceret Programmering (Uge 43)
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


# Graphs

## What is a Graph

- A Graph is a set of verticies with edges between them.

```{.graphviz width=75% .center}
digraph { 
  rankdir=LR;
  a -> b -> c;
  b -> x -> d;
  c -> a;
}
```

## Examples

-  Transport Graph
-  Navigation Graph

## Representation (Matrix) 

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1
}
```

```python
>>> graph = [ [False, True ] 
...         , [False, False]
...         ]

```

### An edge from 0 to 1.
```python
>>> graph[0][1]
True

```

### No edge from 1 to 0.
```python
>>> graph[1][0]
False

```

## Representation (Adjecency List)

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1
}
```

```python
>>> graph = [ { 1 } # Out edges to 1
...         , { } # No out edges
...         ]

```

### An edge from 0 to 1.
```python
>>> 1 in graph[0]
True

```

### No edge from 1 to 0.
```python
>>> 0 in graph[1]
False

```

## Representation (Derived)

```{.graphviz width=25% .center}
digraph { 
  rankdir=LR;
  0 -> 1
}
```

```python
>>> def graph(frm, to):
...     # Some computation from your data
...     return frm == 0 and to == 1 

```

### An edge from 0 to 1.
```python
>>> graph(0, 1)
True

```

### No edge from 1 to 0.
```python
>>> graph(1, 0)
False

```

## Representations

Matrix 
  ~ Space  $O(V^2)$
  ~ Lookup $O(1)$

Adjacency
  ~ Space  $O(V \times E)$
  ~ Lookup $O(\log E/V)$

Derived
  ~ Space  ?
  ~ Lookup ?

## Example (Map)

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark"]
  SE [label="Sweeden"]
  NO [label="Norway"]
  GE [label="Germany"]
  FR [label="France"]
  I [label="Italy"]

  DK -> SE;
  DK -> GE;
  GE -> I;
  GE -> FR;
  GE -> DK;
  SE -> DK;
  SE -> NO;
  NO -> SE;
  FR -> GE;
}
```

```python
>>> directions = {
...   "Denmark": ["Sweden", "Germany"],
...   "Germany": ["Italy", "France", "Denmark"],
...   "Italy": [],
...   "Sweden": ["Denmark", "Norway"],
...   "Norway": ["Sweden"],
...   "France": ["Germany"]
... }

```


## Is Connected? (Breath First Search)

```python
>>> def bfs(edgesof, start, end):
...     visited, fringe = {start}, [start]
...     while not end in visited:
...         if not fringe: return False
...         v = fringe.pop(0);
...         for e in edgesof(v):
...             if e in visited: continue
...             visited.add(e)
...             fringe.append(e)
...     return True

>>> bfs(directions.get, "Denmark", "Italy")
True
>>> bfs(directions.get, "Italy", "Denmark")
False

```

## Is Connected? (Depth First Search)

```python
>>> def dfs(edgesof, start, end):
...     visited, fringe = {start}, [start]
...     while not end in visited:
...         if not fringe: return False
...         v = fringe.pop();
...         for e in edgesof(v):
...             if e in visited: continue
...             visited.add(e)
...             fringe.append(e)
...     return True

>>> dfs(directions.get, "Denmark", "Italy")
True
>>> dfs(directions.get, "Italy", "Denmark")
False

```

## Fringe (BFS)

```
visited: {Denmark}
fringe: [Denmark]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=red]
  SE [label="Sweden"]
  NO [label="Norway"]
  GE [label="Germany"]
  FR [label="France"]
  PL [label="Italy"]

  DK -> SE [color=red]; DK -> GE [color=red]; GE -> PL; GE -> FR; GE -> DK; SE -> DK; SE -> NO; NO -> SE; FR -> GE;
}
```

## Fringe (BFS) 

```
visited: {Denmark, Sweden, Germany}
fringe: [Sweden, Germany]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=blue]
  SE [label="Sweden", color=red]
  NO [label="Norway"]
  GE [label="Germany", color=red]
  FR [label="France"]
  PL [label="Italy"]

  DK -> SE; DK -> GE; GE -> PL; GE -> FR; GE -> DK; 
  SE -> DK [color=blue]; SE -> NO [color=red]; NO -> SE; FR -> GE;
}
```

## Fringe (BFS) 

```
visited: {Denmark, Sweden, Germany}
fringe: [Germany, Norway]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=blue]
  SE [label="Sweden", color=blue]
  NO [label="Norway", color=red]
  GE [label="Germany", color=red]
  FR [label="France"]
  PL [label="Italy"]

  DK -> SE; DK -> GE; GE -> PL [color=red]; GE -> FR[color=red]; GE -> DK [color=blue]; 
  SE -> DK ; SE -> NO; NO -> SE; FR -> GE;
}
```

## Fringe (BFS) 

```
visited: {Denmark, Sweden, Germany, Norway, France, Italy}
fringe: [Norway, France, Italy]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=blue]
  SE [label="Sweden", color=blue]
  NO [label="Norway", color=red]
  GE [label="Germany", color=blue]
  FR [label="France", color=red]
  PL [label="Italy", color=red]

  DK -> SE; DK -> GE; GE -> PL; GE -> FR; GE -> DK; 
  SE -> DK ; SE -> NO; NO -> SE; FR -> GE;
}
```

## Fringe (DFS)

```
visited: {Denmark}
fringe: [Denmark]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=red]
  SE [label="Sweden"]
  NO [label="Norway"]
  GE [label="Germany"]
  FR [label="France"]
  PL [label="Italy"]

  DK -> SE [color=red]; DK -> GE [color=red]; GE -> PL; GE -> FR; GE -> DK; SE -> DK; SE -> NO; NO -> SE; FR -> GE;
}
```

## Fringe (DFS) 

```
visited: {Denmark, Sweden, Germany}
fringe: [Sweden, Germany]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=blue]
  SE [label="Sweden", color=red]
  NO [label="Norway"]
  GE [label="Germany", color=red]
  FR [label="France"]
  PL [label="Italy"]

  DK -> SE; DK -> GE; GE -> PL [color=red]; GE -> FR [color=red]; GE -> DK [color=blue]; 
  SE -> DK ; SE -> NO ; NO -> SE; FR -> GE;
}
```

## Fringe (DFS) 

```
visited: {Denmark, Sweden, Germany, France, Italy}
fringe: [Sweden, France, Italy]
```

```{.graphviz width=50% .center}
digraph { 
  rankdir=LR;
  DK [label="Denmark", color=blue]
  SE [label="Sweden", color=red]
  NO [label="Norway"]
  GE [label="Germany", color=blue]
  FR [label="France", color=red]
  PL [label="Italy", color=red]

  DK -> SE; DK -> GE; GE -> PL; GE -> FR ; GE -> DK ; 
  SE -> DK ; SE -> NO ; NO -> SE; FR -> GE;
}
```

## Shortest Path (Breath First Search)

```python
>>> def bfs(edgesof, start, end):
...     parent, fringe = {start: None}, [start]
...     while not end in parent:
...         if not fringe: return None
...         v = fringe.pop(0);
...         for e in edgesof(v):
...             if e in parent: continue
...             parent[e] = v
...             fringe.append(e)
...     path = [end]
...     while (end := parent[end]) != None:
...         path.insert(0, end)
...     return path

```

## Shortest Path (example)

``` python
>>> bfs(directions.get, "Norway", "France")
['Norway', 'Sweden', 'Denmark', 'Germany', 'France']

```
## AI (example)

Wolf, Goat, and Cabbage Problem

![](graphics/wolf-goat-cabbage.png)

## AI (example)

```Python
>>> def has_problem(bank):
...     return {"W", "G"} <= bank or {"G", "C"} <= bank 

>>> def actions(state):
...     on_left, left, right = state
...     if has_problem(left) and not on_left: return
...     if has_problem(right) and on_left: return
...     yield (not on_left, left, right)
...     if on_left:
...         for k in sorted(left): 
...             yield (False, left - {k}, right | {k})
...     else:
...         for k in sorted(right): 
...             yield (True, left | {k}, right - {k})

```

## AI (Solution)

```Python
>>> start = (True, frozenset("WGC"), frozenset())
>>> end = (False, frozenset(), frozenset("WGC"))

>>> for w, lef, rig in bfs(actions, start, end):
...     print(f"{' '.join(sorted(lef)) or '.':>5} " 
...           + f"{'<-' if w else '->'} "
...           + f"{' '.join(sorted(rig)) or '.'}")
C G W <- .
  C W -> G
  C W <- G
    W -> C G
  G W <- C
    G -> C W
    G <- C W
    . -> C G W
 
 
 
 
 
 

```









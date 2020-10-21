--- 
title: Avanceret Programmering (Uge 41)
author: Christian Gram Kalhauge (CKL)
aspectratio: 43
theme: Copenhagen
colortheme: seahorse
headers-includes: |
  \usepackage{absmath}
  \usepackage[utf8]{inputenc}
---

## Today

|     Time      | Content                         |
| :-----------: | :------------------------------ |
| 17:00 - 17:45 | Presentations (8 \* 5 = 40 min) |
| 18:00 - 18:30 | Python Modules and `venv`       |
| 18:45 - 20:00 | Trees and Questions             |

## Presentation

- Idea

- Plan 

- Github Repo with README

- What is done next time (October 8th)

# Python Modules and `venv`

## How to reuse code (Modules)

### otherfile.py
```python
def function():
    print("Imported")
```

### myfile.py
```python
from otherfile import function
function()
```

## How to reuse code (in folders)

### `deep/__init__.py`
empty file to indicate that deep is a module

### `deep/otherfile.py`
```python
def function():
    print("Imported")
```

### `myfile.py`
```python
from deep.otherfile import function
function()
```

## Creating a virtual environment

More here: https://docs.python.org/3/library/venv.html

In your exam project create a virtual environment.
```bash
> c:\Python38\python -m venv venv
```

Activate it:

```bash
> venv\Scripts\activate.bat
```

Deactivate it:
```bash
> deactivate
```

## Using a virtual environment (in venv):

Installing:
```
$ pip install pylint
```

Freezing:
```
$ pip freeze > requirements.txt
```

Thawing:
```
$ pip install -r requirements.txt
```

# Trees

## Tree Basics

```
     r 
  /     \
 l  ...  l
```

- Root

- Node

- Leafs

## Binary Search trees

Each node is a key, a left branch and a right branch
Left side is smaller, Right side is bigger than key.

## Tree Traversals

https://en.wikipedia.org/wiki/Tree_traversal

- Depth First searches
  - Pre-order
  - In-order
  - Post-order

- Breadth First searches

## Iterative Tree Traversals (Zippers)

https://en.wikipedia.org/wiki/Zipper_(data_structure)

- Zippers. A data structure that holds the position of the iteration in 
the tree.

## Tries

- https://en.wikipedia.org/wiki/Trie
- https://en.wikipedia.org/wiki/Suffix_tree
- https://www.youtube.com/watch?v=VA9m_l6LpwI
- https://marknelson.us/posts/1996/08/01/suffix-trees.html


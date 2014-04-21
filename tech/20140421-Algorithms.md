Apr 21 2014 | algorithms | Kelly Chan
# Algorithms

table of contents
- 1. Basic Data Structures
    - stack
    - queue
    - list
    - tree
    - graph
- 2. Algorithms
    - analysis
    - recursion
    - sorting and searching

## 1. Basic Data Structures

### stack
### queue
### list
### tree

- node
- edge / path
- root / parent / children
- sibling
- subtree/ leafnode
- level / height

```python
BinaryTree()

getLeftChild()
getRightChild()

setRootVal(val)
getRootVal()

insertLeft(val)
insertRight(val)
```

example
```python
myTree = ['a',   #root
         ['b',  #left subtree
               ['d' [], []],
               ['e' [], []] ],
         ['c',  #right subtree
               ['f' [], []],
               [] ]
         ]
```

class tree
```python
class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
```

### graph

## 2. Algorithms

### anlysis
### recursion
### sorting and searching

---
### Reference
[Problem Solving with Algorithms and Data Structures](http://interactivepython.org/courselib/static/pythonds/index.html)

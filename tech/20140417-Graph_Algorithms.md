Apr 17 2014 | algorithms, graph | Kelly Chan
# Graph Algorithms

table of contents
- 1. searching
- 2. path
- 3. tree
- 4. matching
- 5. flow


## Introduction

G = (V, E)
- G: graph
- V: vertex/node
- E: edge/link

E = (v, w) - tuple
- E: edge/link
- v: 
- w: weight

V={V0,V1,V2,V3,V4,V5}  
E={(v0,v1,5),(v1,v2,4),(v2,v3,9),(v3,v4,7),(v4,v0,1),(v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)}

- path: V3 -> V1 - (V3,V4,V0,V1) - {(v3,v4,7),(v4,v0,1),(v0,v1,5)}
- cycle: (V5,V2,V3,V5)


Abstract Data Type
```python
Graph() 

addVertex(vert)
addEdge(fromVert, toVert)
addEdge(fromVert, toVert, weight)

getVertex(vertKey)
getVertices() 
```

Adjacency Matrix (dense) / List (sparse)

```python
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
```

## 1. searching

### BFS

```python

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')

    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)

    vertQueue = Queue()
    vertQueue.enquene(start)

    while(vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))

```

### DFS
### A*

## 2. path

### Dijkstra
### Bellman-Ford
### Floyd-Warshall


## 3. tree

### Prim
### Kruskal 


## 4. matching

### Edmonds's matching

## 5. flow

### Ford-Fulkerson
### Edmonds-Karp
### Dinic
### Push-relabel
### maximum flow
### Kosaraju
### Gabow
### Tarjan

---
### Reference
1. [Problem Solving with Algorithms and Data Structures](http://interactivepython.org/courselib/static/pythonds/index.html)
2. [Top 10 Graph Algorithms](http://www.cnblogs.com/v-July-v/archive/2011/02/14/1983678.html)

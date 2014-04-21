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
```

## 1. searching

### BFS
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

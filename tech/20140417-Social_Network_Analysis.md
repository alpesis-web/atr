Apr 17 2014 | SNA, algorithms | Kelly Chan
# Social Network Analysis

table of contents
- 1. A Social Network Magic Trick
- 2. Growth Rates in Social Networks
- 3. Basic Graph Algorithms
- 4. It's Who You Know
- 5. Strong and Weak Bonds
- 6. Hardness of Network Problems

## 1. A Social Network Magic Trick

### eulerian path

applications
- seven bridges
- one stroke

even nodes must have an eulerian path
- node:
- path: 
- degree: odd/even

eulerian path  
eulerian tour  

## 2. Growth Rates in Social Networks

- nodes/vertices
- edges/links

|           | euler   | 
|:----------|:--------|
| nodes/n   | n       | 
| edges/m   | n-1     | 
| cycles    |         | 
| regions/r | n-m+r=2 | 
| degree    |         |  

growth rate
- n-m+r=2
- 3r <= 2m, r <= 2/3m
- m + 2 = m + r <= n + 2/3m
- 3m + 6 <= 3n + 2m
- m <= 3n - 6

|           | chain network | ring network | grid network   | planar graph | complete graph | hyper cube | tree graph |
|:----------|:--------------|:-------------|:---------------|:-------------|:---------------|:-----------|:-----------|
| nodes/n   | n             | n            | n              | n            | n              | n          | n          |
| edges/m   | n-1           | n            | 2n - 2\*sqrt(n) |             | n\*(n-1)/2     | 1/2*nlogn  |            |
| cycles    |               |              | 2*edges        |              |                |            |            |
| regions/r |               |              |                | n-m+r=2      |                |            |            |
| degree    |               |              |                |              |                | logn       |            |
- tree graph: connected but no cycles
- randomly generated graphs: erdos-renyi model
- recursive graphs: 
- tangled hypercube


## 3. Basic Graph Algorithms
## 4. It's Who You Know
## 5. Strong and Weak Bonds
## 6. Hardness of Network Problems

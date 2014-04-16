Apr 16 2014 | Machine_Learning | Kelly Chan
# Machine Learning: Unsupervised Learning

Table of Contents
- 1. Randomized Optimization
- 2. Clustering
- 3. Feature Selection
- 4. Feature Transformation
- 5. Info Theory


## 1. Randomized Optimization

Space X, f(x)max = maxF(x)  

find the best:
- factory, chemical, process control
- route finding
- root finding
- neural network
- decision tree

solutions:
- generate 8 test: small input space, complex function
- calculus: function has derivative, soluable = 0
- Newton's Method: function has derivative, iterately, single optima

Hard:
- big input space
- complex function
- no derivative (or hard to find)
- possibly many small optima

Random restart hillclimbing
- multple tries to find a good starting place
- not much more expensive (constant factor)

Annealing Algorithm
- find a finite set of iterations:
- sample new point x in N(x)
- jump to new sample with probability given by an acceptable probability function P(x, xt, T)
- decrease temperature T

Genetic Algorithms  
GA Skeleton  
MIMIC  



## 2. Clustering
## 3. Feature Selection
## 4. Feature Transformation
## 5. Info Theory

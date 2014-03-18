Mar 18 2014 | ML, supervised_learning | Kelly Chan
# Machine Learning (Supervised Learning)

table of contents
- 1. Decision Trees
- 2. Regression & Classification
- 3. Neural Networks
- 4. Instance Based Learning - knn
- 5. Ensemble B&B
- 6. Kernel Methods & SVMs
- 7. Comp Learning Theory
- 8. VC Dimensions
- 9. Bayesian Learning/Inference

## 1. Decision Trees

algorithms (ID3):  
- step1. choose a best attribute <- entropy
- step2. split data
- step3. if good, stop; else, iterate
     - output: vote
     - when to stop?
         - everything classified correctly
         - no more attributes
         - no overfitting


notes:
- attribute can be repeated in a tree
- outputs: average, local linear fit


## 2. Regression & Classification

data:

| x   | y   |
|-----|-----|
| x1  | y1  |
| x2  | y2  |
| x3  | y3  |
| ... | ... |
| xn  | yn  |

algorithms:
- linear regression: f = ax + b
- polynomial regression: f(x) = c0 + c1x + c2x^2 + ... + cnx^n


### Linear Regression

functions:
- f = ax + b
- loss error: sum(y_i - c)^2
- best constant = mean (squared error)

approvement:  
- step1. f(x) = c
- step2. E(c) = sum(y_i - c)^2  
- step3. d(E(c)) / dc = sum( 2 * (y_i - c) * (-1) )  
- step4. \- sum( 2 * (y\_i -c) * (-1) ) = 0 --> n * c = sum(y\_i) --> c = sum(y\_i) / n = mean  
- step5. sum(y_i) - sum(c) = 0  


### Polynomical Regression

order of polynomial:  
- f(x) = c0 + c1x + c2x^2 + ... + cnx^n
- degrees:
    - k = 0: constant
    - k = 1: line
    - k = 2: parabola
    - k = 3: cubic
    - k = 8: octic
- example:
    - c0 + c1x + c2x^2 + c3x^3 = y
    - X * w = Y
    - [1, x1, x1^2, x1^3] * [c0, c1, c2, c3].T ~ [y1]
    - [1, x2, x2^2, x2^3] * [c0, c1, c2, c3].T ~ [y2]
    - [1, x3, x3^2, x3^3] * [c0, c1, c2, c3].T ~ [y3]
    - [1, ..., ..., ...]  * [c0, c1, c2, c3].T ~ [...]
    - [1, xn, xn^2, xn^3] * [c0, c1, c2, c3].T ~ [yn]
- weights:
    - X * w = Y
    - X^T * X * w = X^T * Y
    - (X^T * X)^(-1) * (X^T * X) * w = (X^T * X)^(-1) * X^T * Y
    - w = (X^T * X)^(-1) * X^T * Y
- errors: f + error
    - sensor error
    - malrciously - being given bad data
    - transcription error
    - unmodeled influences
- cross validation: split data by folds


## 3. Neural Networks

neural networks
```
theta: perceptron unit --> threshold -- sigmoid units - hidden layer

x1 - (w1) --|
x2 - (w2) --| ---> (theta) -------------------------> y
x3 - (w3) --| 
```

### Perceptron

theta = 0, return yes|y=1, no|y=0  

|   | 1   |   2 |   3  |
|---|-----|-----|------|
| x | 1   |   0 | -1.5 |
| w | 1/2 | 3/5 | 1    |

solution: x1 \* w1 + x2 \* w2 + x3 \* w3 = 1\*1/2 + 0\*3/5 - 1.5\*1 = -1    ==> y=0  

perceptron unit:
- and/or/not: repeat anything
- xor: evil function, xor = or - and

| x1 | x2 | AND | OR | XOR |
|----|----|-----|----|-----|
| 0  | 0  | 0   | 0  | 0   |
| 0  | 1  | 0   | 1  | 0   |
| 1  | 0  | 0   | 1  | 0   |
| 1  | 1  | 1   | 1  | 1   |

perceptron training: finds weights that map inputs to outputs
- perceptron rule <- threshold - guarantee, finite, linear
- gradient descent/ delta rule <- unthreshold - calculus, robust, local, optimum

differetiable threshold
- sigmoid: 1/1+e^(-a), interval [(-, +), (0, 1)]

### Weights

optimizing weights  

### Model Summary
restriction/perference bias


## 4. Instance Based Learning - knn

k nearest neighbors /knn:
- function: f(x) = lookup(x)
- factors:
    - d() - distances <- similarity
        - euclidean
        - manhanttan
    - k
    - average
- returns:
    - classification
    - regression

## 5. Ensemble B&B
## 6. Kernel Methods & SVMs
## 7. Comp Learning Theory
## 8. VC Dimensions
## 9. Bayesian Learning/Inference

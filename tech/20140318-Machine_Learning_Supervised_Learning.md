Mar 18 2014 | ML, supervised_learning | Kelly Chan
# Machine Learning (Supervised Learning)

table of contents
- 1. Decision Trees
- 2. Regression & Classification
- 3. Neural Networks
- 4. Instance Based Learning
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

function:
- f = ax + b
- loss error: sum(y_i - c)^2

calculations:  
- step1. f(x) = c
- step2. E(c) = sum(y_i - c)^2  
- step3. d(E(c)) / dc = sum( 2 * (y_i - c) * (-1) )  
- step4. \- sum( 2 * (y\_i -c) * (-1) ) = 0 --> n * c = sum(y\_i) --> c = sum(y\_i) / n = mean  
- step5. sum(y_i) - sum(c) = 0  

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
- dfd


## 3. Neural Networks
## 4. Instance Based Learning
## 5. Ensemble B&B
## 6. Kernel Methods & SVMs
## 7. Comp Learning Theory
## 8. VC Dimensions
## 9. Bayesian Learning/Inference

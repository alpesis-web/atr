Jan 25 2014 | Forecasting, Regression | Kelly Chan
# Forecasting with Regression

Table of Contents
- linear regression
- tree-based regression

## 1. Linear Regression

Summary  
Pros: Easy to interpret results, computationally inexpensive  
Cons: Poorly models nonlinear data  
Data: Numeric values, nominal values  

Data Type  

| feature1  | feature2  | target    |
|:---------:|:---------:|:---------:|
| 1.000000  | 0.067732  | 3.176513  |
| 1.000000  | 0.427810  | 3.816464  |
| 1.000000  | 0.995731  | 4.550095  |
| 1.000000  | 0.738336  | 4.256571  |
| 1.000000  | 0.981083  | 4.560815  |
| 1.000000  | 0.526171  | 3.929515  |
| 1.000000  | 0.378887  | 3.526170  |



Maths  
- regression equation: Y = X^T * W
- W = (X^T \* X)^(-1) \* X^T * Y
- locally weighted linear regression (LWLR): wHat = (X^T * W * X)^(-1) * X^T * W * y
- kernel: exp (|xi - x|/(-2k^2))

Algorithm  



## 2. Tree-based Regression


Summary  
Pros: Easy to interpret results, computationally inexpensive  
Cons: Poorly models nonlinear data  
Data: Numeric values, nominal values  

Data Type  


Maths  

Algorithm  


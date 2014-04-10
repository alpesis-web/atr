Apr 7 2014 | Data_Transformation | Kelly Chan
# Data Transformations

### 1. Logarithmic transformation

non-normal distribution -> normal distribution
- newX = ln(X + 1)
- xhat = e^(newX) - 1

| 10-based                           | log-based     |
|:-----------------------------------|:--------------|
| 10 raised to the power of 1 = 10   | log(10)10=1   |
| 10 raised to the power of 2 = 100  | log(10)100=2  |
| 10 raised to the power of 3 = 1000 | log(10)1000=3 |


When running linear regression models using GDP, as the data are often positively skewed, so log transformation is often adopted to solve this problem. Ex:

| 10-based                | log-based                |
|:------------------------|:-------------------------|
| GDP of Country A = 10   | Log GDP of Country A = 1 |
| GDP of Country B = 100  | Log GDP of Country B = 2 |
| GDP of Country C = 1000 | Log GDP of Country C = 3 |

So your data will look more normally distributed.

### 2. Square root transformation
### 3. Arcsine transformation
### 4. Reciprocal transformation
### 5. Squared transformation

--- 
### References
1. [Data Transformations](http://www.anselm.edu/homepage/jpitocch/transform/transforms.html)

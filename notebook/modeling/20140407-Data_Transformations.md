Apr 7 2014 | Data_Transformation | Kelly Chan
# Data Transformations

Preprocessing
- train faster
- avoid saturation
- reduce the chances of getting stuck in local optima

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

Some type of non-linearity in the data that can be somehow "compensated". The logarithmic and square root scaling are usually performed when the data is characterized by "bursts", i.e. the data is well grouped in low values, but some portion of it has relatively larger values. 

If input has negative values we cannot use the square root transformation unless a constant is added making all of them non negatives.

### 3. Arcsine transformation

used to normalize data in percentages or proportions whose distributions fits the binomial distribution.

### 4. Reciprocal transformation

sed when standard deviation is proportional to the square of the mean.

### 5. Squared transformation

used when standard deviation decreases as the mean increases.

### 6. Normalization

Always normalization is important and necessary. Normalization consists on either moving your data into the interval [0,1], or by making the norm-2 of the data equal to 1. 

- Z-score 
- Min-Max normalization

### Notes

You can introduce even stronger non-linearities into your data that will be harder to compensate later by your model. So, just use them only when you know that it actually corresponds to some type of non-linearity in your data.

We should be more cautious in using some terms such as transformation and normalization or data reduction and normalization. As an example transformation for one scientist may mean rotation, scaling, and moving. Normalization is to change a range of number from one representation to another. Sometime feature reduction is done if you have a large dimension of data.

--- 
### References
1. [Data Transformations](http://www.anselm.edu/homepage/jpitocch/transform/transforms.html)

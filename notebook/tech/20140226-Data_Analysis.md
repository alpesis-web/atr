Feb 26 2014 | data_analysis, statistics | Kelly Chan
# Data Analysis

### 1. Normal Distribution

f(x) = 1/sqrt( 2 * pi * std^2 ) * exp( -(x-u)^2 / 2 * std^2 )

- u: mean
- std: standard deviation
- variance: std^2


### 2. T-test

t = (u1 - u2) / sqrt( variance1/N1 + variance2/N2 )  
r = ( variance1/N1 + variance2/N2 ) / ( variance^2/ v1*N1^2 + variance^2/ v2*N2^2 )  
v = N-1 (degree of freedom)

t & r -> p  

python
```python
import scipy.stats
scipy.stats.ttest_ind(list_1, list_2, equal_var=False)
```

### 3. U-test

- U Test (non parametric test): `U, P = scipy.stats.mannwhitneyu(x,y)`
- Shapiro-Wilk Test (non normal data): `W, P = scipy.stats.shapiro(data)`

### 4. Machine Learning

- Statistics: focused on analyzing existing data, and drawing valid conclusions
- Machine Learning: focused on making predictions

data -> model -> predictions
- supervised learning
    - examples with input and output
    - predict output for future
    - classification
    - regression
- unsupervised learning
    - trying to understand the structure of data
    - clustering

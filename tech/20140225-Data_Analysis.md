Feb 25 2014 | data_analysis, statistics | Kelly Chan
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

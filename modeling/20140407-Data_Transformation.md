Apr 7 2014 | Data_Transformation | Kelly Chan
# Data Transformation

### 1. Log Transformation

non-normal distribution -> normal distribution

When using 10 as base:
10 raised to the power of 1 = 10
10 raised to the power of 2 = 100
10 raised to the power of 3 = 1000

S0:
log(10)10=1
log(10)100=2
log(10)1000=3

When running linear regression models using GDP, as the data are often positively skewed, so log transformation is often adopted to solve this problem. Ex:

GDP of Country A = 10
GDP of Country B = 100
GDP of Country C = 1000

If we tranform GDP data into log form, the results will be:

Log GDP of Country A = 1
Log GDP of Country B = 2
Log GDP of Country C = 3

So your data will look more normally distributed.

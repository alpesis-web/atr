Mar 17 2014 | operation, warranty, time_series | Kelly Chan
# Warranty Data Analysis

### 1. Data Types

reliability data
- life data
- time-to-failure (TTF) data <- non-repairable
- time-between-failure (TBF) data <- repairable
- survival data
- event-time data
- degradation data

censored data
- exact failure times are not known
- types: right/left/interval censoring

### 2. Distributions

hazard function (rate):  
h(t) = f(t) / (1-F(t)) = f(t)/R(t)

distributions of reliability:
- weibull
- exponential
- lognormal
- gamma
- binomial
- logistic

#### (1) exponential distribution

calculations:
- pdf: f(t) = lambda * e^(-lambda*t)
- cdf: F(t) = 1 - e^(-lambda*t)
- reliability: R(t) = e^(-lambda*t)
- hazard rate: h(t) = lambda = inverse of MTTF (mean-time-to-failure)
- MTTF: MTTF = 1/lambda = sigta
- quantile: F^(-1)(p) = (1/lambda)[-ln(1-p)]

applications:
- constant hazard rate implies that the probability that a unit will fail in the next instant does not depend on the unit's age
- reasonable for many electronic components that do not wear out
- usually inappropriaate for modeling TTF of mechanical components that are subject to fatigue, corrosion, or wear


#### (2) weibull distribution

    
2. Degradation Models
    - linear: y=ax+b
    - exponential: y=b*e^(ax)
    - power: y=b*x^a
    - logarithmic: y=a*ln(x)+b
    - gompertz: y=a*b^(cx)
    - lloyd-lipow: y=a-b/x
3. dd




Table of Contents
- 1. Nevada Chart Format
- 2. Time-to-Failure Format
- 3. Dates of Failure Format
- 4. Usage Format

## 1. Nevada Chart Format
## 2. Time-to-Failure Format
## 3. Dates of Failure Format
## 4. Usage Format

---
### References
- 1. [Warranty Data Analysis](http://reliawiki.org/index.php/Warranty_Data_Analysis)
- 2. [Predicting Product Life Using Reliability Analysis Methods](http://www.slideshare.net/ASQwebinars/predicting-product-life-using-reliability-analysis-methods)

Apr 1 2014 | Time_Series | Kelly Chan
# Time Series Forecasting

### 1. Data
- random
- Level (long-term average): data fluctuates around a constant mean
    - Naive: Ft+1 = At (the last value)
    - Simple Mean: Ft+1 = sum(A1..t)/N
- Trend: data exhibits an increasing or decreasing pattern
    - Moving Average: Ft+1 = sum(An...t) / N
    - Weighted Moving Average: Ft+1 = sum(WtAt)
    - Exponential Smoothing: Ft+1 = alpha * At + (1-alpha) * Ft 
        - At: last actual value
        - Ft: last forecast value
        - alpha: smoothing coefficient
    - Forecast including trend = smooth the level of the series + smooth the trend
        - FIT = St + Tt
        - (level) St = alpha * At + (1-alpha) * (St-1 + Tt-1)
        - (trend) Tt = beta * (St - St-1) + (1-beta) * Tt-1
- Seasonality: any pattern that regularly repeats itself and is of a constant length
- Cycle: patterns created by economic fluctuations 


### 2. Methods
- Regressions
    - linear regression
        - formula: Y = aX + b
        - b = (sum(xy) - n * xMean * yMean)  / (sum(x^2) - n * xMean^2)
        - a = yMean - b * xMean
    - survival regression
        - lambda(t) = b0(t) * exp(b1x1 + b2x2 + ... + bnxn)
        - lambda(t) = b0(t) + b1(t)x1 + b2(t)x2 + ... + bn(t)xT
- Time Series
    - Naive: recent value
    - (n/ weights) Moving Average: simple/ weighted
        - applications: little/ no trend, smoothing
        - period: Ft+1 = 1/n * (At + At-1 + At-2 + ... + At-n+1) <- 3-period?
        - weighted: Ft+1 = w1At + w2At-1 + ... + wnAt-n+1 <- weights = 1
    - (alpha) Expoential Smoothing: level/ trend/ seasonality
        - level: Ft+1 = Ft + alpha * (At - Ft) <- alpha: how important of recent data
        - weighted: Ft+1 = alpha * At + (1-alpha) * At-1 + alpha * (1-alpha)^2 * At-2 + ...
        - trend: FITt = Ft + Tt = [FITt-1 + alpha* (At-1 - Ft-1)] + [Tt-1 + eta * (Ft - FITt-1)]

### 3. Errors
- (MAD) Mean Absolute Deviation: 1/n * sum(At-Ft)
- (MSE) Mean Squared Error: 1/n * sum((At-Ft)^2)
- (RMSE) Root Means Squared Error: sqrt(MSE)

### 4. Bias
- TS = RSFE / MAD = sum(At-Ft) / MAD

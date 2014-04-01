Apr 1 2014 | Time_Series | Kelly Chan
# Time Series Forecasting

### 1. Data
- random
- trend
- seasonal
- composite

### 2. Methods
- Regressions
- Time Series
    - Naive: recent value
    - (n/ weights) Moving Average: simple/ weighted
        - applications: little/ no trend, smoothing
        - period: Ft+1 = 1/n * (At + At-1 + At-2 + ... + At-n+1) <- 3-period?
        - weighted: Ft+1 = w1At + w2At-1 + ... + wnAt-n+1 <- weights = 1
    - (alpha) Expoential Smoothing: level/ trend/ seasonality
        - level: Ft+1 = Ft + alpha * (At - Ft) <- alpha: how important of recent data
        - weighted: Ft+1 = alpha * At + (1-alpha) * At-1 + alpha * (1-alpha)^2 * At-2 + ...

### 3. Errors
- (MAD) Mean Absolute Deviation: 1/n * sum(At-Ft)
- (MSE) Mean Squared Error: 1/n * sum((At-Ft)^2)
- (RMSE) Root Means Squared Error: sqrt(MSE)

### 4. Bias
- TS = RSFE / MAD = sum(At-Ft) / MAD

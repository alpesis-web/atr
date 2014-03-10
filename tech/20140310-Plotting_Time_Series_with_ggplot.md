Mar 10 2014 | visualization, time_series, ggplot | Kelly Chan
# Plotting Time Series with ggplot

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *
```

### 1. index

setting index
```python
meat = meat.dropna(thresh=800, axis=1) # drop columns that have fewer than 800 observations
ts = meat.set_index(['date'])

print ts.head(10)
```

### 2. Grouping
grouping by year: `ts.groupby(ts.index.year).sum().head(10)`  
grouping by decade: `the1940s = ts.groupby(ts.index.year).sum().ix['1940-01-01':'1949-12-31']`

grouping by floor division
```python
def floor_decade(date_value):
    "Takes a date. Returns the decade."
    return (date_value.year // 10) * 10

pd.to_datetime('2013-10-09')
floor_decade(_)
ts.groupby(floor_decade).sum()
```

### 3. reindex and plotting
reindex: `the1940s.sum().reset_index(name='meat sums in the 1940s')`

plotting by reindex
```python
by_decade = ts.groupby(floor_decade).sum()
by_decade.index.name = 'year'
by_decade = by_decade.reset_index()

ggplot(by_decade, aes('year', weight='beef')) + \
    geom_bar() + \
    scale_y_continuous(labels='comma') + \
    ggtitle('Head of Cattle Slaughtered by Decade')
```

plotting by melt
```python
by_decade_long = pd.melt(by_decade, id_vars="year")

ggplot(aes(x='year', weight='value', colour='variable'), data=by_decade_long) + \
    geom_bar() + \
    ggtitle("Meat Production by Decade")
```

trends over time
```python
from ggplot import meat
meat_lng = pd.melt(meat, id_vars=['date'])
ggplot(aes(x='date', y='value', colour='variable'), data=meat_lng) + geom_line()
```

smoothing
```python
ggplot(aes(x='date', y='value', colour='variable'), data=meat_lng) + \
    stat_smooth(span=0.10) + \
    ggtitle("Smoothed Livestock Production")
```

---
### Reference
- [Aggregating & plotting time series in python](http://blog.yhathq.com/posts/aggregating-and-plotting-time-series-in-python.html)

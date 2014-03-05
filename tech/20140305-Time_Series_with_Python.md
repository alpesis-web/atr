Mar 5 2014 | python, data_analysis, time_series | Kelly Chan
# Time Series with Python

## 1. Date and Time

getting datetime from system
```python
from datetime import datetime
now = datetime.now()
now.year, now.month, now.day
```

calculating delta between days
```python
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta.days
delta.seconds

from datetime import timedelta
start = datetime(2011, 1, 7)
start + timedelta(12)
start - 2 * timedelta(12)
```

converting between datetime and string
```python

# 1. converting with strftime

stamp = datetime(2011, 1, 3)
str(stamp)
stamp.strftime('%Y-%m-%d')

value = '2011-01-03'
datetime.strptime(value, '%Y-%m-%d')

datestrs = ['7/6/2011', '8/6/2011']
[datetime.strptime(x, '%m/%d/%Y') for x in datestrs]


# 2. converting with parse
from dateutil.parser import parse
parse('2011-01-03')
parse('Jan 31, 1997 10:45 PM')
parse('6/12/2011', dayfirst=True)


# 3. coverting with pandas
pandas.to_datetime(datestrs)
idx = pd.to_datetime(datestrs + [None])
idx
idx[2]
pandas.isnull(idx)
```

## 2. Time Series Basic

creating dates with pandas
```python
from datetime import datetime

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), 
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pandas.Series(np.random.randn(6), index=dates)
ts

type(ts)
ts.index
ts.index.dtype

stamp = ts.index[0]
stamp
```

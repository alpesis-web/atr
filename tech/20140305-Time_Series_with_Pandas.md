Mar 5 2014 | pandas, data_analysis, time_series | Kelly Chan
# Time Series with Pandas

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

indexing, selection, subsetting
```python
stamp = ts.index[2]
ts[stamp]
ts['1/10/2011']
ts['20110110']

longer_ts = pandas.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
longer_ts['2001']
longer_ts['2001-05']

ts[datetime(2011, 1, 7):]
ts['1/6/2011':'1/11/2011']

ts.truncate(after='1/9/2011')

dates = pandas.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pandas.DataFrame(np.random.randn(100, 4), index=dates, columns=['Colorado', 'Texas', 'New York', 'Ohio'])
```

time series with duplicate indices
```python
dates = pandas.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = pandas.Series(np.arange(5), index=dates)
dup_ts.index.is_unique
dup_ts['1/3/2000']
dup_ts['1/2/2000']

grouped = dup_ts.groupby(level=0)
grouped.mean()
grouped.count()
```

date ranges, frequencies, shifting
```python

# 1. resample
ts
ts.resample('D')

# 2. date_range
index = pandas.date_range('4/1/2012', '6/1/2012')

pandas.date_range(start='4/1/2012', periods=20)
pandas.date_range(end='6/1/2012', periods=20)
pandas.date_range('1/1/2000', '12/1/2000', freq='BM')

pandas.date_range('5/2/2012 12:56:31', periods=5)
pandas.date_range('5/2/2012 12:56:31', periods=5, normalize=True)

# 3. frequencies

from pandas.tseries.offsets import Hour, Minute
hour = Hour()
four_hours = Hour(4)
pandas.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')

Hour(2) + Minute(30)
pandas.date_range('1/1/2000', periods=10, freq='1h30min')

# 4. week of month
rng = pandas.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
list(rng)

# 5. shifting (leading/lagging)
ts = pandas.Series(np.random.randn(4),index=pandas.date_range('1/1/2000', periods=4, freq='M'))
ts.shift(2)
ts.shift(-2)
ts.shift(2, freq='M')
ts.shift(3, freq='D')
ts.shift(1, freq='3D')
ts.shift(1, freq='90T')

# shifting dates with offsets
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()
now + MonthEnd()
now + MonthEnd(2)

offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)

ts = pandas.Series(np.random.randn(20),index=pandas.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()
ts.resample('M', how='mean')
```

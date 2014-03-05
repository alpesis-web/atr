Mar 5 2014 | python, data_analysis, time_series | Kelly Chan
# Time Series with Python

## 1. Date and Time

datetime
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

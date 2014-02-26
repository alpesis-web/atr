Feb 26 2014 | data_wrangling | Kelly Chan
# Data Wrangling

### 1. csv data

```python
import pandas

baseball_data = pandas.read_csv('master.csv')
print baseball_data['nameFirst']

baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']

baseball_data.to_csv('baseball_data_height_plus_weight.csv')
```

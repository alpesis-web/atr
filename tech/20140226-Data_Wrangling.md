Feb 26 2014 | data_wrangling | Kelly Chan
# Data Wrangling

- Files
- Databases
- APIs

### 1. csv data

loading and writing csv data by pandas
```python
import pandas

baseball_data = pandas.read_csv('master.csv')
print baseball_data['nameFirst']

baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']

baseball_data.to_csv('baseball_data_height_plus_weight.csv')
```

### 2. relational databases

sql query
```sql
SELECT district, subdistrict FROM aadhaar_data LIMIT 20;
SELECT * from aadhaar_data WHERE state == 'xxx';
SELECT district, SUM(aadhaar_generated) FROM aadhaar_data GROUP BY district;
```

### 3. API

extracting data from JSON
```python
import json
import requests

if __name == "__main__":
    url = 'xxx'
    data = requests.get(url).text
    print type(data)
    print data
    data['artist']
```

### 4. imputation for missing values


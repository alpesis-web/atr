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

imputating values for missing by mean
```python
from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    
    #YOUR CODE GOES HERE
    m = numpy.mean(baseball['weight'])
    baseball['weight'] = baseball['weight'].fillna(m)

    return baseball
```

Mar 5 2014 | pandas, data_analysis | Kelly Chan
# Ten Minutes to Pandas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### 1. Object Creation

creating array
```python
s = pd.Series([1,3,5,np.nan,6,8])
```
creating dates with dataframe
```python
dates = pd.date_range('20130101',periods=6)
```
creating dataframe
```python
df2 = pd.DataFrame({ 'header1' : 1.,
                     'header2' : pd.Timestamp('20130102'),
                     'header3' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'header4' : np.array([3] * 4,dtype='int32'),
                     'header5' : 'foo' })
```
checking datatypes of dataframe
```
dataframe.dtypes
```

### 2. Viewing Data

top/bottom rows of data
```python
dataframe.head()
dataframe.tail(3)
```
index/row, columns and values
```python
dataframe.index
dataframe.columns
dataframe.values
```
(R) summary of numeric data
```python
dataframe.describe()
```
data transpose
```python
dataframe.T
```
sorting by header/names and values
```python
dataframe.sort_index(axis=1, ascending=False)
dataframe.sort(columns='columnName')
```

### 3. Selection

getting data by column: `dataframe['A']`  
getting data by rows
```python
dataframe[0:3]
dataframe['20130102':'20130104']
```

Mar 5 2014 | pandas, data_analysis | Kelly Chan
# Ten Minutes to Pandas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## 1. Object Creation

creating array: `s = pd.Series([1,3,5,np.nan,6,8])`  
creating dates with dataframe: `dates = pd.date_range('20130101',periods=6)`
creating dataframe
```python
df2 = pd.DataFrame({ 'header1' : 1.,
                     'header2' : pd.Timestamp('20130102'),
                     'header3' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'header4' : np.array([3] * 4,dtype='int32'),
                     'header5' : 'foo' })
```
checking datatypes of dataframe: `dataframe.dtypes`

## 2. Viewing Data

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
(R) summary of numeric data: `dataframe.describe()`  
data transpose: `dataframe.T`  
sorting by header/names and values
```python
dataframe.sort_index(axis=1, ascending=False)
dataframe.sort(columns='columnName')
```

## 3. Selection

getting data by column: `dataframe['A']`  
getting data by rows
```python
dataframe[0:3]
dataframe['20130102':'20130104']
```
reshaping dataframe: `dataframe.loc[:,['A','B']]`  
getting one record with T: `dataframe.iloc[3]`  
getting rows and columns as defined: 
```python
dataframe.iloc[3:5,0:2]
dataframe.iloc[[1,2,4],[0,2]]
dataframe.iloc[1:3,:]
dataframe.iloc[:,1:3]
```
getting specific value/cell: `dataframe.iloc[1,1]` or `dataframe.iat[1,1]`

## 4. Boolean Indexing

filtering data by a single column: `df[df.A > 0]`  
filtering data by all columns: `df[df > 0]`, if value <= 0, it will return NaN

## 5. Setting

setting values by label, position, array
```python
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.loc[:,'D'] = np.array([5] * len(df))

df2 = df.copy()
df2[df2 > 0] = -df2
```

rename columns: `df = df.rename(columns={'$a': 'a', '$b': 'b'}, inplace=True)`  


## 6. Missing Values

dropping any rows that have missing values: `df1.dropna(how='any')`  
filling missing values: `df1.fillna(value=5)`  
getting the boolean mask where values are nan: `pd.isnull(df1)`

## 7. Operations

mean: `df.mean()`  
frequency count: `df['A'].value_counts()`  
correlation: `df.corr()` 

string: `s.str.lower()`

## 8. Merge

merging data by rows: `pieces = [df[:3], df[3:7], df[7:]]`  
join
```python
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
```
append
```python
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
df.append(s, ignore_index=True)
```

## 9. Grouping

(histogram)/grouping all columns by one column: `df.groupby('A').sum()`  
(cross tabs)/grouping all columns by multi-columns: `df.groupby(['A','B']).sum()`

## 10. Reshape

stack
```python
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
stacked = df2.stack()
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)
```

pivot table
```python
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
                   
pd.pivot_table(df, values='D', rows=['A', 'B'], cols=['C'])                   
```

## 11. Getting Data In/Out

csv in/out
```python
pd.read_csv('foo.csv')
df.to_csv('foo.csv')
```
excel in/out
```python
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
df.to_excel('foo.xlsx', sheet_name='Sheet1')
```
HDF5 in/out
```python
d.read_hdf('foo.h5','df')
df.to_hdf('foo.h5','df')
```


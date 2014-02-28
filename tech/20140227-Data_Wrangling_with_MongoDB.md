Feb 27 2014 | MongoDB, data_wrangling | Kelly Chan
# Data Wrangling with MongoDB

table of contents
- 1. Data Extraction
- 2. Data in Complex Format
- 3. Data Quality
- 4. Working with MongoDB
- 5. Data Analysis

## 1. Data Extraction

parsing csv file with pyhon
```python
def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

        fields = line.split(",")
        entry = {}
        
        for i, value in enumerate(fields):
            entry[header[i].strip()] = value.strip()

        data.append(entry)
        counter += 1
        
    return data
```

parsing excel file with python
```python
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in rnage(sheet.nrows)]
    
    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)
    
    maxval = max(cv)
    minval = min(cv)
    
    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1
    
    maxtime = sheet.cell_value(maxpos, 0)
    realmaxtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)
    
    data = {
            'maxtime': mrealmaxtime,
            'maxvalue': maxval,
            'mintime': realmintime,
            'minvalue': minval,
            'avgcoast': sum(cv) / float(len(cv))
    }
    
    return data

```

## 2. Data in Complex Format
## 3. Data Quality
## 4. Working with MongoDB
## 5. Data Analysis

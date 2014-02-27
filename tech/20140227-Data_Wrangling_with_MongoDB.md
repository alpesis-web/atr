Feb 27 2014 | MongoDB, data_wrangling | Kelly Chan
# Data Wrangling with MongoDB

table of contents
- 1. Data Extraction
- 2. Data in Complex Format
- 3. Data Quality
- 4. Working with MongoDB
- 5. Data Analysis

## 1. Data Extraction

csv file
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


## 2. Data in Complex Format
## 3. Data Quality
## 4. Working with MongoDB
## 5. Data Analysis

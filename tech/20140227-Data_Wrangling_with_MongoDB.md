Feb 27 2014 | MongoDB, data_wrangling | Kelly Chan
# Data Wrangling with MongoDB

table of contents ([source codes](https://github.com/KellyChan/Python/tree/master/examples/Data%20Wrangling%20with%20MongoDB))
- 1. Data Extraction
- 2. Data Quality
- 3. Working with MongoDB
- 4. Data Analysis

## 1. Data Extraction

- csv/xls: tabular
- json: dictionary
- xml: tree

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

parsing json file with python
```python
# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    artist_id = results["artist"][1]["id"]
    print "\nARTIST:"
    pretty_print(results["artist"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print "\nALL TITLES:"
    for t in release_titles:
        print t


if __name__ == '__main__':
    main()

```

## 2. Data Quality
## 3. Working with MongoDB
## 4. Data Analysis

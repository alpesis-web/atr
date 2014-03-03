Feb 27 2014 | MongoDB, data_wrangling | Kelly Chan
# Data Wrangling with MongoDB

table of contents ([source codes](https://github.com/KellyChan/Python/tree/master/examples/Data%20Wrangling%20with%20MongoDB))
- 1. Data Extraction
- 2. Data Cleaning
- 3. Data Analysis with MongoDB

## 1. Data Extraction

- csv/xls: tabular
- json: dictionary
- xml: tree

#### parsing csv file with pyhon
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

cssv.reader() and next() for looping
```python
def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        r = csv.reader(f)
        name = r.next()[1]
        header = r.next()
        data = [row for row in r]

    return (name, data)
```

#### parsing excel file with python
```python
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    
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

parsing data by columns and csv.writer()
```python
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)

        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval,
                         "maxtime": realtime}

    print data
    return data

def save_file(data, filename):
    with open(filename, "w") as f:
        w = csv.writer(f, delimiter='|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
            year, month, day, hour, _ , _= data[s]["maxtime"]
            w.writerow([s, year, month, day, hour, data[s]["maxval"]])
```

#### parsing json file with python
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

getting (key, value) by loopings
```python
def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]

    for article in data:
        section = article["section"]
        title = article["title"]
        titles.append({section: title})
        if "media" in article:
            for m in article["media"]:
                for mm in m["media-metadata"]:
                    if mm["format"] == "Standard Thumbnail":
                        urls.append(mm["url"])
    return (titles, urls)
```

#### parsing xml file with python 
```python
def get_author(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')
        for i in insr:
            data["insr"].append(i.attrib["iid"])
        authors.append(data)

    return authors
```

#### parsing data from html
- step1. make data lists
- step2. download data by HttpReuqest
- step3: parse data

```python
def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    return data
```

BeautifulSoup  
extracting values from option
```python
contents = [str(x.text) for x in soup.find(id="start_dateid").find_all('option')]
```
extracting values from table \<tr> and \<td>
```python
def process_file(f):

    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    
    with open("{}/{}".format(datadir, f), "r") as html:
       
        soup = BeautifulSoup(html)
        dataTDRight = soup.find("table", {"class" : "dataTDRight"})
        
        records = []
        for row in dataTDRight.findAll('tr'):
            cols = row.findAll('td')
            
            if cols[1].string.strip() == "Month" or cols[1].string.strip() == "TOTAL":
                continue
            else:
                year = int(cols[0].string.strip())
                month = int(cols[1].string.strip())
                domestic = int(cols[2].string.strip().replace(',', ''))
                international = int(cols[3].string.strip().replace(',',''))
            
 
            record = {
                  "courier": info["courier"],
                  "airport": info["airport"],
                  "year": year,
                  "month": month,
                  "flights": {
                               "domestic": domestic,
                               "international": international
                            }
            }
            records.append(record)
    data.append(records)    
    return data

```

## 2. Data Cleaning
## 3. Data Analysis with MongoDB

MongoDB: NoSQL database
- Python: dictionary
- PHP: arrays
- Ruby: hashes



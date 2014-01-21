Jan 15 2014 | Classification, ML | Kelly Chan
# Classification


### 1. k Nearest Neighbors (kNN)
Summary
- Pros: High accuracy, insensitive to outliers, no assumptions about data
- Cons: Computationally expensive, requires a lot of memory
- Data: Numeric values, nominal values

Data Type  

| Movie Title                | # of kicks | # of kisses | Type of Movie |
|:---------------------------|:-----------|:------------|:--------------|
| California Man             | 3          | 104         | Romance       |
| He’s Not Really into Dudes | 2          | 100         | Romance       |
| Beautiful Woman            | 1          | 81          | Romance       |
| Kevin Longblade            | 101        | 10          | Action        |
| Robo Slayer 3000           | 99         | 5           | Action        |
| Amped II                   | 98         | 2           | Action        |
| ?                          | 18         | 90          | Unknown       |

Algorithm
```

# (classification) kNN
# return the nearest label in k neighbors by computing Euclidean Distance
def knn(testX, trainData, labels, k):
    
    # (testX, trainData) computing Euclidean Distance
    n = trainData.shape[0]
    distanceMatrix = tile(testX, (n,1)) - trainData  # tile: [testX]_n
    distanceMatrix = distanceMatrix**2
    distances = distanceMatrix.sum(axis=1) # axis=0: by cols | aisx=1: by rows
    distances = distances**0.5
    distancesIndex = distances.argsort()  # argsort(): index by ascending values


    # (k, labels) return the nearest label in k neighbors
    kDistances = {}
    for i in range(k):
        label = labels[distancesIndex[i]]
        # counting # of label in k values, .get(key, value), default = 0
        kDistances[label] = kDistances.get(label,0) + 1
    # .iteritems: loop keys, operator.itemgetter(1): sort by values, descending
    kDistances = sorted(kDistances.iteritems(), key=operator.itemgetter(1), reverse = True)
    return kDistances[0][0]
    
```

### 2. Decision Tree
Summary
- Pros: Computationally cheap to use, easy for humans to understand learned results, missing values OK, can deal with irrelevant features
- Cons: Prone to overfitting
- Data: Numeric values, nominal values


Data Type

| row # |Can survive without coming to surface? | Has flippers? | Fish? | 
|:------|:--------------------------------------|:--------------|:------|
| 1     | Yes                                   | Yes           | Yes   |
| 2     | Yes                                   | Yes           | Yes   |
| 3     | Yes                                   | No            | No    |
| 4     | No                                    | Yes           | No    |
| 5     | No                                    | Yes           | No    |

Algorithm



### 3. Bayes
Summary
- Pros:
- Cons:
- Data:

Data Type


Algorithm



### 4. Logistic Regression
Summary
- Pros:
- Cons:
- Data:

Data Type


Algorithm



### 5. Support Vector Machine
Summary
- Pros:
- Cons:
- Data:

Data Type


Algorithm



### 6. AdaBoost Meta-Algorithm

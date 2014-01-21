Jan 15 2014 | Classification, ML | Kelly Chan
# Classification


### 1. k Nearest Neighbors (kNN)
Summary
- Pros: High accuracy, insensitive to outliers, no assumptions about data
- Cons: Computationally expensive, requires a lot of memory
- Data: Numeric values, nominal values


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


Algorithm


### 3. Bayes
Summary
- Pros:
- Cons:
- Data:

### 4. Logistic Regression
Summary
- Pros:
- Cons:
- Data:

### 5. Support Vector Machine
Summary
- Pros:
- Cons:
- Data:

### 6. AdaBoost Meta-Algorithm

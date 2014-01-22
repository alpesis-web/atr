Jan 15 2014 | Classification, ML | Kelly Chan
# Classification
Table of Contents
- 1. K Nearest Negighbors (kNN) - distance
- 2. Decision Tree - feature
- 3. Naive Bayes - probability
- 4. Logistic Regression
- 5. Support Vector Machine
- 6. AdaBoost Meta-Algorithm

Notes: knn needs a lot of computations, naive bayes has less. Decision tree does not work each time.

---

## 1. k Nearest Neighbors (kNN)
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

## 2. Decision Tree
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

```
'''

Function Tree

- classifier
   |
- tree
   |---- majorityLabel
   |---- dataReduction
   |---- featureChoice
   |          |---------- shannonEntropy
   |          |---------- dataReduction
   |
   |
- treeLeaves
- treeDepth
- treeSave
- treeLoad

'''


from math import log
import operator

# shannonEntropy
# return entropy of a specific feature (single) in a dataSet
def shannonEntropy(dataSet, featureIndex):

    # (category: #) counting # of the categories
    featureLabels = {}
    for line in dataSet:
        featureLabel = line[featureIndex]
        if featureLabel not in featureLabels.keys():
            featureLabels[featureLabel] = 0
        featureLabels[featureLabel] += 1

    # (entropy) calculating entropy in the categories
    entropy = 0.0
    n = len(dataSet)
    for key in featureLabels:
        probability = float(featureLabels[key]) / n
        entropy -= probability * log(probability, 2)
    return entropy


# dataReduction
# return dataReduced by a specific feature value (specific feature EXCLUSIVE)
def dataReduction(dataSet, featureIndex, featureValue):
    dataReduced = []
    for line in dataSet:
        if line[featureIndex] == featureValue:
            dataSplit = line[:featureIndex]  # data before featureIndex
            dataSplit.extend(line[featureIndex+1:]) # data (before index + after index)
            dataReduced.append(dataSplit)
    return dataReduced



# featureChoice
# return the bestFeatureIndex by calculating entropy for each feature/col
def featureChoice(dataSet, categoryIndex):

    bestInfoGain = 0.0
    bestFeatureIndex = categoryIndex
    categoryEntropy = shannonEntropy(dataSet, categoryIndex)

    cols = len(dataSet[0]) - 1 # dataSet[0]: the first row, get # of cols
    for col in range(cols):
        featureEntropy = 0.0
        feature = [row[col] for row in dataSet]  # col vector
        featureValues = set(feature) # get dict of values
        for featureValue in featureValues:
            dataReduced = dataReduction(dataSet, col, featureValue) # col EXCLUSIVE
            probability = len(dataReduced) / float(len(dataSet))
            featureEntropy += probability * shannonEntropy(dataReduced, categoryIndex)
        featureInfoGain = categoryEntropy - featureEntropy 
        # featureEntropy smaller, featureInfoGain bigger
        if (featureInfoGain > bestInfoGain):
            bestInfoGain = featureInfoGain
            bestFeatureIndex = col
    return bestFeatureIndex


# majorityLabel
# return majorityLabel in a feature/category vector
def majorityLabel(feature):
    labels = {}
    for label in feature:
        if label not in labels.keys():
            labels[label] = 0
        labels[label] += 1
    labels = sorted(labels.iteritems(), key=operator.itemgetter(1), reverse=True)
    return labels[0][0]


# tree
# return tree by deducting the best feature one by one (recursion)
def tree(dataSet, featureNames, categoryIndex):

    # get the categories vector
    categories = [row[categoryIndex] for row in dataSet]
    # if just one category in the categories
    if categories.count(categories[0]) == len(categories):
        return categories[0]
    # if just one column, return the majorityLabel in the col labels
    if len(dataSet[0]) == 1:
        return majorityLabel(categories)

    # (bestFeatureIndex, bestFeatureName, featureNames) constructing bestFeature 
    bestFeatureIndex = featureChoice(dataSet, categoryIndex)
    bestFeatureName = featureNames[bestFeatureIndex]
    del(featureNames[bestFeatureIndex]) # delete bestFeatureName from featureNames
    
    # (bestFeature, bestFeatureValues)
    bestFeature = [row[bestFeatureIndex] for row in dataSet]
    bestFeatureValues = set(bestFeature)

    # (treeOutput) constructing tree by recursion
    treeCreated = {bestFeatureName: {}}
    for bestFeatureValue in bestFeatureValues:
        subFeatureNames = featureNames[:]
        treeCreated[bestFeatureName][bestFeatureValue] = tree(dataReduction(dataSet, bestFeatureIndex, bestFeatureValue), 
                                                              subFeatureNames, 
                                                              categoryIndex)
    return treeCreated


# treeLeaves
# return # of leaves from treeCreated
def treeLeaves(treeCreated):
    leaves = 0
    root = treeCreated.keys()[0]
    nodes = treeCreated[root]
    for key in nodes.keys():
        if type(nodes[key]).__name__ == 'dict':
            leaves += treeLeaves(nodes[key])
        else:
            leaves += 1
    return leaves


# treeDepth
# return the depth of treeCreated
def treeDepth(treeCreated):
    depth = 0
    root = treeCreated.keys()[0]
    nodes = treeCreated[root]
    for key in nodes.keys():
        if type(nodes[key]).__name__ =='dict':
            thisDepth = 1 + treeDepth(nodes[key])
        else:
            thisDepth = 1
        if thisDepth > depth:
            depth = thisDepth
    return depth


# treeSave
# save treeCreated to a file
def treeSave(treeCreated, filename):
    import pickle
    treeFile = open(filename,'w')
    pickle.dump(treeCreated, treeFile)
    treeFile.close()

# treeLoad
# return treeCreated from a treeFile
def treeLoad(filename):
    import pickle
    treeFile = open(filename)
    return pickle.load(treeFile)


# classifier
# return category of testX by training treeCreated
def classifier(treeCreated, featureNames, testX):
    root = treeCreated.keys()[0]
    nodes = treeCreated[root]
    # get index of root in featureNames
    featureIndex = featureNames.index(root)
    for key in nodes.keys():
        if testX[featureIndex] == key:
            if type(nodes[key]).__name__ == 'dict':
                category = classifier(nodes[key], featureNames, testX)
            else:
                category = nodes[key]
    return category
    


#--------------------------------------------------
# tree (training)

featureNames = ['no surfacing','flippers']

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]


#print shannonEntropy(dataSet, -1)
#print dataReduction(dataSet, 1,1)
#print featureChoice(dataSet, -1)
treeCreated = tree(dataSet, featureNames, -1)
print treeCreated
print treeLeaves(treeCreated)
print treeDepth(treeCreated)


#--------------------------------------------------
# tree (testing)

featureNames = ['no surfacing','flippers']

dataTest = [[1, 0],
            [1, 0],
            [1, 1],
            [1, 1],
            [0, 1]]

for i in range(len(dataTest)):
    print classifier(treeCreated, featureNames, dataTest[i])


```



## 3. Naive Bayes
Summary
- Pros: Works with a small amount of data, handles multiple classes
- Cons: Sensitive to how the input data is prepared
- Data: Nominal values

Data Type


Algorithm



## 4. Logistic Regression
Summary
- Pros:
- Cons:
- Data:

Data Type


Algorithm



## 5. Support Vector Machine
Summary
- Pros:
- Cons:
- Data:

Data Type


Algorithm



## 6. AdaBoost Meta-Algorithm

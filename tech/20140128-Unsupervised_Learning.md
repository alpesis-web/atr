Jan 28 2014 | k-means, apriori, FP-growth | Kelly Chan
#Unsupervised Learning

Table of Contents
- unlabeled items grouping: k-means clustering
- association analysis: apriori
- frequent itemsets finding: FP-growth

## 1. Unlabeled items grouping: k-means clustering

Summary  
Pros: Easy to implement  
Cons: Can converge at local minima; slow on very large datasets  
Data: Numeric values   

Data Type  

| feature1   | feature2   |
|:----------:|:----------:|
| 1.658985   | 4.285136   |
| -3.453687  | 3.424321   |
| 4.838138   | -1.151539  |
| -5.379713  | -3.362104  |
| 0.972564   | 2.924086   |
| -3.567919  | 1.531611   |
| 0.450614   | -3.302219  |


Maths  
- mean
- euclidean distance: (x-y)^2
- squared error: distnace^2

Algorithm  

```

'''

Function Tree

- bisectingKMeans
     |
     |-------------- euclidean
     |                 |
     |-------------- kMeans
                       |----- randomCentroids


'''

from numpy import *


# dataLoad
# (data) extracting data from rawData
def dataLoad(dataFile):
    data = []
    rawData = open(dataFile)
    for line in rawData.readlines():
        thisLine = line.strip().split('        ')
        filtedLine = map(float, thisLine)
        data.append(filtedLine)
    return data


# euclidean
# return distance by calculating euclidean distance
# euclidean distance = sqrt((x-y)^2)
def euclidean(vectorX, vectorY): # row1 - row2
    return sqrt(sum(power(vectorX - vectorY, 2))) 


# randomCentroids
# (centroids) return k centroids by random selection
# centroids: (k, n) k rows, n cols/features
def randomCentroids(dataMatrix, k):
    cols = shape(dataMatrix)[1]
    centroids = mat(zeros((k, cols)))
    for col in range(cols):
        minThisFeature = min(dataMatrix[:, col])
        # range = max - min
        rangeThisFeature = float(max(dataMatrix[:, col] - minThisFeature))
        # centroids = min + range * random(k)
        # random.rand(k,1): generating random matrix (k rows, 1 col)
        centroids[:, col] = minThisFeature + rangeThisFeature * random.rand(k,1)
    return centroids # centroids: k rows, n features


# kMeans
# (centroids, clusterEval) return centorids, clusterEval by calculating euclidean distance
# centroids: 
#     cluster1: [mean of col0, mean of col2, ...]
#     cluster2: [mean of col0, mean of col2, ...]
#     cluster3: [mean of col0, mean of col2, ...]
#     cluster4: [mean of col0, mean of col2, ...]
# clusterEval: [cluster, distance**2]
def kMeans(dataMatrix, k, distMeans=euclidean, centroidsCreated=randomCentroids):

    rows = shape(dataMatrix)[0]
    clusterEval = mat(zeros((rows,2)))
    centroids = centroidsCreated(dataMatrix, k)

    # clusterChanged vs centroids
    # randomCentroids is just used once, then looping the meanCentroids
    # if evaluation of newCentroids = evaluation of lastCentroids, stop
    # else, generating newCentroids and evaluation continued
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False

        # evaluating each row by calculating distances for k times
        # and then assign it to the closest centroid
        for row in range(rows):
            minDistance = inf
            cluster = -1
            for i in range(k):
                # calculating distance between centroids[i] and dataX
                # first is randomCentroids, then meanCentroids based on last centroids
                distanceThisK = distMeans(centroids[i,:], dataMatrix[row,:])
                if distanceThisK < minDistance:
                    minDistance = distanceThisK
                    cluster = i
            # if this cluster != last cluster assigned, cluster is updated
            if clusterEval[row,0] != cluster:
                clusterChanged = True
            clusterEval[row,:] = cluster, minDistance**2

        # printing the centroids of this while loop taken
        print "centroids:\n",centroids
        # when this centroids finished, generating the meanCentroids
        # this new meanCentroids would be taken for the next while loop
        # when clusterChanged = False, centroids keeps the same
        for i in range(k):#recalculate centroids
            # clusterEval[:,0]: cluster output for all data
            # clusterEval[:,0].A: get minIndex (col 0) in the clusterEval
            # clusterEval[:,0].A == i: return True/False
            # nonzero(clusterEval[:,0].A == i): return the index of two arrays separately (true/false)
            # nonzero(clusterEval[:,0].A == i)[0]: return the index of true array
            # thisCluster: return the data rows of this cluster
            thisCluster = dataMatrix[nonzero(clusterEval[:,0].A == i)[0]] #get all the points in this cluster
            # return mean of each column and assign them to centroid
            # computing mean by column in thisCluster
            # axis=0: computing mean by column
            # axis=1: computing mean by row
            centroids[i,:] = mean(thisCluster, axis=0) # mean of each cluster for k clusters

    return centroids, clusterEval


# bisectingKMeans
# (centroids, clusterEval) 
# return centroids, clusterEval by subClustering
def bisectingKMeans(dataMatrix, k, distMeans=euclidean):

    rows = shape(dataMatrix)[0]
    clusterEval = mat(zeros((rows,2)))

    # calculating meanCentroids of the rawData by columns
    centroids = mean(dataMatrix, axis=0).tolist()[0]
    # evaluating cluster errors by the distance of meanCentroids and rawData
    for row in range(rows):
        clusterEval[row,1] = distMeans(mat(centroids), dataMatrix[row,:])**2


    centroidsList = [centroids] # converting centroids to centroid items
    while (len(centroidsList) < k):

        lowestSSE = inf
        for i in range(len(centroidsList)):
            # get data rows of this cluster
            splitCluster = dataMatrix[nonzero(clusterEval[:,0].A==i)[0],:]
            # calculating centroids, clusterEvaluation of splitCluster by kMeans
            centroidsSplitCluster, splitClusterEval = kMeans(splitCluster, 2, distMeans)

            # calculating SSE of splitCluster and cluster
            sseSplitCluster = sum(splitClusterEval[:,1])
            # clusterEval[nonzero(clusterEval[:,0].A != i)[0],1]: 
            # get the SSE (col1) of clusterEval, and then sum up 
            sseCluster = sum(clusterEval[nonzero(clusterEval[:,0].A != i)[0],1])
            print ("SSE of splitCluster: %f, SSE of cluster: %f") % (sseSplitCluster, sseCluster)

            if (sseSplitCluster + sseCluster) < lowestSSE:
                bestCentroidIndex = i
                bestNewCentroids = centroidsSplitCluster
                bestClusterEval = splitClusterEval.copy()
                lowestSSE = sseSplitCluster + sseCluster


        # (bestClusterEval)
        bestClusterEval[nonzero(bestClusterEval[:,0].A == 1)[0],0] = len(centroidsList)
        bestClusterEval[nonzero(bestClusterEval[:,0].A == 0)[0],0] = bestCentroidIndex
        print "bestCentroidIndex to split: ", bestCentroidIndex
        print "bestClusterEval's Length: ", len(bestClusterEval)

        # (centroidsList)
        centroidsList[bestCentroidIndex] = bestNewCentroids[0,:].tolist()[0]
        centroidsList.append(bestNewCentroids[1,:].tolist()[0])
        
        # (clusterEval)
        clusterEval[nonzero(clusterEval[:,0].A == bestCentroidIndex)[0],:] = bestClusterEval


    return mat(centroidsList), clusterEval


```


## 2. Association analysis: apriori

Summary  
Pros: Easy to code up  
Cons: May be slow on large datasets  
Data: Numeric values, nominal values  

Data Type  
[1, 3, 4]  
[2, 3, 5]  
[1, 2, 3, 5]  
[2, 5]  
 
 
Maths  
- probability
- confidence

Algorithm  

```

'''

Function Tree

apriori: finding the frequenced items
rulesGen: generating rules from frequenced items (apriori)

- rulesGen
    |
    |------- apriori
    |           |-------- aprioriGen
    |           |-------- itemScan
    |                       |------- itemsExtracted
    |                                     |--------- dataLoad
    |
    |
    |------- rulesFromConsequence
    |                |
    |------- confidenceCalculation  


'''


from numpy import *

# dataLoad
# extracting data from rawData
def dataLoad():
    return [[1, 3, 4], 
            [2, 3, 5], 
            [1, 2, 3, 5], 
            [2, 5]]


# itemsExtracted
# (forzenItems) return individual items / rawElements from data
def itemsExtracted(data):
    items = []
    for transaction in data:
        for item in transaction:
            if not [item] in items:
                items.append([item])
    items.sort()
    # forzenset: use it as a key in a dict
    return map(frozenset, items)


# itemScan
# (itemSupported, itemProbabilityDict)
# itemSupported: return item if its probablity >= minProbability
# itemProbabilityDict: return probability of each item
def itemScan(transactionSets, frozenItems, minProbabilitySupport):

    # counting the frequency of each item
    itemFreq = {}
    for transaction in transactionSets:
        for item in frozenItems:
            if item.issubset(transaction):
                if not itemFreq.has_key(item):
                    itemFreq[item] = 1
                else:
                    itemFreq[item] += 1

    n = float(len(transactionSets))
    itemSupported = []
    itemProbabilityDict = {}
    for key in itemFreq:
        probability = itemFreq[key] / n
        itemProbabilityDict[key] = probability
        if probability >= minProbabilitySupport:
            itemSupported.insert(0,key)

    return itemSupported, itemProbabilityDict


# aprioriGen
# (itemCombinations) return itemCombinations after combining k subsets
# itemSupported: generated from itemScan
# k: how many subsets for this combination
def aprioriGen(itemSupported, k):
    itemCombinations = []
    sets = len(itemSupported)
    for i in range(sets):
        for j in range(i+1, sets):
            # convert frozenset of itemSupported to list
            # list(itemSupported[i]) each set in itemSupported
            # [: k - 2]: get the first item in this set 
            firstItemInSet1 = list(itemSupported[i])[: k - 2]
            firstItemInSet2 = list(itemSupported[j])[: k - 2]
            firstItemInSet1.sort()
            firstItemInSet2.sort()
            # if both items are the same, union and get one
            if firstItemInSet1 == firstItemInSet2:
                itemCombinations.append(itemSupported[i] | itemSupported[j])
    return itemCombinations


# apriori
# (itemSupportedList, itemProbabilityDict)
# return itemSupportedList, itemProbabilityDict by aprioriGen
def apriori(data, minProbabilitySupport = 0.5):
    frozenItems = itemsExtracted(data)
    transactionSets = map(set, data)
    itemSupported, itemProbabilityDict = itemScan(transactionSets, frozenItems, minProbabilitySupport)

    itemSupportedList = [itemSupported]
    k = 2
    while (len(itemSupportedList[k-2]) > 0):
        itemCombinations = aprioriGen(itemSupportedList[k-2], k)
        kItemSupported, kItemProbabilityDict = itemScan(transactionSets, itemCombinations, minProbabilitySupport)
        itemProbabilityDict.update(kItemProbabilityDict)
        itemSupportedList.append(kItemSupported)
        k += 1
    return itemSupportedList, itemProbabilityDict


# confidenceCalculation
# (prunedSubsetItems) return prunedSubsetItems by calculating confidence
def confidenceCalculation(subset, subsetItems, itemProbabilityDict, rules, minConfidence=0.7):
    prunedSubsetItems = []
    for consequence in subsetItems:
        confidence = itemProbabilityDict[subset] / itemProbabilityDict[subset-consequence]
        if confidence >= minConfidence:
            print subset-consequence, '-->', consequence,'confidence:',confidence
            rules.append((subset-consequence, consequence, confidence))
            prunedSubsetItems.append(consequence)
    return prunedSubsetItems



# rulesFromConsequence
# generating rules by itemCombinations in subset
def rulesFromConsequence(subset, subsetItems, itemProbabilityDict, rules, minConfidence=0.7):
    # get the first frozenset in subsetItems
    n = len(subsetItems[0])
    # if # of subset > # of first frozenset + 1
    if (len(subset) > (n+1)):
        itemCombinations = aprioriGen(subsetItems, n+1)
        itemCombinations = confidenceCalculation(subset, itemCombinations, itemProbabilityDict, rules, minConfidence)
        if (len(itemCombinations) > 1):
            rulesFromConsequence(subset, itemCombinations, itemProbabilityDict, rules, minConfidence)



# rulesGen
# (rules) return rules by rulesFromConsequence and confidenceCalculation
# itemSupportedList: gengerated by apriori
# itemProbabilityDict: generated by itemScan
def rulesGen(itemSupportedList, itemProbabilityDict, minConfidence=0.7):
    rules = []
    for i in range(1, len(itemSupportedList)): # only get the sets with two or more items
        for subset in itemSupportedList[i]:
            subsetItems = [frozenset([item]) for item in subset]
            if (i > 1):
                rulesFromConsequence(subset, subsetItems, itemProbabilityDict, rules, minConfidence)
            else:
                confidenceCalculation(subset, subsetItems, itemProbabilityDict, rules, minConfidence)
    return rules

```




## 3. Frequent itemsets finding: FP-growth

Summary  
Pros: Usually faster than Apriori  
Cons: Difficult to implement; certain datasets degrade the performance  
Data: Nominal values  

Data Type  
[['r', 'z', 'h', 'j', 'p'],  
 ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],  
 ['z'],  
 ['r', 'x', 'n', 'o', 's'],  
 ['y', 'r', 'x', 'z', 'q', 't', 'p'],  
 ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]  

Maths  
- frequency count
- tree (data structure)


Algorithm  

```

'''

Function Tree

- frequencedItemsList
     |
     |------------ mineTree
                      |
                      |------ findPrefixPath
                      |           |----------- ascendTree
                      |
                      |------ createTree
                                  |----------- (treeNode)
                                  |----------- udpateTree
                                                  |-------- (treeNode)
                                                  |-------- updateHeader

- mineTree
    |
    |------ createTree (fpTree, headerTable)
               |
               |-------- createInitSet
                              |---------- dataLoad

'''


# treeNode
# creating fpTree structure
# fpTree: 
# - nodeName - occurrence
#            - nodeLink    - parent
#                          - children
class treeNode:
    def __init__(self, nodeName, occurrence, parent):
        self.nodeName = nodeName
        self.occurrence = occurrence
        self.nodeLink = None
        self.parent = parent
        self.children = {}
    
    # counting the frequencies of occurrence
    def countFreq(self, occurrence):
        self.occurrence += occurrence

    # displaying the tree
    def display(self, tabs=1):
        print '  '*tabs, self.nodeName, ' ', self.occurrence
        # recursing the children nodes
        for child in self.children.values():
            child.display(tabs+1)

# createTree
# (fpTree, headerTable) 
# return fpTree and headerTable with items and freq(>=minFreq) from dataSet
# dataSet: extracting from rawData, must be [set]
def createTree(dataSet, minFreq=1):

    # generating headerTable from dataSet
    headerTable = {}
    # getting items and their frequencies from dataSet
    for transaction in dataSet:
        for item in transaction:
            headerTable[item] = headerTable.get(item, 0) + dataSet[transaction]
    # removing items those not meet the minFreq
    for key in headerTable.keys():
        if headerTable[key] < minFreq:
            del(headerTable[key])

    # checking the items/keys in headerTable
    itemsHeaderTable = set(headerTable.keys())
    #print 'itemsSet: ', itemsSet
    # if no items in headerTable, return None for fpTree and headerTable
    if len(itemsHeaderTable) == 0:
        return None, None

    # reformating headerTable to meet class treeNode
    # before reformating:
    # headerTable: {item: frequency, item: frequency}
    # after reformating:
    # headerTable: {item: [frequency, parent], item: [frequency, parent]}
    for key in headerTable:
        headerTable[key] = [headerTable[key], None]
    #print 'headerTable: ', headerTable

    # creating fpTree
    fpTree = treeNode('Null Set', 1, None)
    for transaction, frequency in dataSet.items():
        # creating transactionDict from headerTable
        transactionDict = {}
        for item in transaction:
            if item in itemsHeaderTable:
                # localDict: itemFreq = itemFreq in headerTable
                # headerTable[item][0]: frequency, headerTable: {item: [frequency, parent], item: [frequency, parent]}
                transactionDict[item] = headerTable[item][0]
        if len(transactionDict) > 0:
            # transactionDict.items(): get (item, frequency) from transactionDict
            # sorted(): sorting the items with frequnecy by descending order
            # orderedItems: get items by frequency with descending order
            orderedItems = [item[0] for item in sorted(transactionDict.items(), key=lambda freq: freq[1], reverse=True)]
            # populating tree with ordered frequency items
            updateTree(orderedItems, fpTree, headerTable, frequency)
    return fpTree, headerTable


# updateTree
# most freq item -> fpTree.children -> headerTable parent
# - updating fpTree.children with the most freq item
# - updating headerTable parent with fpTree.children
def updateTree(orderedItems, fpTree, headerTable, frequency):

    # orderedItems[0]: the most freq item
    # - as fpTree.children: 
    #      - if existing, add frequency
    #      - else, create fpTree.children with this item by treeNode
    #              update headerTable parent <- new fpTree.children    
    if orderedItems[0] in fpTree.children:
        # if fpTree.children is existing, update frequency
        fpTree.children[orderedItems[0]].countFreq(frequency)
    else:
        # if fpTree.children is NOT existing, create fpTree.children 
        fpTree.children[orderedItems[0]] = treeNode(orderedItems[0], frequency, fpTree)
        # update headerTable parent with fpTree.children
        if headerTable[orderedItems[0]][1] == None:
            # if no this parent, headerTable parent <- fpTree.chidren
            headerTable[orderedItems[0]][1] = fpTree.children[orderedItems[0]]
        else:
            # if parent, calling updateHeader()
            updateHeader(headerTable[orderedItems[0]][1], fpTree.children[orderedItems[0]])

    # if orderedItems is more than 1, calling updateTree to update the remaining ordered items 
    if len(orderedItems) > 1:
        updateTree(orderedItems[1::], fpTree.children[orderedItems[0]], headerTable, frequency)

# updateHeader
# updating parentHeaderTable <- fpTree.children 
def updateHeader(parentHeaderTable, childrenFPTree):
    while (parentHeaderTable.nodeLink != None):
        parentHeaderTable = parentHeaderTable.nodeLink
    parentHeaderTable.nodeLink = childrenFPTree


# ascendTree
# ascending from leaf node to root
def ascendTree(nodeHeaderTable, prefixPath):
    if nodeHeaderTable.parent != None:
        # appending the nodeName of nodeHeaderTable to prefixPath
        prefixPath.append(nodeHeaderTable.nodeName)
        # recursing the parent of nodeHeaderTable
        ascendTree(nodeHeaderTable.parent, prefixPath)

# findPrefixPath
# (conditionPaths) return conditionPaths by looping nodeHeaderTable's nodeLink
# - searching the ascending tree
# - return the occurrence
def findPrefixPath(item, nodeHeaderTable):
    conditionPaths = {}
    while nodeHeaderTable != None:
        prefixPath = []
        ascendTree(nodeHeaderTable, prefixPath)
        if len(prefixPath) > 1:
            # item -> prefixPath[0]
            # prefixPath[1:]: excluding item/prefixPath[0]
            conditionPaths[frozenset(prefixPath[1:])] = nodeHeaderTable.occurrence
        nodeHeaderTable = nodeHeaderTable.nodeLink
    return conditionPaths
    

# mineTree
# appending frequencedItemsList by prefix-conditionPaths
def mineTree(fpTree, headerTable, minFreq, prefixSet, frequencedItemsList):

    # get the items in headerTable by frequency with ascending order
    # headerTable.items: (item, frequency)
    # item: item[1] - frequency
    ascItems = [item[0] for item in sorted(headerTable.items(), key=lambda item: item[1])]

    # mining the items in headerTable one by one (ASCENDING order)
    # ascending order: the bottom of fpTree
    for item in ascItems:

        # adding items into prefixSet one by one
        thisPrefixSet = prefixSet.copy()
        thisPrefixSet.add(item)
        #print 'thisPrefixSet: ', thisPrefixSet
        frequencedItemsList.append(thisPrefixSet)



        # creating the conditionPaths
        conditionPaths = findPrefixPath(item, headerTable[item][1])
        #print 'conditionPaths: ', item, conditionPaths

        # creating conditionFPTree, coonditionHeaderTable by conditionPaths
        conditionFPTree, conditionHeaderTable = createTree(conditionPaths, minFreq)
        #print 'conditionHeaderTable from conditionFPTree: ', conditionHeaderTable

        # printing thisPrefixSet, conditionFPTree, mining the tree with thisPrefixSet
        if conditionHeaderTable != None:
            print 'conditionFPTree for: ', thisPrefixSet
            conditionFPTree.display(1)
            mineTree(conditionFPTree, conditionHeaderTable, minFreq, thisPrefixSet, frequencedItemsList)





#------------------------------------------------------
# testing

#rootNode = treeNode('pyramid',9, None)
#rootNode.children['eye'] = treeNode('eye', 13, None)
#rootNode.disp()

#rootNode.children['phoenix'] = treeNode('phoenix', 3, None)
#rootNode.disp()


def dataLoad():
    rawData = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return rawData


def createInitSet(data):
    initSet = {}
    for transaction in data:
        initSet[frozenset(transaction)] = 1
    return initSet

testData = dataLoad()
initSet = createInitSet(testData)

fpTree, headerTable = createTree(initSet, 3)
fpTree.display()


# mining the frequencedItems
frequencedItems = []
mineTree(fpTree, headerTable, 3, set([]), frequencedItems)
print frequencedItems

```


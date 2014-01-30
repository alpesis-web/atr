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

Maths  

Algorithm  




## 3. Frequent itemsets finding: FP-growth

Summary  
Pros:  
Cons:  
Data:  

Data Type  

Maths  

Algorithm  




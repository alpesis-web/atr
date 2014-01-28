Jan 25 2014 | Forecasting, Regression | Kelly Chan
# Forecasting with Regression

Table of Contents
- linear regression
- tree-based regression

## 1. Linear Regression

Summary  
Pros: Easy to interpret results, computationally inexpensive  
Cons: Poorly models nonlinear data  
Data: Numeric values, nominal values  

Data Type  

| feature1  | feature2  | target    |
|:---------:|:---------:|:---------:|
| 1.000000  | 0.067732  | 3.176513  |
| 1.000000  | 0.427810  | 3.816464  |
| 1.000000  | 0.995731  | 4.550095  |
| 1.000000  | 0.738336  | 4.256571  |
| 1.000000  | 0.981083  | 4.560815  |
| 1.000000  | 0.526171  | 3.929515  |
| 1.000000  | 0.378887  | 3.526170  |



Maths  
- <b>regression</b> - (X^T * X) inversed  
    Y = X^T * W  
    W = (X^T \* X)^(-1) \* X^T * Y  

- <b>locally weighted linear regression (LWLR)</b> - (X^T * X) inversed  
    yHat = (X^T * W * X)^(-1) * X^T * W * y  
    (kernel) W = exp (|xi - x|/(-2k^2)), constant k - how much to weight nearby points  

- <b>ridge regression</b> - (X^T * X) NOT inversed  
    Y = X^T * X + lambda * I  
    W = (X^T * X + lambda * I)^(-1) * X^T * y  

- <b>forward stagewise regression</b> - greedy algorithm  
    lasso  

Algorithm  

```


'''

Function Tree

- regressionWeights
     |-------------- dataLoad


- squaredError
   |
- regressionLocalWeightsTest
      |
      |--------- regressionLocalWeights
      |--------- dataLoad


NOTE: which lambda should be chosen?
NOTE: Normalizing rawData before implementing regressionRidge
- regressionRidgeWeightsTest
      |--------- regressionRidge
      |--------- dataLoad


# Lasso
- regressionStagewise
      |--------- regularize
      |--------- squaredError
'''


from numpy import *


# dataLoad
# (features, target) extracting features, target from rawData
def dataLoad(dataFile):
    features = []
    target = []
    nFeatures = len(open(dataFile).readline().split('        ')) - 1
    rawData = open(dataFile)
    for line in rawData.readlines():
        thisLine = line.strip().split('        ')
        thisFeatures = []
        for i in range(nFeatures):
            thisFeatures.append(float(thisLine[i]))
        features.append(thisFeatures)
        target.append(float(thisLine[-1]))
    return features, target


# regressionWeights
# (weightsMartix) retrun weightsMatrix by calculating w = (X^T * X)^(-1) * X^T * Y
def regressionWeights(features, target):
    xMatrix = mat(features)
    yMatrix = mat(target).T
    # X^T * X
    xTx = xMatrix.T * xMatrix
    # linalg.det(): computing the determinate
    if linalg.det(xTx) == 0.0:
        print "The matrix is singular, could not do inverse."
        return
    # w = (X^T * X)^(-1) * X^T * Y
    weightsMatrix = xTx.I * xMatrix.T * yMatrix
    return weightsMatrix

#---------------------------------------------------------------------------------

# regressionLocalWeights
# (yHatTestX) return yHat by locally weighted linear regression
# kernel: kernel = exp (|xi - x|/(-2k^2))
# wHat = (X^T * kernel * X)^(-1) * X^T * kernel * y
# yHatTestX = testX * wHat
def regressionLocalWeights(testX, features, target, k = 1.0):
    xMatrix = mat(features)
    yMatrix = mat(target).T
    rows = shape(xMatrix)[0]
    kernelMatrix = mat(eye((rows)))
    for row in range(rows):
        differenceMatrix = testX - xMatrix[row, :]
        # kernel: wHat = exp (|xi - x|/(-2k^2))
        kernelMatrix[row, row] = exp(differenceMatrix * differenceMatrix.T / (-2.0*k**2))
        xTx = xMatrix.T * (kernelMatrix * xMatrix)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, it cannot do inverse."
        return
    # wHat = (X^T * kernel * X)^(-1) * X^T * kernel * y
    weightsMatrix = xTx.I * (xMatrix.T * kernelMatrix * yMatrix)
    return testX * weightsMatrix



# regressionLocalWeightsTest
# (yHat) return yHat by locally weighted linear regression
def regressionLocalWeightsTest(testFeatures, trainFeatures, trainTarget, k=1.0):
    rows = shape(testFeatures)[0]
    yHat = zeros(rows)
    for row in range(rows):
        yHat[row] = regressionLocalWeights(testFeatures[row],trainFeatures, trainTarget, k)
    return yHat

# error
# return the error of (y - yHat)^2
def squaredError(yArray,yHatArray):
    return ((yArray-yHatArray)**2).sum()

#---------------------------------------------------------------------------------



# regressionRidgeWeights
# (ridgeWeights) retrun ridgeWeights by calculating
# Y = X^T * X + lambda * I
# W = (X^T * X + lambda * I)^(-1) * X^T * y
def regressionRidgeWeights(xMatrix, yMatrix, lamb=0.2): # lamb: lambda 
    xTx = xMatrix.T * xMatrix
    # Y = X^T * X + lambda * I
    ridgeMatrix = xTx + eye(shape(xMatrix)[1])*lamb
    if linalg.det(ridgeMatrix) == 0.0:
        print "This matrix is singular, it cannot do inverse."
        return
    # W = (X^T * X + lambda * I)^(-1) * X^T * y
    ridgeWeights = ridgeMatrix.I * (xMatrix.T * yMatrix)
    return ridgeWeights


# regressionRidgeWeightsTest
# (weightsMatrix) return different weights with different lambda
#NOTE: which lambda should be chosen?
#NOTE: Normalizing the rawData before implementing Ridge Regression
def regressionRidgeWeightsTest(features, target):
    xMatrix = mat(features)
    yMatrix = mat(target).T

    # normalizing target
    yMeanMatrix = mean(yMatrix,0)
    yMatrix = yMatrix - yMeanMatrix

    # normalizing features
    xMeanMatrix = mean(xMatrix,0)
    xVar = var(xMatrix,0) # var: variance
    xMatrix = (xMatrix - xMeanMatrix) / xVar


    # get different weights by calculating different lambdas
    nLambdas = 30
    weightsMatrix = zeros((nLambdas, shape(xMatrix)[1]))
    for i in range(nLambdas):
        weights = regressionRidgeWeights(xMatrix, yMatrix, exp(i-10))
        weightsMatrix[i,:] = weights.T
    return weightsMatrix 


#---------------------------------------------------------------------------------

# regularize
# (xRegularizedMatrix) return xMatrix after regularization
def regularize(featuresMatrix):
    xMatrix = featuresMatrix.copy()
    xMeanMatrix = mean(xMatrix,0) # mean
    xVariance = var(xMatrix,0)  # variance
    xRegularizedMatrix = (xMatrix - xMeanMatrix) / xVariance
    return xRegularizedMatrix


# regressionStagewise
# (weightSet) return weightSet by calculating lasso for n loops
def regressionStagewise(features, target, eps=0.01, loops=100):
    xMatrix = mat(features)
    yMatrix = mat(target).T

    # normalizing yMatrix
    yMeanMatrix = mean(yMatrix,0)
    yMatrix =yMatrix - yMeanMatrix

    # normalizing xMatrix
    #(regularize) calling the function regularize to regularize xMatrix
    xMatrix = regularize(xMatrix)

    rows, cols = shape(xMatrix)
    weightsMatrix = zeros((cols,1))
    testWeightsMatrix = weightsMatrix.copy()
    maxWeightsMatrix = weightsMatrix.copy()

    weightSet = zeros((loops, cols))
    for loop in range(loops):
        #print weightsMatrix.T
        lowestError = inf
        for col in range(cols):
            for sign in [-1,1]:
                testWeightsMatrix = weightsMatrix.copy()
                # calculating weightsMatrix
                testWeightsMatrix[col] += eps * sign
                # Y = X * weights
                yTestMatrix = xMatrix * testWeightsMatrix
                rssError = squaredError(yMatrix.A, yTestMatrix.A)
                if rssError < lowestError:
                    lowestError = rssError
                    maxWeightsMatrix = testWeightsMatrix
        weightsMatrix = maxWeightsMatrix.copy()
        weightSet[loop,:] = weightsMatrix.T
    return weightSet


```



## 2. Tree-based Regression


Summary  
Pros: Fits complex, nonlinear data  
Cons: Difficult to interpret results   
Data: Numeric values, nominal values   

Data Type  

| feature   | target      |
|:---------:|:-----------:|
| 0.228628  | -2.266273   |
| 0.965969  | 112.386764  |
| 0.342761  | -31.584855  |
| 0.901444  | 87.300625   |
| 0.585413  | 125.295113  |
| 0.334900  | 18.976650   |
| 0.769043  | 64.041941   |


Maths  
- bestFeatureSplit: targetMean, targetVariance

Algorithm  

```


'''

Prediction
1. forecast1: target tree
2. forecast2: model predicted - y = w0x0 + w1x1
3. forecast3: regression - weights


forecast1: target tree
- forecast
   |-------- (dataLoad)
   |-------- (treeCreated)  <---- targetMean / targetError
   |-------- treeForecast
                 |--------- regressionEvaluation


forecast2: model predicted - y = w0x0 + w1x1
- forecast
   |-------- (dataLoad)
   |-------- (treeCreated)  <---- regressionLeaf / regressionError
   |-------- treeForecast
                 |--------- modelEvaluation


forecast3: regression - weights
- regression
      |------ (dataLoad)


#------------------------------------------------------------------
# Master Function Tree

- forecast
   |
   |-------- (treeCreated) 
   |              |----------- targetMean / targetError
   |              |----------- regressionLeaf / regressionError
   |
   |-------- (dataLoad)
   |
   |-------- treeForecast
                 |--------- regressionEvaluation <---- targetMean / targetError
                 |--------- modelEvaluation      <---- regressionLeaf / regressionError




# creating tree from trainData
# tree structure
# (feature) featureIndex, featureValue
# (target/weights) leftNode, rightNode
#
# treePrune: to check if tree can be pruned

- treeCreated
   |------------- dataLoad
   |------------- dataSplit   
   |------------- bestFeatureSplit
   |                    |------------- targetMean  <---- regressionLeaf  <---- regression
   |                    |------------- targetError <---- regressionError <---- regression
   |                    |------------- dataSplit
   |
- treePrune
      |------- isTree
      |------- treeMean
      |------- dataSplit


'''

from numpy import *

# dataLoad
# (data) extracting data from raw file
def dataLoad(dataFile):
    data = []
    rawData = open(dataFile)
    for line in rawData.readlines():
        thisLine = line.strip().split('        ')
        filtedLine = map(float,thisLine)
        data.append(filtedLine)
    return data


# dataSplit
# (dataGt, dataLE) return dataGt, dataLE by featureValue in a specific featureIndex
# dataGt: >  featureValue
# dataLE: <= featureValue
def dataSplit(data, featureIndex, featureValue):
    dataGt = data[nonzero(data[:, featureIndex] >  featureValue)[0], :][0]
    dataLE = data[nonzero(data[:, featureIndex] <= featureValue)[0], :][0]
    return dataGt, dataLE



# targetMean
# retrun mean value of target
def targetMean(data):
    return mean(data[:,-1])  # data[:,-1]: get the last col

# targetError
# return variance of target
def targetError(data):
    return var(data[:,-1]) * shape(data)[0]

# bestTargetSplit
# (bestFeatureIndex, bestFeatureValue) 
# return bestFeatureIndex, bestFeatureValue by errorType=targetError 
#                                           or  leafType=targetMean
def bestFeatureSplit(data, leafType=targetMean, errorType=targetError, ops=(1,4)):

    # (featureIndex, featureValue)
    if len(set(data[:,-1].T.tolist()[0])) == 1:
        return None, leafType(data)  # featureIndex, featureValue

    bestTolerance = inf
    fixedTolerance = ops[0]  # tolerance on the error reduction
    tolerance = errorType(data)

    minN = ops[1]  # the minimum data instances to include in a split
    rows, cols = shape(data)

    bestFeatureIndex = 0
    bestFeatureValue = 0
    for featureIndex in range(cols-1):
        for featureValue in set(data[:, featureIndex]):
            dataGt, dataLE = dataSplit(data, featureIndex, featureValue)
            if (shape(dataGt)[0] < minN) or (shape(dataLE)[0] < minN):
                    continue
            newTolerance = errorType(dataGt) + errorType(dataLE)
            if newTolerance < bestTolerance:
                bestFeatureIndex = featureIndex
                bestFeatureValue = featureValue
                bestTolerance = newTolerance
    
    # (featureIndex, featureValue)
    if (tolerance - bestTolerance) < fixedTolerance:
        return None, leafType(data)   # featureIndex, featureValue

    # (featureIndex, featureValue)
    dataGt, dataLE = dataSplit(data, bestFeatureIndex, bestFeatureValue)
    if (shape(dataGt)[0] < minN) or (shape(dataLE)[0] < minN):
        return None, leafType(data)   # featureIndex, featureValue

    return bestFeatureIndex, bestFeatureValue



# treeCreated
# (tree) return tree by bestFeatureSplit
def treeCreated(data, leafType=targetMean, errorType=targetError, ops=(1,4)):

    # (bestFeatureIndex, bestFeatureValue)
    bestFeatureIndex, bestFeatureValue = bestFeatureSplit(data, leafType, errorType, ops)
    if bestFeatureIndex == None:
        return bestFeatureValue

    # constructing tree
    tree = {}
    tree['featureIndex'] = bestFeatureIndex
    tree['featureValue'] = bestFeatureValue
    dataGt, dataLE = dataSplit(data, bestFeatureIndex, bestFeatureValue)
    tree['leftNode'] = treeCreated(dataGt, leafType, errorType, ops)
    tree['rightNode'] = treeCreated(dataLE, leafType, errorType, ops)
    return tree



# isTree
# checking if type(obj) == 'dict'?
def isTree(obj):
    return (type(obj).__name__=='dict')


# treeMean
# return the mean of a tree by recursing left and right nodes
# treeMean = (leftValue + rightValue) / 2
def treeMean(tree):
    if isTree(tree['rightNode']):
        tree['rightNode'] = treeMean(tree['rightNode'])
    if isTree(tree['leftNode']):
        tree['leftNode'] = treeMean(tree['leftNode'])
    return (tree['leftNode'] + tree['rightNode']) / 2.0


# treePrune
# (tree) return tree after pruning
def treePrune(tree, testData):

    # if no testData, return treeMean
    if shape(testData)[0] == 0:
        return treeMean(tree)

    # if left/right node existed in the tree, 
    # get testDataGt, testDataLE by splitting testData with featureIndex, featureValue
    if (isTree(tree['rightNode']) or isTree(tree['leftNode'])):
        testDataGt, testDataLE = dataSplit(testData, tree['featureIndex'], tree['featureValue'])
    # recursing the subset(s) of left/right nodes
    if isTree(tree['leftNode']):
        tree['leftNode'] = treePrune(tree['leftNode'], testDataGt)
    if isTree(tree['rightNode']):
        tree['rightNode'] = treePrune(tree['rightNode'], testDataLE)

    # if no left/right nodes in a tree, calculating the error
    if not isTree(tree['leftNode']) and not isTree(tree['rightNode']):
        testDataGt, testDataLE = dataSplit(testData, tree['featureIndex'], tree['featureValue'])
        # error in left/right nodes
        # error = (leftTarget - leftNode)^2 + (rightTarget - rightNode)^2
        errorNotMerge = sum(power(testDataGt[:, -1] - tree['leftNode'], 2)) + \
                        sum(power(testDataLE[:, -1] - tree['rightNode'], 2))
        # error in left/right nodes combined
        # error = testTarget - (1/2 * (leftNode + rightNode))
        thisTreeMean = (tree['leftNode'] + tree['rightNode']) / 2.0
        errorMerge = sum(power(testData[:, -1] - thisTreeMean, 2))

        # if errorMerge < errorNotMerge, than merging the data
        if errorMerge < errorNotMerge:
            print "merging"
            return thisTreeMean
        else:
            return tree
    else:
        return tree

#-------------------------------------------------------------------------
# Regression


# regression
# (weightsMatrix, xMatrix, yMatrix)
# return model items by linear regression
def regression(data):
    rows, cols = shape(data)
    xMatrix = mat(ones((rows, cols)))
    yMatrix = mat(ones((rows, 1)))

    xMatrix[:, 1:cols] = data[:, 0:cols-1] # col 0: w0x0
    yMatrix = data[:, -1]
    
    xTx = xMatrix.T * xMatrix
    if linalg.det(xTx) == 0.0:
        raise NameError("This matrix is singular, it cannot do inverse.\n Try increasing the second value of ops.")
    weightsMatrix = xTx.I * (xMatrix.T * yMatrix)
    return weightsMatrix, xMatrix, yMatrix


# regressionLeaf
# (weightsMatrix) return weights of left/right nodes
def regressionLeaf(data):
    weightsMatrix, xMatrix, yMatrix = regression(data)
    return weightsMatrix


# regressionError
# return error of left/right nodes
# error = (yMatrix - yHat)^2
def regressionError(data):
    weightsMatrix, xMatrix, yMatrix = regression(data)
    yHat = xMatrix * weightsMatrix
    return sum(power(yMatrix - yHat, 2))

#-------------------------------------------------------------------------
# forecast


# regressionEvaluation
# (node) return the value of left/right node
def regressionEvaluation(node, testX):
    return float(node)

# modelEvaluation
# (xMatrix * node) retrun yHat with left/right node
def modelEvaluation(node, testX):
    cols = shape(testX)[1]
    xMatrix = mat(ones((1, cols+1)))
    xMatrix[:, 1:cols+1] = testX
    return float(xMatrix * node)


# treeForecast
# (yHat[i]) retrun yHat by each row
def treeForecast(tree, testX, testTarget=regressionEvaluation):

    if not isTree(tree):
        return testTarget(tree, testX)
    
    if testX[tree['featureIndex']] > tree['featureValue']:
        if isTree(tree['leftNode']):
            return treeForecast(tree['leftNode'], testX, testTarget)
        else:
            return testTarget(tree['leftNode'], testX)
    else:
        if isTree(tree['rightNode']):
            return treeForecast(tree['rightNode'], testX, testTarget)
        else:
            return testTarget(tree['rightNode'], testX)


# forecast
# (yHat) return yHat by searching treeForecast
def forecast(tree, testFeature, testTarget=regressionEvaluation):
    rows = len(testFeature)
    yHat = mat(zeros((rows,1)))
    for row in range(rows):
        yHat[row,0] = treeForecast(tree, mat(testFeature[row]), testTarget)
    return yHat
    
```

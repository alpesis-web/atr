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
- regression equation: 
    Y = X^T * W, 
    W = (X^T \* X)^(-1) \* X^T * Y
- W = (X^T \* X)^(-1) \* X^T * Y
- locally weighted linear regression (LWLR): wHat = (X^T * W * X)^(-1) * X^T * W * y
- kernel: exp (|xi - x|/(-2k^2)), constant k - how much to weight nearby points

Algorithm  

```

'''

Function Tree

- error
   |
- regressionLocalWeightsTest
      |
      |--------- regressionLocalWeights
      |
      |--------- regressionWeights
                      |----------------- dataLoad

'''


from numpy import *


# dataLoad
# (features, target) extracting features, target from rawData
def dataLoad(dataFile):
    features = []
    target = []
    nFeatures = len(open(dataFile).readline().split('\t')) - 1
    rawData = open(dataFile)
    for line in rawData.readlines():
        thisLine = line.strip().split('\t')
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
def error(yArray,yHatArray):
    return ((yArray-yHatArray)**2).sum()

```



## 2. Tree-based Regression


Summary  
Pros: Easy to interpret results, computationally inexpensive  
Cons: Poorly models nonlinear data  
Data: Numeric values, nominal values  

Data Type  


Maths  

Algorithm  


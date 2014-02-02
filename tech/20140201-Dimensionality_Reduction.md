Feb 1 2014 | PCA, SVD | Kelly Chan
# Dimensionality Reduction

Table of Contents  
- Principal Component Analysis (PCA)
- Singular Value Decomposition (SVD) - (application)recommendation system

## 1. Principal Component Analysis (PCA)
Summary  
Pros: Reduces complexity of data, indentifies most important features  
Cons: May not be needed, could throw away useful information  
Data: Numerical values  

Data Type:  

| feature1   | feature2   |
|:----------:|:----------:|
| 10.235186	 | 11.321997  |
| 10.122339	 | 11.810993  |
| 9.190236	 | 8.904943   |
| 9.306371	 | 9.847394   |
| 8.330131	 | 8.340352   |
| 10.152785	 | 10.123532  |

Maths:  
- covariance
- eigenValues, eigenVectors

Algorithm:  
```

from numpy import *


# dataLoad
# (dataMatrix) extracting dataMatrix from rawData
def dataLoad(dataFile, delim ='\t'):
    rawData = open(dataFile)
    features = [line.strip().split(delim) for line in rawData.readlines()]
    data = [map(float, line) for line in features]
    return mat(data)

# NaNtoMean
# replacing NaN <- Mean
def NaNtoMean():
    dataMatrix = dataLoad(dataFile, '\t')
    cols = shape(dataMatrix)[1]
    for col in range(cols):
        # meanFeatures: calculating means of each feature (NaN exclusive)
        meanFeatures = mean(dataMatrix[nonzero(~isnan(dataMatrix[:,col].A))[0],col])
        # NaN <- mean
        dataMatrix[nonzero(isnan(dataMatrix[:,col].A))[0],col] = meanFeatures
    return dataMatrix


# pca
# (reducedDataMatrix, reconstructedMatrix)
# reducedDataMatrix = meanRemoved * reducedEigenVectors
# reconstructedMatrix = (reducedDataMatrix * reducedEigenVectors.T) + meanFeatures
#
# reducedEigenVectors <- eigenVecotrs[:, reducedEigenValuesIndex] <- eigenValues
# eigenValues, eigenVectors <- covariance <- meanRemoved
def pca(dataMatrix, featuresTopN=9999999):

    # calculating mean by each col/feature
    meanFeatures = mean(dataMatrix, axis=0)
    meanRemovedMatrix = dataMatrix - meanFeatures

    # calculating covarianceMatrix with meanRemovedMatrix
    covarianceMatrix = cov(meanRemovedMatrix, rowvar=0)
    # calculating eigenValues, eigenVectors with covarianceMatrix
    eigenValues, eigenVectors = linalg.eig(mat(covarianceMatrix))

    # sorting: smallest -> largest
    # argsort(): get the order of the eigenvalues
    eigenValuesIndex = argsort(eigenValues)
    # cutting  off unwanted dimensions
    eigenValuesIndex = eigenValuesIndex[:-(featuresTopN+1):-1]

    # reorganizing eigenVectors: largest -> smallest
    reducedEigenVectors = eigenVectors[:, eigenValuesIndex]

    # transforming data into new dimensions
    reducedDataMatrix = meanRemovedMatrix * reducedEigenVectors
    reconstructedMatrix = (reducedDataMatrix * reducedEigenVectors.T) + meanFeatures
    return reducedDataMatrix, reconstructedMatrix

```


## 2. Singular Value Decomposition (SVD)

Summary  
Pros: Simplifies data, removes noise, may improve algorithm results  
Cons: Transformed data may be difficult to understand  
Data: Numeric values  

Data Type:  

Maths:  
- [DATA]m\*n = [U]m\*m  [SIGMA]m\*n   [V^T]n\*n

Algorithm:  


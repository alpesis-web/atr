# Machine Learning
- [Classification](https://github.com/KellyChan/notebook/blob/master/tech/20140115-ML1_Classification.md)
- [Forecasting with regression](https://github.com/KellyChan/notebook/blob/master/tech/20140115-ML2_Forecasting_with_Regression.md)
- [Unsupervised Learning](https://github.com/KellyChan/notebook/blob/master/tech/20140115-ML3_Unsupervised_Learning.md)
- [Dimensionality Reduction](https://github.com/KellyChan/notebook/blob/master/tech/20140115-ML4_Dimensionality_Reduction.md)
- [Big Data and MapReduce](https://github.com/KellyChan/notebook/blob/master/tech/2014011-ML5_Big_Data_and_Map_Reduce.md)

---
Feb 2 2014| big_data, map_reduce | Kelly Chan
# Big Data and Map Reduce

MapReduce: a framework for distributed computing

Summary  
Pros: Processes a massive job in a short period of time  
Cons: Algorithms must be rewritten; requires understanding of systems engineering  
Data: Numeric values, nominal values  

### 1. Machine Learning Algorithms for MapReduce  
- Naive Bayes
  * mapper: results of the probability of a feature
  * reducer: sum up results
  
- k-Nearest Neighbors (kNN)
  * tree: to narrow search for cloest vectors
  
- Support Vector Machines (SVM)
  * Pegasos algorithm: stochastic gradient descent
  
- Singular Value Decomposition (SVD)
  * Lanczos algorithm: find the singular values in a large matrix
  
- k-means Clustering
  * Canopy clustering

### 2. Toolkits

- [Amazon AWS](http://aws.amazon.com/)
- [Apache Mahout](http://mahout.apache.org/)

### 3.Example

mapper
```

import sys
from numpy import mat, mean, power

def dataLoad(dataFile):
    for line in dataFile:
        yield line.rstrip()

# creating a list of data lines
data = dataLoad(sys.stdin)
data = [float(line) for line in data] # overwriting with floats
n = len(data)
dataMatrix = mat(data)
squaredDataMatrix = pwoer(dataMatrix, 2)
        
# output size, mean, mean(square values)
print "%d\t%f\t%f" % (n, mean(dataMatrix), mean(squaredDataMatrix)) #calculating mean of columns
print >> sys.stderr, "report: still alive" 

```

reducer
```

import sys
from numpy import mat, mean, power

def dataLoad(dataFile):
    for line in dataFile:
        yield line.rstrip()


# creating a list of lines from dataFile
data = dataLoad(sys.stdin)
       
# spliting data lines into separte items and storing in list of lists
mapperOut = [line.split('\t') for line in data]

# accumulating total number of samples, overall sum and overall sum squared
accumulateN = 0.0
accumulateSum = 0.0
accumulateSumSquared = 0.0

for instance in mapperOut:
    thisN = float(instance[0])
    accumulateN += thisN
    accumulateSum += thisN * float(instance[1])
    accumulateSumSquared += thisN * float(instance[2])

# calculating means
mean = accumulateSum / accumulateN
meanSq = accumulateSumSquared / accumulateN

# printing size, mean, mean squared
print "%d\t%f\t%f" % (accumulateN, mean, meanSq)
print >> sys.stderr, "report: still alive"

```

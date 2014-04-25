Apr 22 2014 | sklearn, ML | Kelly Chan
# Examples of Scikit-learn

## 1. Sampling / rows

### sampling 
- Hiden Markov Model (HMM) - mean, covariance

### parameter estimation
- random search, grid search, random forest

## 2. Features / columns

### feature elimination
- univariate - F-test with significant features
- anova svm - pipeline(anova_filter, svm)
- feature_selection/RFE  - digits
- feature_selection/RFECV - KFold - classification

### standarization
- StandardScaler



## 3. Algorithms

### classification
- svm - digit recognizer
- pca + logistic regression - digit recognizer
- logistic regression - multiclassification
- multilabel classification - OneVsRestClassifier
- multi-output classification - knn, extra-tree,  linear regression, ridge - face completion
- KNeighborsClassifier
- DecisionTreeClassifier
- RandoForestClassifier
- AdaBoostClassifier
- GaussianNB
- LDA
- QDA
- BernoulliRBM, logistic regression - digit recognizer


### cross validation
- K folds
- grid search
- random search

## 4. Evaluations

- precision recall - classification
- ROC curve (cross validation?) - classification
- confusion matrix - classification


### Statistics

- score, permutation score, p-value - classification
- train errors, test errors, coef


## TOPIC: Text Mining

### 1. Feature 

#### feature extraction
- grid search
- DictVectorizer, FeatureHasher - frequency dict / raw tokens
- TfidfVectorize

### 2. Algorithms

#### classification
- SGDClassifier
- MultinomialNB

---
### Reference
[Scikit-learn Examples](http://scikit-learn.org/stable/auto_examples/index.html)

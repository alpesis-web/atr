Apr 22 2014 | sklearn, ML | Kelly Chan
# Examples of Scikit-learn

## 1. Sampling

- Hiden Markov Model (HMM) - mean, covariance

## 2. Features

### feature elimination
- univariate - F-test with significant features
- anova svm - pipeline(anova_filter, svm)
- feature_selection/RFE  - digits
- feature_selection/RFECV - KFold - classification

## 3. Algorithms

### classification
- svm - digit recognizer
- pca + logistic regression - digit recongizer

### cross validation
- K folds

## 4. Evaluations

- precision recall - classification
- ROC curve (cross validation?) - classification
- confusion matrix - classification


### Statistics

- score, permutation score, p-value - classification
- train errors, test errors, coef


---
### Reference
[Scikit-learn Examples](http://scikit-learn.org/stable/auto_examples/index.html)
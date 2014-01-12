Jan 12 2014 | Recommendation_System, Algorithms, DM | Kelly Chan
# Recommendation Algorithms

Data Table

|               | Person1       | Person2    | Person3    | Person4    | ...    |
| ------------- |:-------------:|:----------:|:----------:|:----------:| ------:|
| Article1      | rating        | rating     | rating     | rating     | ...    |
| Article2      | rating        | rating     | rating     | rating     | ...    |
| Article3      | rating        | rating     | rating     | rating     | ...    |
| ...           | ...           | ...        | ...        | ...        | ...    |

### 1. Collaborative Filtering
* user-based

    1. <b>(rating) distance</b> --- data dense (almost no missing)
        * Manhanttan
        * Euclidean
        * Supremum
    2. <b>(rating) pearson</b> --- grade-infalation - different scales for different users
    3. <b>(rating) cosine similarity</b> --- data sparse
    4. <b>(n users) pearson -> k nearest neighbor</b> --- How well does the specific user would like the specific book?
    
* item-based

     1. adjusted cosine similarity --- median
     2. slope one

### 2. Classification
* k nearest neighbor
* bayes

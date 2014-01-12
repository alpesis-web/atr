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

    1. (rating) distance
    2. (rating) pearson
    3. (rating) cosine similarity
    4. (n users) pearson -> k nearest neighbor
    
* item-based

     1. adjusted cosine similarity
     2. slope one

### 2. Classification
* k nearest neighbor
* bayes

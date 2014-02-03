Feb 2 2014| big_data, map_reduce | Kelly Chan
# Big Data and Map Reduce

MapReduce: a framework for distributed computing

Summary  
Pros: Processes a massive job in a short period of time  
Cons: Algorithms must be rewritten; requires understanding of systems engineering  
Data: Numeric values, nominal values  

Machine Learning Algorithms for MapReduce  
- Naïve Bayes  
> This is one of a few algorithms that’s naturally implementable in MapReduce. In MapReduce, it’s easy to calculate sums. > In naïve Bayes, we were calculating the probability of a feature given a class. We can give the results from a given    > class to an individual mapper. We can then use the reducer to sum up the results.

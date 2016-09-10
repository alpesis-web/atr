Mar 12 2014 | prediction, DM, sports | Kelly Chan
# Predictive Modeling for Sports Games

table of contents
- 1. Games
     - Football
     - Basketball
- 2. Modeling
     - Rating - scores
     - Ranking - seeds

## 1. Games

### (1) Football

prediction = historicalKicks + recentStatus

kickRate = ( total # of kicks + # of kicks of recent fives) / # of games

### (2) Basketball

winProb = 0.5 + 0.03 * diffRanks  
Win % = 0.50 + 0.03 * (weak seed minus strong seed) 

Rating = 100 - 4*LN(rank+1) - rank/22  
WinPct(RatingDiff) = 1/(1+POWER(10,-RatingDiff/C))  
WinPct(RatingDiff) = 1/(1+POWER(10,-RatingDiff/15))  -- basketball: 15


## 2. Modeling

- step1. calculating rating/ranking for each team  --> diffRating/diffRanking
- step2. logistic regression to predict win probability
- step3. predicting results for team-team pair

### Rating - scores
### Ranking - seeds

---
### References
modeling  
1. [Elo rating system](http://en.wikipedia.org/wiki/Elo_rating_system)  
2. [Sports rating system](http://en.wikipedia.org/wiki/Sports_rating_system)  
3. [Chess rating system](http://en.wikipedia.org/wiki/Chess_rating_system)

maths  
1. [Logistic distribution](http://en.wikipedia.org/wiki/Logistic_distribution)  
2. [Logistic function](http://en.wikipedia.org/wiki/Logistic_curve)

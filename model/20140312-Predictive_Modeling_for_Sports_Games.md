Mar 12 2014 | prediction, DM, sports | Kelly Chan
# Predictive Modeling for Sports Games

### 1. Football

prediction = historicalKicks + recentStatus

kickRate = ( total # of kicks + # of kicks of recent fives) / # of games

### 2. Basketball

winProb = 0.5 + 0.03 * diffRanks  

WinPct(RatingDiff) = 1/(1+POWER(10,-RatingDiff/C)) - C is constant, basketball: 15

---
### Reference
1. [Elo rating system](http://en.wikipedia.org/wiki/Elo_rating_system)

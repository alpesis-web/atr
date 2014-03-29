Mar 29 2014 | rating | Kelly Chan
# Rating System

Rating:
- quality > frequencies
- 3 wins > 10 losses
- if beat strong team, points++, if weak team, points--

Rnew = Rpre + k * (real - expect)  
- Rnew: new rating score
- Rpre: previous rating score
- k: k facotrs
- real/expected: real score and expected score


Prob = 1 / (10^(Rnew - Roppo) + 1)
- Rnew: new rating score
- Roppo: opposite score

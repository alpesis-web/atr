Apr 17 2014 | routing, algorithms | Kelly Chan
# Routing Algorithms


## 1. Types
- addressing, forwarding, routing
- distance-vector algorithms
- link-state algorithms

### Addressing, Forwarding, Routing

- addressing / nodes: A, B, C, D, ...
- links: -> A, -> B
- link cost: A->B/100, D->B/40

tables:
- forwarding: self
- routing: correct forwarding + total costs

nodes:
- know current neighbor links and costs
- exchange simple info, repeatedly
- aim to establish optimal routing ASAP


### Distance-Vector Algorithms

maintain, exchange, neighbors routing distance tables

### Link-State Algorithms

memorize, forward neighbor/cost info for every node

---
### References
1. [Routing Algorithms - MIT](http://web.mit.edu/6.02/www/currentsemester/handouts/L20_slides.pdf)

Mar 6 2014 | visualization, matplotlib, python | Kelly Chan
# Plotting with Matplotlib

```python
import matplotlib.pyplot as plt
```

## 1. Matlab like API

```python
from pylab import *
```
example
```python
x = linspace(0, 5, 10)
y = x ** 2

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-');
show()
```

## 2. Matplotlib Object-Oriented API

```python
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

plt.show()
```


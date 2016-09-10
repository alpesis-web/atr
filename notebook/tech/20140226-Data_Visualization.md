Feb 26 2014 | Data_Visualization | Kelly Chan
# Data Visualization

### 1. perception of visual cues (1985 AT&T Labs on graphical perception)
- accurate: position > length > angle > direction > area > volumn > saturation > hue

### 2. Plotting
- matplotlib
- ggplot

grammar of graphics
- plot: x-position, y-position
- shapes: points, lines, bars, sizes, colors

ggplot
- step1. creating plot
- step2. representing data with geometric objects
- step3. adding labels

```
print ggplot(data, aes(xvar, yar)) 
+ geom_point(color='coral') + geom_line(color='coral') 
+ ggtitle('title') + xlab('x-label') + ylab('y-label')
```

### 3. Data Types

- numeric
- factors/categories
- time series

Mar 13 2014 | EDA, data_analysis | Kelly Chan
# Exploratory Data Anlaysis

## 1. Toolkit

### R

plotting: libraries ggplot2 and RColorBrewer
```{r}
install.packages('ggplot2', dependencies = TRUE)
library(ggplot2)
install.packages('RColorBrewer', dependencies = TRUE)
library(RColorBrewer)
```
Rmd/RMarkdown: library knitr
```{r}
install.packages('knitr', dependencies = T) 
library(knitr)
```

## 2. Exploratory

### 1. One Variable

Histogram: 
```
names(pf)
qplot( x = dob_day, data = pf) + 
     scale_x_discrete(breaks = 1:31) +
     facet_wrap(~dob_month, ncol = 3)

ggplot(aes(x = friend_count), data = pf) +
     geom_histogram()
```
facet\_wrap() and facet_grid()
```
facet_wrap(~variable)
facet_grid(vertical ~ horizontal)
```

### 2. Two Variables
### 3. More Variables

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
qplot( x = dob_day, data = pf, binwidth=25) + 
     scale_x_discrete(breaks = 1:31) +
     facet_wrap(~dob_month, ncol = 3)

ggplot(aes(x = friend_count), data = pf) +
     geom_histogram() + 
     scale_x_continuous(limits = c(0, 1000), breaks = seq(0,1000,50)) +
     facet_wrap(~gender)


ggplot(aes(x = friend_count), data = na.omit(pf)) +
     geom_histogram() + 
     scale_x_continuous(limits = c(0, 1000), breaks = seq(0,1000,50)) +
     facet_wrap(~gender)

ggplot(aes(x = friend_count), data = subset(pf, is.na(gender))) +
     geom_histogram() + 
     scale_x_continuous(limits = c(0, 1000), breaks = seq(0,1000,50)) +
     facet_wrap(~gender)
```
facet\_wrap() and facet_grid()
```
facet_wrap(~variable)
facet_grid(vertical ~ horizontal)
```

summary table
```
table(pf$gender)
by(pf$friend_count, pf$gender, summary)
```

### 2. Two Variables
### 3. More Variables

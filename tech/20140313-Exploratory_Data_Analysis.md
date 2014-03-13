Mar 13 2014 | EDA, data_analysis | Kelly Chan
# Exploratory Data Anlaysis

## 1. Toolkit: R

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
library gridExtra
```{r}
install.packages('gridExtra')
library(gridExtra)
```

## 2. Exploratory

### 1. One Variable

Histogram: 
```
names(pf)
qplot( x = dob_day, data = pf, binwidth=25, color=I('black'), fill=I('#099009')) + 
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
     
ggplot(aes(x = tenure/365), data = pf) + 
     geom_histogram(binwidth = .25, color = 'black', fill = '#F79420')

ggplot(aes(x = tenure / 365), data = pf) + 
  geom_histogram(color = 'black', fill = '#F79420') + 
  scale_x_continuous(breaks = seq(1, 7, 1), limits = c(0, 7)) + 
  xlab('Number of years using Facebook') + 
  ylab('Number of users in sample')
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

transforming data
```
qplot(x=friend_count, data=df)

summary(pf$friend_count)
summary(log10( pf$friend_count + 1 ))
summary(sqrt( pf$friend_count ))


library(gridExtra)
p1 <- qplot(x = friend_count, data =df)
p2 <- qplot(x = log10(friend_count + 1), data =df)
p3 <- qplot(x = sqrt(friend_count), data =df)
grid.arrange(p1, p2, p3, ncol=1)

p1 <- ggplot(aes(x=friend_count), data=df) + geom_histogram()
p2 <- p1 + scale_x_log()
p3 <- p1 + scale_x_sqrt()
grid.arrange(p1, p2, p3, ncol=1)
```


### 2. Two Variables
### 3. More Variables
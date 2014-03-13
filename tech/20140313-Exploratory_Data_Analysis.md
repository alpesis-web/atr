Mar 13 2014 | EDA, data_analysis | Kelly Chan
# Exploratory Data Anlaysis
Table of Contents
- Toolkit: R
- Exploratory
    - one variable: histogram/ frequency polygons/ boxplot | summary/ transformation/ logical
    - two variables: scatterplot
    - more variables:

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
plotted pics arranged: library gridExtra
```{r}
install.packages('gridExtra')
library(gridExtra)
```

library: dplyr
```{r}
install.packages('dplyr')
library(dplyr)

filter()
group_by()
mutate()
arrange()
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

Frequency Polygons
```
qplot(x=friend_count, data=subset(pf, !is.na(gender)), binwidth=10, geom='freqpoly', color=gender) +
    scale_x_continuous(lim=c(0, 1000), breaks = seq(0, 1000, 50)) 

ggplot(aes(x = friend_count, y = ..count../sum(..count..)), data = subset(pf, !is.na(gender))) + 
  geom_freqpoly(aes(color = gender)) + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) + 
  xlab('Friend Count') + 
  ylab('Percentage of users with that friend count')

ggplot(aes(x = www_likes), data = subset(pf, !is.na(gender))) + 
  geom_freqpoly(aes(color = gender)) + 
  scale_x_log10()
```

Box Plot
```
qplot(x=gender, y=friend_count, 
      data=subset(pf, !is.na(gender)), 
      geom='boxplot', ylim=c(0,1000))

qplot(x=gender, y=friend_count, 
      data=subset(pf, !is.na(gender)), 
      geom='boxplot') +
     coord_cartesion(ylim=c(0,1000))

by(pf$friend_count, pf$gender, summary)
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
by(pf$www_likes, pf$gender, sum)
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

getting logical
```
summary(pf$mobile_likes)
summary(pf$mobile_likes > 0)

mobile_check_in <- NA
pf$mobile_check_in <- ifelse(pf$mobile_likes > 0, 1, 0)

summary(pf$mobile_check_in)
sum(pf$mobile_check_in == 1) / length(pf$mobile_check_in)
```


### 2. Two Variables

scatterplot
```
qplot (x=age, y=friend_count, data=pf)

ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_point(alpha = 1/20, position = position_jitter(h = 0)) +
  xlim(13,90) +
  coord_trans(y = 'sqrt')

ggplot(aes(x = age, y = friend_count), data = pf) + 
  geom_jitter(alpha = 1/20) +
  xlim(13,90)

```

conditional means
```
library(dplyr)

age_groups <- group_by(pf, age)
pf.fc_by_age <- summarise(age_groups,
          friend_count_mean <- mean(friend_count),
          friend_count_median <- median(friend_count),
          n = n())
pf.fc_by_age <- arrange(pf.fc_by_age, age)

head(pf.fc_by_age)


pf.fc_by_age <- pf %.%
    group_by(age) %.%
    summarise(friend_count_mean <- mean(friend_count),
              friend_count_median <- median(friend_count),
              n = n()) %.%
    arrange(age)
    
head(pf.fc_by_age)
```
### 3. More Variables

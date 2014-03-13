Mar 13 2014 | EDA, data_analysis | Kelly Chan
# Exploratory Data Anlaysis
Table of Contents
- Toolkit: R
- Exploratory
    - one variable: histogram/ frequency polygons/ boxplot | summary/ transformation/ logical
    - two variables: scatterplot | correlation
    - more variables: ratio plot | reshape
- Case Study: Diamonds and Price Prediction

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
library: reshape2
```
install.packages('reshape2')
library(reshape2)
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
    
head(pf.fc_by_age, 20)

ggplot(aes(age, friend_count_mean), data=pf.fc_by_age) + geom_point()
```
summary plot with scatter
```
ggplot(aes(x = age, y = friend_count), data = pf) + 
  xlim(13,90) +
  geom_point(alpha = 0.05, 
             position = position_jitter(h = 0),
             color = 'orange') +
  coord_trans(y = 'sqrt') +
  geom_line(stat = 'summary', fun.y = mean) +
  geom_line(stat = 'summary', fun.y = quantitle, prob = .1, linetype = 2, color = 'blue') +
  geom_line(stat = 'summary', fun.y = quantitle, prob = .5, color = 'blue') +
  geom_line(stat = 'summary', fun.y = quantitle, prob = .9, linetype = 2, color = 'blue')
```

correlation
```
cor.test(pf$age, pf$friend_count, method='pearson')
with(pf, cor.test(age, friend_count, method='pearson'))
with(subset(pf, age <= 70), cor.test(age, friend_count, method='pearson'))

ggplot(aes(x=www_likes_received, y=likes_received), data=pf) + 
    geom_point() +
    xlim(0, quantitle(pf$www_likes_received, 0.95)) +
    ylim(0, quantitle(pf$likes_recieved, 0.95)) + 
    geom_smooth(method = 'lm', color='red')
```

time series
```
ggplot(aes(x=(Month%%12),y=Temp),data=Mitchell)+ 
  geom_point()
```

### 3. More Variables

reshaping data: long -> wide
```
library(reshape2)
pf.fc_by_age_gender.wide <- dcast(pf.fc_by_age_gender,
                                  age ~ gender,
                                  value.var = 'median_friend_count')
head(pf.fc_by_age_gender.wide)


pf.fc_by_age_gender.wide <- pf.fc_by_age_gender %.% 
  group_by(age) %.% 
  summarise(male = friend_count.median[gender = 'male'], 
                      female = friend_count.median[gender = 'female'], 
                      ratio = female / male) %.% 
  arrange(age)
  
head(pf.fc_by_age_gender.wide)
```

ratio plot
```
ggplot(aes(x=age, y=female/male), 
       data = pf.fc_by_age_gender.wide) +
       geom_line() +
       geom_hline(yintercept=1, alpha=0.3, linetype=2)
```

---
### Case Study: Diamonds and Price Prediction

Price
```
library(gridExtra)

plot1 <- qplot() + 
  ggtitle('Price')

plot2 <- qplot() +
  ggtitle('Price (log10)')

grid.arrange()
```

overplotted visited
```
ggplot(aes(carat, price), data = diamonds) + 
  geom_point() + 
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')
```

Price vs. Carat and Clarity
```
library(RColorBrewer)

ggplot(aes(x = carat, y = price), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
    guide = guide_legend(title = 'Clarity', reverse = T,
    override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
    breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
    breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Clarity')
```

Price vs Carat and Cut
```
ggplot(aes(x = carat, y = price, color = clarity), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = 'Clarity', reverse = T,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Clarity')
```
Price vs Carat and Color
```
ggplot(aes(x = carat, y = price, color = cut), data = diamonds) + 
  geom_point(alpha = 0.5, size = 1, position = 'jitter') +
  scale_color_brewer(type = 'div',
                     guide = guide_legend(title = Cut, reverse = T,
                                          override.aes = list(alpha = 1, size = 2))) +  
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat and Cut’)
```

Building the Linear Model
```
m1 <- lm(I(log(price)) ~ I(carat^1/3), data=diamonds)
m2 <- update(m1, ~ . + carat)
m3 <- update(m2, ~ . + cut)
m4 <- update(m3, ~ . + color)
m5 <- update(m4, ~ . + clarity)
mtable(m1, m2, m3, m4, m5)
```

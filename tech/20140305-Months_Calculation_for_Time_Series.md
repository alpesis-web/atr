Mar 5 2014 | time_series | Kelly Chan
# Mmonths Calculation for Time Series

```asp
DateTime time1 = DateTime.Parse("2012-7-30"); //起始日期  
DateTime time2 = DateTime.Parse("2013-6-29"); //结束日期  
Response.Write((time2.Year * 12 - (12-time2.Month)) - (time1.Year * 12 -(12-time1.Month))); 
```

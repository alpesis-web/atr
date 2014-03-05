Mar 5 2014 | time_series | Kelly Chan
# Months Calculation for Time Series

```asp.net
DateTime time1 = DateTime.Parse("2012-7-30"); // start date
DateTime time2 = DateTime.Parse("2013-6-29"); // end date 
Response.Write((time2.Year * 12 - (12-time2.Month)) - (time1.Year * 12 -(12-time1.Month))); 
```

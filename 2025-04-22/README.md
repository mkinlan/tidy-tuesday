# Fatal Crash Data

This week's [#TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/main/data/2025/2025-04-22/readme.md)  data is a subset of U.S. Census data on fatal car crashes in the U.S.

This is obviously a very somber subject, and I thank the researchers that worked to put together this dataset, no doubt with the goal of improving mortality rates and reducing accidents. Thank you for the good work you do. 

I took this opportunity to learn more about time series data and autocorrelation plots, which explore the relationships between a time series and lagged versions of itself. 

The plot below is of monthly data from 1992-2016 correlated with lagged versions of itself going back 60 lags (aka, 60 months). 

Each spike on the plot is the value of the correlation (aka relationship, association, etc.) between a specific month and the number of lags at that point on the x-axis. 

For example, there is a moderate spike at Lag 1 with a correlation of -0.5.

Lag 1 means "1 month prior", so the value of -0.5 is the result of comparing each month in the time series to the month prior to it (aka Dec vs Nov, Nov vs. Oct, Oct vs Sept, etc.). 

Since this is a negative correlation, the relationship between any given month and the month prior is an opposite one. One might interpret this as something like "Each month is moderately affected by the month before it. If the prior month had high values, the current month is moderately likely to have lower values."

Another moderately significant lag is at Lag 12. Using the same logic as above, this might be interpreted as "Each month is moderately influenced by the same month in the year prior. If September of last year was high, then September of this year is moderately likely to be lower."

![plot](plot.png)

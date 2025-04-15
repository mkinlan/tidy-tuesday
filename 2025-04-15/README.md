# Palmer's Penguin Data

This week I explored Palmer's penguin dataset and used the resulting visualization for both [#TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/main/data/2025/2025-04-15/readme.md) and for Day 15 of the [#30DayChartChallenge](https://www.cedricscherer.com/2021/05/09/contributions-30daychartchallenge-2021/). 

Day 15's theme is "Complicated". While this joyplot is not particularly difficult, I definitely struggled to identify a workaround to get the legend to display all penguin types, because as the plot shows, not every penguin type can be found on every island. 

This resulted in some NaN values, which translated into joyplot thinking, "We don't need to show *that* penguin type in the legend." Womp, womp. 

The solution? Data masking in numpy! 

### Why mask data? 
I wanted to leave the gaps in the data so that users could see that some penguin types were present on some islands, but not on every island. One way to handle this would have been to replace all NaN values with zeros. However, I wanted to maintain the data in it's original form, and I also wanted to practice using this technique, which can be particularly useful for something like a line plot, where a gap in the line would look quite different if it was substituted with a zero.

![plot](plot.png)

### Coding

```python
import PyDyTuesday
import pandas as pd
import plotly.express as px
from joypy import joyplot
import numpy as np
import matplotlib.pyplot as plt

PyDyTuesday.get_date('2025-04-15')

dfp = pd.read_csv('penguins.csv')

dfp=dfp.dropna()

#Explore data

#Bubble Chart
fig = px.scatter(dfp.query("sex=='female' and species=='Adelie'"), x="bill_len", y="bill_dep",
	         size="flipper_len", color="island",
                 hover_name="island", log_x=True, size_max=60,
                 labels={
                    "bill_len": "Bill Length (mm)",
                    "bill_dep": "Bill Depth (mm)",
                    "island": "Island"
                 },
                 title="Female Adelie Penguins ")
fig.show()


#JoyPlot / RidgePlot:
dfJoy = dfp.pivot_table(index=['sex','island'],columns='species',values='body_mass')

#masking NANs with zeros so the legend in the plot will recognize missing data
dfJoy['Chinstrap']=dfJoy['Chinstrap'].mask(dfJoy['Chinstrap'].isna(),0)
dfJoy['Gentoo']=dfJoy['Gentoo'].mask(dfJoy['Gentoo'].isna(),0)

# changing island index names for readability
dfJoy.rename(index={'Biscoe': 'Biscoe Island',
'Dream': 'Dream Island',
'Torgersen': 'Torgersen Island'}, level=1, inplace=True) #multi index so level 1 for island

plt.figure(figsize=(12,6))
fig, axs = joyplot(data=dfJoy,
                    by='island',
                    column=['Adelie','Chinstrap','Gentoo'],
                    color=['#43bf60','#2b7acf', '#f59f0a'],
                    x_range=[1000,7000],
                    alpha=.67,
                    legend=True,
                    overlap=2,
                    linewidth=.5,
                    title='Penguin Body Mass per Island by Type'
                    )
```

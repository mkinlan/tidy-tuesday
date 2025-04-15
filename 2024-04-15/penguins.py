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

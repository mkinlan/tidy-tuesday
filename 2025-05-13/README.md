# Seismic Events

This week's [#TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/main/data/2025/2025-05-13/readme.md) data is Mt. Vesuvius eruptions.

I took the opportunity to learn more about how to use Plotly graph objects. In particular, the syntax for graph objects and text box annotations, (which took far too long to position properly using code!).  Professional advice - if this is for work, save yourself 45 minutes and just copy the chart as an image, then add a text box in Powerpoint or Canva. 

Since this is volcanic eruptions, I chose a darker black and orange color palette instead of the plotly defaults. I found it interesting to see how large the margin of erros are for these small-magnitude eruptions, which I don't think I would have noticed had I note added the error boundaries.

See below the image for full code used to create it:

![image](https://github.com/user-attachments/assets/658d3950-b200-46c4-aad9-cab4d99c5fbc)


```python
import PyDyTuesday
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from joypy import joyplot
import numpy as np
import matplotlib.pyplot as plt
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap

vesuvius = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-05-13/vesuvius.csv')

z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')


df=vesuvius.pivot_table(index=['year'],values=['duration_magnitude_md','md_error']).reset_index()
df['upper_bound']=df.apply(lambda x: x.duration_magnitude_md + x.md_error, axis=1)
df['lower_bound']=df.apply(lambda x: x.duration_magnitude_md - x.md_error, axis=1)

#fancier line plot
fig = px.line(df, x="year", y = "duration_magnitude_md", title="Mt. Vesuvius Eruptions",
    labels = {
        "year":"Year",
        "duration_magnitude_md" : "Duration & Magnitude"
    }
)
fig.update_xaxes(type='category',tickvals=df['year'].tolist())
fig.add_scatter(x=df['year'], y=df['md_error'], mode='lines')
fig.show()

#even fancier line plot filling in error with single trace
fig = go.Figure([
    go.Scatter(
        name = 'Duration Magnitude',
        x=df['year'],
        y = df['duration_magnitude_md'],
        mode = 'lines',
        marker=dict(
            color='rgb(149,10,17)'
        )
    ),
    go.Scatter(
        name='M.E. Upper Bound',#first trace
        x=df['year'],
        y=df['md_error'] + df['duration_magnitude_md'],
        mode='lines',
        marker=dict(color='black'),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='M.E. Lower Bound',#second trace
        x=df['year'],
        y=df['duration_magnitude_md'] - df['md_error'],
        mode='lines',
        marker=dict(color='black'),
        line=dict(width=0),
        #fillcolor='rgba(255, 193, 0, 0.8)',
        fillcolor='rgba(240,102,37,0.45)',
        fill='tonexty', #fills area between two traces
        showlegend=False
   )
])
fig.update_xaxes(
    type='category',
    tickvals=df['year'].tolist(),#show all years
    #gridcolor='rgb(51,51,51)',
    #color='white'
    ) 

#fig.update_yaxes(
#    gridcolor='rgb(51,51,51)',
#    color='white'
#)

#I think it uses the right side of the legend as the anchor point
fig.update_layout(
    legend=dict(
    yanchor="top",
    y=0.85,
    xanchor="right",
    x=0.95,
    #font=dict(color='white')
    ),
    title=dict(
        text='Mt. Vesuvius Eruptions',
        font=dict(color='white'),
        subtitle=dict(
            text='Duration magnitude of seismic events from 2011-2024',
            #font=dict(color='white',size=13),
        )
    ),
    
    #plot_bgcolor='rgb(51,51,51)',
    #paper_bgcolor='rgb(51,51,51)'
    
)

fig.add_annotation(
        x=0.25,
        y=0.40,
        xref="paper",
        yref="paper",
        text="M.E. upper bound",
        showarrow=True,
        font=dict(
            #family="Open Sans",
            size=11,
            color="white"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="rgb(51,51,51)",
        opacity=0.8
        )
fig.add_annotation(
        x=0.15,
        y=0.15,
        xref="paper",
        yref="paper",
        text="M.E. lower bound",
        showarrow=True,
        font=dict(
            #family="Open Sans",
            size=11,
            color="white"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=-20, #starting point of arrow (tail) neg. means points to right
        ay=30, #ending point of arrow (head)
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="rgb(51,51,51)",
        opacity=0.8
        )
# Add the citation annotation
fig.add_annotation(
    x=1.0,  # Horizontal position (right)
    y=-0.1, # Vertical position (below the plot)
    xref="paper",
    yref="paper",
    text="Morgana Kinlan",
    showarrow=False,
    font=dict(size=10)
)
fig.update_layout(template="plotly_dark")        
fig.show()

#print(fig)
```


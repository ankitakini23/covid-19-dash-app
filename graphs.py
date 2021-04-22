import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime
from datetime import date
from datetime import timedelta

from data import data_set_today 
from data import data_set_yesterday,data_set_yesterday2
from data import covid_data_set as df
colors = {
    'background': '#172238',
    #'background':'#242729',
    'text': '#a8ffff',
}
df1=data_set_today
df2=data_set_yesterday
df3=data_set_yesterday2

continents=['Asia','World','Europe','North America','South America']
df_continents=df1[df1['Country'].isin(continents)]

df=df[~df['Country'].isin(continents)]
df1=df1[~df1['Country'].isin(continents)]
df2=df2[~df2['Country'].isin(continents)]
df3=df3[~df3['Country'].isin(continents)]


# df1=df[df['Date']==str(datetime.date.today())]#.head(15)
# df2=df[df['Date']==str(datetime.date.today()-timedelta(days=1))]#.head(15)

total_confirmed=int(df_continents[df_continents['Country'] == 'World']['TotalCases'])#, 'TotalCases'])
total_recovered=int(df_continents.loc[df_continents['Country'] == 'World']['TotalRecovered'])#, 'TotalRecovered']
total_deaths=int(df_continents.loc[df_continents['Country'] == 'World', 'TotalDeaths'])


#Cloropeth Map--Total cases for Today's data
fig1=px.choropleth(df1 , locations = 'Country' , 
 	locationmode='country names',color='TotalCases',title='Global COVID-19 Map', color_continuous_scale=px.colors.diverging.balance)
fig1.update_layout(
 font_color='white',
 plot_bgcolor=colors['background'],
 paper_bgcolor=colors['background'],
 width=1000,
 height=480, 
	)
# fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Pie Chart-Total Cases for First 15 Countries--Today's data set
fig2 = px.pie(df1.head(15), values='TotalCases', names='Country', title='Total Cases',color_discrete_sequence=px.colors.sequential.RdBu)
fig2.update_layout(
    margin=dict(l=20, r=10, t=10, b=10),
    width=400,
    height=390,
    paper_bgcolor=colors['background'],
    plot_bgcolor=colors['background'],
    font_color='white',
)
#Histogram for Total Cases and Countries
fig3 = px.histogram(df1,x="Country", y="TotalCases",
					nbins=40,
					)
fig3.update_layout(
 title_text='Histogram showing the Spread of Total Cases', # title of plot
 xaxis_title_text='Country', # xaxis label
 yaxis_title_text='Total Cases', # yaxis label
 title_font_color='white',
 legend_font_color='white',
 legend_title='Date',
 legend_title_font_color='white',
 font_color='white',
 plot_bgcolor=colors['background'],
 paper_bgcolor=colors['background'],

)
#Bar Chart-New Cases-today vs yesterday vs day before yesterday
fig4 = go.Figure()
fig4.add_trace(go.Bar(
 						x=df1['Country'].head(10), 
						y=df1['NewCases'].head(10),
						name=str(datetime.date.today()),
						marker_color='#fc8d62',
						opacity=0.75))
fig4.add_trace(go.Bar(
						x=df2['Country'].head(10), 
						y=df2['NewCases'].head(10),	
						name=str(datetime.date.today()-timedelta(days=1)),
						marker_color='#a3fff4',
						opacity=0.75))
fig4.add_trace(go.Bar(
						x=df3['Country'].head(10), 
						y=df3['NewCases'].head(10),	
						name=str(datetime.date.today()-timedelta(days=2)),
						marker_color='#3998b3',
						opacity=0.75))
fig4.update_layout(barmode='group',
 title_text='Yesterday Vs Today', # title of plot
 xaxis_title_text='Country', # xaxis label
 yaxis_title_text='New Cases', # yaxis label
 bargap=0.2, # gap between bars of adjacent location coordinates
 bargroupgap=0.1, # gap between bars of the same location coordinates
 title_font_color='white',
 legend_font_color='white',
 legend_title='Date',
 legend_title_font_color='white',
 font_color='white',
 plot_bgcolor=colors['background'],
 paper_bgcolor=colors['background'],

)
#fig.show()

df1=df1.nlargest(15, ['NewCases'])
#Horizontal Bar Graph of Countries with the highest New Cases
fig5 = go.Figure()
fig5.add_trace(go.Bar(	x=df1['NewCases'].head(15),
						y=df1['Country'].head(15), 
						name=str(datetime.date.today()),
						marker_color='#20ba8c',
						opacity=0.75,
						orientation='h'))
fig5.update_layout(barmode='group',
 title_text='Countries with the Highest Daily Cases Count', # title of plot
 yaxis_title_text='Country', # xaxis label
 xaxis_title_text='New Cases', # yaxis label
 height=490,
 #color=colors['text']
 paper_bgcolor=colors['background'],
 plot_bgcolor=colors['background'],
 font_color='white'
)
df1=data_set_today

fig6 = px.line(df1, x="Country", y="TotalCases")   

#Scatter Plot of NewCases and Total Cases for todays data
fig7 = px.scatter(df1, x="NewCases",y='TotalCases',size_max=40,
             size="TotalCases", color="TotalCases", hover_name="Country",
             log_x=True,
             #color_discrete_sequence = 'px.colors.colorbrewer.Paired')
             color_continuous_scale=px.colors.sequential.Bluyl,
           )
fig7.update_layout(
    #margin=dict(l=20, r=10, t=10, b=10),
    # width=400,
    # height=400,
    paper_bgcolor=colors['background'],
    plot_bgcolor=colors['background'],
    font_color='white'
)

#fig7=go.Figure()
# fig7.add_trace(go.Scatter(y=df1['NewCases'],
# 						x=df1['Country'], 
# 						hoverinfo='x+y',
# 						mode='markers',
# 						marker=dict(
# 				        color='red',
# 				        colorscale='Viridis', 
# 				        showscale=False,

#     )

# 	)
# 	)
# fig7.update_layout(barmode='group',
#  title_text='Sampled Results', # title of plot
#  xaxis_title_text='Country', # xaxis label
#  yaxis_title_text='New Cases', # yaxis label
#  plot_bgcolor=colors['background'],
#  paper_bgcolor=colors['background'],
#)

#Bar Graph -Active cases of countries
fig8 = go.Figure()
fig8.add_trace(go.Bar(	x=df1['ActiveCases'].head(10),
						y=df1['Country'].head(10), 
						name=str(datetime.date.today()),
						marker_color='#20ba8c',
						opacity=0.75,
						orientation='h'))
fig8.update_layout(barmode='group',
 #title_text='Active Cases', # title of plot
 xaxis_title_text='Active Cases', # xaxis label
 yaxis_title_text='Country', # yaxis label
 paper_bgcolor=colors['background'],
 plot_bgcolor=colors['background'],
 font_color='white'
)


#https://www.ft.com/content/a2901ce8-5eb7-4633-b89c-cbdf5b386938
#
#Daily deaths is the best indicator of the progression of the pandemic, although there is generally a 17-21 day lag between infection and deaths.

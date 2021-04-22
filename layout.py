#!usr/bin python3

import pandas as pd
import numpy as np
import math
import datetime
from datetime import date
from datetime import timedelta
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from data import covid_data_set as df
from graphs import fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,df1,df2,df
from graphs import total_confirmed,total_recovered,total_deaths
from app import app

colors = {
     'background': '#172238',
    #'background':'#596065',
    'text': '#7FDBFF'
}
#fig3,fig6 not added
def get_Header():
	header=	dbc.Container(
			children=dbc.Row(className="header",
				children=[
					 dbc.Col(
					 		 #id="banner",
					 		 className='col-8',
					 		 children=[
                             html.H2('Coronavirus tracker: the latest figures as countries fight the Covid-19 resurgence'),
                             html.P('Visualising the number of cases with Plotly - Dash.'),
                             ]),
					 dbc.Col(#className='col-2',

					 		width={"offset":1},
					 		#id="bannerLogo",
							children=[ 
							html.Img(id="logo", src=(app.get_asset_url("plotly_logo.png"))),#src="/home/hp/Documents/beautiful-soup/plotly_logo.png")],					 	)
					 ])
			]))
	return header
def get_emptyrow(h='45px'):
    """This returns an empty row of a defined height"""
    emptyrow = dbc.Row([
        ],
    className = 'empty-row col-12',
    style = {'height' : h})
    return emptyrow
def get_footer():
	markdown_text = '''
	## Acknowledgements

	* Dashboard written in Python using the [Dash](https://dash.plotly.com/) web framework. This enables us to interact with the visualizations.
	* Covid-19 data is scraped from [worldometers.info](https://www.worldometers.info/coronavirus/).
	* Data analysis and calculations implemented using Pandas Python Library.
	* Data visualisation built using [Plotly's](https://plotly.com/python/) Python graphing library.
	'''
	footer=dbc.Container(			
					dbc.Row(
					dbc.Col(className='footer',
						children=[dcc.Markdown(markdown_text)
						]
						))
			)
	return footer

def get_graphs():
	graphs=dbc.Container(		
		children=[
		dbc.Row(
			#style={'border-color' : 'white', 'border' : '1px solid'},
			children=[
					#1st col
					#dbc.Col("Overview",
					#	className="col-1"
					#	),
					#"2nd col",
					dbc.Col(	
						className='col-7',					
						children=[
						dbc.Row(							
							[
								dbc.Col(							
									children=[
									html.P('Total Confirmed:'),
									# dcc.Markdown('''
									# 	Total Confirmed:
									# 	'''),
									#'Total Confirmed:\n',
									html.P(str(total_confirmed)),
									#'\n'+str(total_confirmed)
									],
									className='col-4 text-red',
									style={
									'height':'100px',
									'padding-bottom':'10px',									
									}
								),
								dbc.Col(
									[html.P('Total Recovered:'),
									html.P(str(total_recovered))
									],
									className='col-4',
									id='text-green',
									style={
									'height':'100px',								
									}
								),
								dbc.Col(
									[html.P('Total Deaths:'),
									html.P(str(total_deaths))
									],
									className='graph-col col-4',
									style={
									'height':'100px',								
									}
								)							
							]
						),
						dbc.Row(
							[dbc.Col(className='graph-col',	
							#width={"offset":2},
							style={
							'align-items': 'center'							
							},
							children=[dcc.Graph(
								figure=fig7)
							])],

						),
						dbc.Row(
							dbc.Col(className='graph-col',
								style={
									'align-items': 'center'
								},
								#width={"size": 10,"offset":1},
	                            children=[
	                            html.P("Distribution by Countries - the top 15"),
	                            dcc.Graph(figure=fig2)
	                            ])
						)],				
					),
					#"3rd col",
					dbc.Col(
						className="col-5",
						#style={'border-color' : 'white', 'border' : '1px solid'},
						children=[
						dbc.Row(
							dbc.Col(className='graph-col',
							style={
							'align-items': 'center',							
							},
				# 			width={"size": 10,"offset":1},
                            children=[
                            html.P("Side by Side Comparison of The New Cases"),
                            dcc.Graph(figure=fig4)
                            ]
                            )
							),

						dbc.Row(
							dbc.Col(className='graph-col',
							style={
							'align-items': 'center',							
							},
							#width={"size": 10,"offset":1},
                            children=[                            
                            dcc.Graph(figure=fig5)
                            ])
							),

						])
					],
					#no_gutters=True
					),
		dbc.Row(
			children=[
			dbc.Col(className='graph-col',
				children=[
				dcc.Graph(
					id='chloropeth-graph',
					figure=fig1)
				]
				)]),
		dbc.Row(
			children=[
			dbc.Col(className='graph-col',
				children=[
				dcc.Graph(
					id='histogram',
					figure=fig3)
				]
				),
			dbc.Col(className='graph-col',
				children=[
				dcc.Graph(
					id='active-cases',
					figure=fig8)
				]
				)]),
		],
		)
					
				


					
			
				# dbc.Row(
				# 	# style={#'backgroundColor':'#1E1E1E',
				# 	# 		'border': 5,
				# 	# 		'padding-bottom':20,
				# 	# 		'box-shadow': '2px 3px 3px 0px #adb1b3',							
				# 	# 		'margin': '20px',
				# 	# 		'alignItems':'centre'},					
				# 	children=[
				# 	dbc.Col(className='graph-col',
				# 			width={"size": 4},
    #                         children=[
    #                         	dcc.Graph(id='scatterGraph',figure=fig7,
    #              #            	style= {
	   #              			# 'plot_bgcolor': colors['background'],
	   #              			# 'paper_bgcolor': colors['background'],
    #             				# 'font': {
    #             	# 			'color': colors['text']
		  #               		# }}
		  #               		)
    #                         ]),                                   
				# 	dbc.Col(className='graph-col',
				# 		width={"size": 4,"offset":2},
    #             		#style={'backgroundColor': '#1E1E1E'},
    #             	children=[
    #             	dcc.Graph(id='graph-with-slider',                    		
    #             		animate=True),
				#     dcc.Slider(
				#         id='TotalCases-slider',
				#         min=df1['TotalCases'].min()/2,
				#         max=df1['TotalCases'].max()*1.5,
				#         value =df1['TotalCases'].min(),	
				#         tooltip={"always_visible":True,"placement":'topLeft'},
				#         #marks={str(TotalCases): str(TotalCases) for TotalCases in df1['TotalCases'].unique()},
				#         step=df1['TotalCases'].min()*4,
				#     ),
    #             	]),						 		
				# 	]),					
				# 	#no_gutters=True		#horizontal spacing is added between the columns. Use no_gutters=True to disable this.
    #                 	
    #                 dbc.Row(
				# 	dbc.Col(className='graph-col',
				# 			width={"size": 10,"offset":1},
    #                         children=["Active Case By removing deaths and recoveries from total cases, we get \"currently infected cases\" or \"active cases\" (cases still awaiting for an outcome).",
    #                         dcc.Graph(figure=fig8)
    #                         ])
				# 	)
				# 	])                    
	return graphs

appLayout=dbc.Container(
				className='body',
				children=[
				get_Header(),	
				#get_emptyrow(),							
				get_graphs(),
				get_footer()
    			])

# @app.callback(
# Output('graph-with-slider', 'figure'),
# Input('TotalCases-slider', 'value'))
# def update_figure(selected_Totalcases):
# 	filtered_df = df1[df1.TotalCases <= selected_Totalcases]
# 	fig = px.scatter(filtered_df, x="TotalCases", color="Country", hover_name="Country",log_x=True,size_max=100,
# 		template='plotly_dark').update_layout(
#                                {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#                                 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                
# 	fig.update_layout(transition_duration=500)
# 	return fig

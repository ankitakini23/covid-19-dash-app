import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#from layout import appLayout

app = dash.Dash(__name__,
					external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server	
# app.layout = appLayout	

# logo_image=app.get_asset_url("plotly_logo.png")

# if __name__ == '__main__':
#     app.run_server(debug=False, use_reloader=True)  # Turn off reloader if inside Jupyter
server = app.server
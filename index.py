import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from layout import appLayout
from app import app,server

app.layout = appLayout	
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)  # Turn off reloader if inside Jupyter
from dash import Dash, html, dcc, callback, Input, Output, ctx
import plotly.express as px
import pandas as pd


df = pd.read_csv("output.csv")
app = Dash(__name__)
fig = px.line(df, x = "date", y = "sales", color="region", width=1200, height=500)
app.layout = html.Div(children = [
    html.Button("Button 1", id="btn-1"),
    html.Button("Button 2", id="btn-2"),
    html.Button("Button 3", id="btn-3"),
    html.H1(id="header",
            children="Hello Dash"),

    html.Div(children="""
        Dash: A web application framework for your data.
    """),

    dcc.Graph(
        id="example-graph",
        figure=fig
    )
])

@callback(
    Output("header", "children"),
    Input("btn-1", "n_clicks"),
    Input("btn-2", "n_clicks"))
def update1(btn1, btn2):
    return f"button 1:{btn1} & button 2: {btn2}"

@callback(
    Output("example-graph", "children"),
    Input("btn-1", "n_clicks"),
    Input("btn-2", "n_clicks"))
def update2(btn1, btn2):
    return f"button 1:{btn1} & button 2: {btn2}"

if __name__=="__main__":
    app.run_server(debug=True)

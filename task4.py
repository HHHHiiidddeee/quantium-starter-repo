from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def visualizeData():
    df = pd.read_csv("output.csv")
    app = Dash(__name__)
    fig = px.line(df, x = "date", y = "sales", color="region", width=1200, height=500)
    app.layout = html.Div(children = [
        html.H1(children="Hello Dash"),

        html.Div(children="""
            Dash: A web application framework for your data.
        """),

        dcc.Graph(
            id="example-graph",
            figure=fig
        )
    ])
    app.run_server(debug=True)

if __name__=="__main__":
    visualizeData()

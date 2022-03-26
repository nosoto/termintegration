from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


def weekly_data_p1():
    # ----------------  Data ---------------- #
    # Fetch Data from DB
    url = "https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/p1_raised_weekly/weekly/inc"
    raised1 = json.loads(urlopen(url).read())['items']

    # Create Empty Output Dictionariy in format needed for Graph
    dict_data = {}
    # Fill Dictionary with Week Numbers
    for i in range(1, 19):
        dict_data[i] = 0
    # Fill Dictionaty with Data
    for element in raised1:
        dict_data[int(element["to_char(create_time,'iw')"])] = element['count(*)']

    # ----------------  Figure ---------------- #
    fig = go.Figure()
    # Add Numbers
    fig.add_trace(go.Scatter(
        x=list(dict_data.keys()),
        y=list(dict_data.values()),
        name='P1 INCIDENTS',
        marker_color='#7e969e',
        line_shape='spline',
        text=list(dict_data.values())
    ))
    # Styling
    fig.update_layout(font_family="Helvetica Neue",
                      paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor='rgba(0,0,0,0)',
                      yaxis_title="P1 INCIDENTS", xaxis_title="CALENDAR WEEK 2021",
                      margin=dict(l=20, r=20, t=20, b=80),
                      legend=dict(bgcolor="white",
                                  font=dict(family="Helvetica Neue", color="black")))
    return fig
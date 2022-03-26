from urllib.request import urlopen
import json
import pandas as pd
import plotly.graph_objs as go


def weekly_data_fig2():
    # ----------------  Data ---------------- #
    # Fetch Data from DB
    url = "https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/raised_weekly/inc"
    url2 = "https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/closed_weekly/inc"

    raised1 = json.loads(urlopen(url).read())['items']
    closed = json.loads(urlopen(url2).read())['items']

    # Create Empty Output Dictionaries in format needed for Graph
    dict_raised = {'week': [], 'raised': []}
    dict_closed = {'week': [], 'closed': []}

    # Fill Dictionary With Data
    for element in raised1:
        dict_raised['week'].append(element['week'])
        dict_raised['raised'].append(element['count'])

    for element in closed:
        dict_closed['week'].append(element['week'])
        dict_closed['closed'].append(element['count'])

    # Turn dict to DF
    data_raised = pd.DataFrame.from_dict(dict_raised)
    data_closed = pd.DataFrame.from_dict(dict_closed)

    # ---------------- Figure ---------------- #
    fig = go.Figure()

    # Add Data Raised
    fig.add_trace(go.Scatter(
        x=data_raised.week,
        y=data_raised.raised,
        name='RAISED',
        marker_color='#7e969e',
        text=data_raised.raised
    ))

    # Add Data Closed
    fig.add_trace(go.Scatter(
        x=data_closed.week,
        y=data_closed.closed,
        name='CLOSED',
        marker_color='#2b363a',
        text=data_closed.closed
    ))

    # Stylings
    fig.update_layout(font_family="Helvetica Neue",
                      paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor='rgba(0,0,0,0)', yaxis_title="INCIDENTS",
                      xaxis_title="CALENDAR WEEK 2021",
                      margin=dict(l=20, r=20, t=20, b=80),
                      legend=dict(bgcolor="white", font=dict(family="Helvetica Neue", color="black")))
    return fig
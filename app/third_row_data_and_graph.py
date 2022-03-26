from urllib.request import urlopen
import plotly.express as px
import json
import pandas as pd


def get_inc_per_type(selected_month):
    # ----------------  Data ---------------- #
    # Fetch Data from DB
    url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/cause_raise/{selected_month}"
    response_inc_per_type = urlopen(url)
    inc_per_type = json.loads(response_inc_per_type.read())['items']

    # Create Lists to Pre-Store Data in
    type = []
    data = []
    for element in inc_per_type:
        type.append(element['incident_type'])
        data.append(element['data'])

    # Return Data as DF to use in Figure
    df_per_type = pd.DataFrame({'TYPE': type, 'INCIDENTS': data})
    return df_per_type


def inc_type(data):
    # ----------------  Figure ---------------- #
    # Add Data
    fig_inc = px.bar(
        data, x="TYPE", y="INCIDENTS",
        barmode="group", text_auto=True)
    # Stylings
    fig_inc = fig_inc.update_layout(
        showlegend=False, font_family="Helvetica Neue",
        margin=dict(l=20, r=20, t=20, b=80),
        paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor='rgba(0,0,0,0)')
    fig_inc.update_traces(marker_color='#BAC6C9')

    return fig_inc
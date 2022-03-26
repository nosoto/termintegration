import plotly.express as px
from urllib.request import urlopen
import json
import pandas as pd


# ---------------------------------------------------- DATA ---------------------------------------------------- #
def get_data_per_month(selected_month, status):
    if status == 'raised':
        url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/raised_in_month/{selected_month}"
        url2 = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/raised_in_month_all/{selected_month}"
    elif status == 'closed':
        url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/closed_in_month_prio/{selected_month}"
        url2 = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/closed_in_month_all/{selected_month}"
    elif status == 'backlog':
        url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/open_in_month_prio/{selected_month}"
        url2 = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/all_open_in_month/{selected_month}"

    # Fetch Data: per Priority
    per_prio = json.loads(urlopen(url).read())['items']
    PRIORITY = []
    data = []
    for element in per_prio:
        PRIORITY.append(element['priority'].upper())
        data.append(element['count(*)'])

    df_prio = pd.DataFrame({'PRIORITY': PRIORITY, 'INCIDENTS': data})

    # Fetch Data For All
    count_incidents = json.loads(urlopen(url2).read())['items']

    return df_prio, count_incidents[0]['count(*)']


# ---------------------------------------------------- FIGURE ---------------------------------------------------- #
def define_pie(data):
    fig_raised_prio = px.bar(data, x="PRIORITY", y="INCIDENTS", barmode='group', text_auto=True)
    fig_raised_prio.update_layout(showlegend=False, font_family="Helvetica Neue",
                                  paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor='rgba(0,0,0,0)',
                                  margin=dict(l=60, r=20, t=20, b=80))
    fig_raised_prio.update_traces(marker_color='#BAC6C9')
    fig_raised_prio = fig_raised_prio
    return fig_raised_prio




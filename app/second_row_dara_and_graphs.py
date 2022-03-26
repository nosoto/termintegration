from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


def get_slas(selected_month):
    # ----------------  Data Count for Percentages ---------------- #
    # Fetch Data
    url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/closed_in_month_prio/{selected_month}"
    closed_all = json.loads(urlopen(url).read())['items']
    # Create Empty Dictionaries to enter data to
    df_all = {}
    # Fill Dictionary with data
    for group in closed_all:
        df_all[group['priority']] = group['count(*)']

    # ----------------  Data per Priority ---------------- #
    # Fetch Data
    url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/slas_met/{selected_month}"
    raised = json.loads(urlopen(url).read())['items']

    # Create Empty Dictionaries to enter data to so that MTTR = 0 if no data avilable
    dict_sla_met = {'Baja': 0, 'Media': 0, 'Alta': 0, 'Crítica': 0}
    dict_sla_not_met = {'Baja': 0, 'Media': 0, 'Alta': 0, 'Crítica': 0}
    dict_mttr_sla_met = {'Baja': 0, 'Media': 0, 'Alta': 0, 'Crítica': 0}
    dict_mttr_sla_not_met = {'Baja': 0, 'Media': 0, 'Alta': 0, 'Crítica': 0}

    # Fill Dictionaries with data
    for element in raised:
        # Sla Not Met --> hourly MTTR
        if element['sla'] == 0:
            dict_sla_not_met[element['priority']] = round((element['count(*)'] / df_all[element['priority']]*100), 2)
            dict_mttr_sla_not_met[element['priority']] = round((element['mttr'] / 60), 4)
        # Sla Met  --> hourly MTTR
        else:
            dict_sla_met[element['priority']] = round((element['count(*)'] / df_all[element['priority']]*100), 2)
            dict_mttr_sla_met[element['priority']] = round((element['mttr'] / 60), 4)

    return dict_sla_met, dict_sla_not_met, dict_mttr_sla_met, dict_mttr_sla_not_met


def sla_prio(dict_sla_met, dict_sla_not_met):
    # ----------------  Figure ---------------- #
    # Create Figure
    fig = go.Figure()

    # Add Data SLA Met
    fig.add_trace(go.Bar(
        x=[x.upper() for x in list(dict_sla_met.keys())],
        y=list(dict_sla_met.values()),
        name='MET',
        marker_color='#BAC6C9',
        text=list(dict_sla_met.values())
    ))

    # Add Data SLA Not Met
    fig.add_trace(go.Bar(
        x=[x.upper() for x in list(dict_sla_not_met.keys())],
        y=list(dict_sla_not_met.values()),
        name='NOT MET',
        marker_color='#7e969e',
        text=list(dict_sla_not_met.values()),
    ))

    # Styling
    fig.update_layout( barmode='stack',font_family="Helvetica Neue",
                      paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor='rgba(0,0,0,0)',
                       margin=dict(l=20, r=20, t=20, b=80),
                      legend=dict(bgcolor="white",
                                  font=dict(family="Helvetica Neue", color="black")))
    return fig

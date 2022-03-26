from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from app.stylings import *
from app.first_row_data_and_graphs import *
from app.second_row_dara_and_graphs import *
from app.third_row_data_and_graph import *
from app.forth_row_data_and_graph import *
from app.fifth_row_data_and_graph import *

# -------------------------------------------------------------- Import Stylings -------------------------------------------------------------- #
# Stylings for Dashboard
NAV, LOGO, ICON_GREEN, ICON_RED, MENUEBUTTON, GRID_1, GRID, GRID_BIG, GRID_BIG_BOTTOM, GRID_SMALL, GRID_CHILD_SMALL, GRID_CHILD, FOOTER, FOOTERP, CARD, CARD_SMALL, TITEL_GRAPH, GRAPH, DROP_DOWN = return_stylings()
# Icons
icon_green = "https://media.istockphoto.com/vectors/green-checkmark-vector-illustration-vector-id1133442802?k=20&m=1133442802&s=612x612&w=0&h=N3UvaUREpqMYVpOV7kUrQzgpVaCgddEi-LESGeAl_FI="
icon_red = "https://cdn.pixabay.com/photo/2012/04/26/19/45/cross-42928_1280.png"


# -------------------------------------------------------------- Create App -------------------------------------------------------------- #
def create_dash_application(flask_app):
    dash_app = Dash(server=flask_app, name="__name__", url_base_pathname='/dash/', assets_folder = '/app/static/assets')


    # --------------------------------- Define Layout: Navbar, 5 Rows, Footer --------------------------------- #
    dash_app.layout = html.Div(
        children=[
            # ------------------ Navigarion Bar ------------------ #
            html.Div(style = NAV, children=[
                # Iberia Logo
                html.Img(src="https://www.iberia.com/wcs/logos/iberia/logo-iberia.svg", style=LOGO),
                html.H1(children=""),
                # Log-Out Button
                html.A(children='LOG-OUT', href="/to_logout", style=MENUEBUTTON),
                # Drop Down Menue
                html.Div(style=DROP_DOWN, children=dcc.Dropdown(['APRIL', 'MARCH', 'FEBRUARY', 'JANUARY'], 'APRIL', id='select_month'))
            ]),
            # ------------------ First Row: Raised, Closed, Backlog ------------------ #
            html.Div(style=GRID_1, children=[
                # Raised Incidents
                html.Div(style=GRID_CHILD, children=[
                    html.Div(style=CARD, children=[
                        # Header
                        html.H3(id='titel_text_raised', style=TITEL_GRAPH),
                        # Counter
                        html.H3(id='total_raised', style=TITEL_GRAPH),
                        # Graph
                        html.Div(dcc.Graph(id='Incidents_Raised_Bar', config={'displayModeBar': False}),
                                 style=GRAPH)])]),
                # Closed Incidents
                html.Div(style=GRID_CHILD, children=[
                    html.Div(style=CARD, children=[
                        # Header
                        html.H3(id='titel_text_closed', style=TITEL_GRAPH),
                        # Counter
                        html.H3(id='total_closed', style=TITEL_GRAPH),
                        # Graph
                        html.Div(dcc.Graph(id='Incidents_Closed_Bar', config={'displayModeBar': False}),
                                 style=GRAPH)])]),
                # Bcklog Incidents
                html.Div(style=GRID_CHILD, children=[
                    html.Div(style=CARD, children=[
                        # Header
                        html.H3(id='titel_text_backlog', style=TITEL_GRAPH),
                        # Counter
                        html.H3(id='total_backlog', style=TITEL_GRAPH),
                        # Graph
                        html.Div(dcc.Graph(id='Incidents_Backlog_Bar', config={'displayModeBar': False}),
                                 style=GRAPH)])])
            ]),
            # ------------------ Second Row: SLAs ------------------ #
            html.Div(style=GRID, children=[
                # SLA MET NOT MET GRAPH
                html.Div(style=GRID_CHILD, children=[
                    html.Div(style=CARD, children=[
                        # Card Header
                        html.H3(id='titel_text_sla_met', style=TITEL_GRAPH),
                        # Card Graph
                        html.Div(dcc.Graph(id='sla_met', config={'displayModeBar': False}), style=GRAPH)])]),

                # MTTR CARDS
                html.Div(style=GRID_CHILD_SMALL, children=[
                    # Card for Prio Critica
                    html.Div(style=CARD_SMALL, children=[
                        # Card Header
                        html.H3(id='mttr_c', style=TITEL_GRAPH),
                        html.Div(style=GRID_SMALL, children=[
                            # mttr sla met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_green, style=ICON_GREEN),
                                html.H4(id='mttr_c_met', style=TITEL_GRAPH)]),
                            # mttr sla not met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_red, style=ICON_GREEN),
                                html.H4(id='mttr_c_n_met', style=TITEL_GRAPH)])
                        ])]),
                    # Card for Prio Alta
                    html.Div(style=CARD_SMALL, children=[
                        # Card Header
                        html.H3(id='mttr_a', style=TITEL_GRAPH),
                        html.Div(style=GRID_SMALL, children=[
                            # mttr sla met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_green, style=ICON_GREEN),
                                html.H4(id='mttr_a_met', style=TITEL_GRAPH)]),
                            # mttr sla not met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_red, style=ICON_GREEN),
                                html.H4(id='mttr_a_n_met', style=TITEL_GRAPH)])
                        ])]),
                    # Card for Prio Media
                    html.Div(style=CARD_SMALL, children=[
                        # Card Header
                        html.H3(id='mttr_m', style=TITEL_GRAPH),
                        html.Div(style=GRID_SMALL, children=[
                            # mttr sla met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_green, style=ICON_GREEN),
                                html.H4(id='mttr_m_met', style=TITEL_GRAPH)]),
                            # mttr sla not met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_red, style=ICON_GREEN),
                                html.H4(id='mttr_m_n_met', style=TITEL_GRAPH)])
                        ])]),
                    # Card for Prio Baja
                    html.Div(style=CARD_SMALL, children=[
                        # Card Header
                        html.H3(id='mttr_b', style=TITEL_GRAPH),
                        html.Div(style=GRID_SMALL, children=[
                            # mttr sla met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_green, style=ICON_GREEN),
                                html.H4(id='mttr_b_met', style=TITEL_GRAPH)]),
                            # mttr sla not met Icon + Counter
                            html.Div(style={'margin-top': 20}, children=[
                                html.Img(src=icon_red, style=ICON_GREEN),
                                html.H4(id='mttr_b_n_met', style=TITEL_GRAPH)])
                        ])])
                ])]),
            # ------------------ Third Row: Incident Types ------------------ #
            html.Div(style=GRID_BIG, children=[
                html.Div(style=GRID_CHILD, children=[
                html.Div(style=CARD, children=[
                    # Header
                    html.H3(id='titel_text_inc_types', style=TITEL_GRAPH),
                    # Graph
                    html.Div(dcc.Graph(id='inc_types', style=GRAPH))])
            ])]),

            # ------------------  Forth Row: Weekly Trend P1 ------------------ #
            html.Div(style=GRID_BIG, children=[
                html.Div(style=GRID_CHILD, children=[
                html.Div(style=CARD, children=[
                    # Header
                    html.H3(children='WEEKLY TREND P1 RAISED 2021', style=TITEL_GRAPH),
                    # Graph
                    html.Div(dcc.Graph(figure=weekly_data_p1(), style=GRAPH))])
            ])]),

            # ------------------ Fifth Row: Weekly Trend Raised and Closed ------------------#
            html.Div(style=GRID_BIG_BOTTOM, children=[
                html.Div(style=GRID_CHILD, children=[
                html.Div(style=CARD, children=[
                    # Header
                    html.H3(children='WEEKLY TREND RAISED AND CLOSED 2021', style=TITEL_GRAPH),
                    # Graph
                    html.Div(dcc.Graph(figure=weekly_data_fig2(), style=GRAPH))])
            ])]),

            # ------------------ Footer ------------------#
            html.Div(style=FOOTER, children=[
                html.P(children='Term Integration Project MCSBT 2021 NORA TOMBERS', style=FOOTERP)])
        ])

    # --------------------------------- Define Callback --------------------------------- #
    @dash_app.callback(
        ### --- Row 1 --- ###
        # Bargraph Raised Incidents in Month #
        Output('Incidents_Raised_Bar', 'figure'),  # Graph
        Output('total_raised', 'children'),  # Counter
        Output('titel_text_raised', 'children'),  # Header
        # Bargraph Closed Incidents in Month #
        Output('Incidents_Closed_Bar', 'figure'),  # Graph
        Output('total_closed', 'children'),  # Counter
        Output('titel_text_closed', 'children'),  # Header
        # Bargraph Backlog Incidents in Month #
        Output('Incidents_Backlog_Bar', 'figure'),  # Graph
        Output('total_backlog', 'children'),  # Counter
        Output('titel_text_backlog', 'children'),  # Header

        ### --- Row 2 --- ###
        # Stacked Graph Percentage SLA Met Not Met per Prio#
        Output('sla_met', 'figure'),  # Graph
        Output('titel_text_sla_met', 'children'),  # Header
        # MTTR Cards per Prio #
        Output('mttr_c', 'children'),  # Header
        Output('mttr_c_met', 'children'),  # mttr sla met
        Output('mttr_c_n_met', 'children'),  # mttr sla not met
        Output('mttr_a', 'children'),  # Header
        Output('mttr_a_met', 'children'),  # mttr sla met
        Output('mttr_a_n_met', 'children'),  # mttr sla not met
        Output('mttr_m', 'children'),  # Header
        Output('mttr_m_met', 'children'),  # mttr sla met
        Output('mttr_m_n_met', 'children'),  # mttr sla not met
        Output('mttr_b', 'children'),  # Header
        Output('mttr_b_met', 'children'),  # mttr sla met
        Output('mttr_b_n_met', 'children'),  # mttr sla not met

        ### --- Row 3 --- ###
        # Bar Graph Count Type of Incident #
        Output('inc_types', 'figure'),  # Graph
        Output('titel_text_inc_types', 'children'),  # Header

        ### --- Input --- ###
        Input('select_month', 'value'))  # Dropdown Menue
    # --------------------------------- Functions for Callback --------------------------------- #
    def callback_a(value):
        # Numerical Value for month to query database
        dict_month = {'APRIL': '202104', 'MARCH': '202103', 'FEBRUARY': '202102', 'JANUARY': '202101'}
        selected_month = dict_month[value]

        ### Row 1 Raised, Closed, Backlog###
        raised_per_prio, all_raised = get_data_per_month(selected_month, 'raised')  # Fetch Data Raised
        raised_prio_pie = define_pie(raised_per_prio)  # Create Graph
        text_total_raised = f'TOTAL RAISED IN {value}'  # Write Titel

        closed_per_prio, all_closed = get_data_per_month(selected_month, 'closed')  # Fetch Data Closed
        closed_prio_pie = define_pie(closed_per_prio)  # Create Graph
        text_total_closed = f'TOTAL CLOSED IN {value}'  # Write Titel

        backlog_per_prio, all_backlog = get_data_per_month(selected_month, 'backlog')  # Fetch Data Backlog
        backlog_prio_pie = define_pie(backlog_per_prio)  # Create Graph
        text_total_backlog = f'TOTAL BACKLOG IN {value}'  # Write Titel

        ### Row 2 SLA ###
        # Figure Percentage SLA Met Not Met #
        dict_sla_met, dict_sla_not_met, dict_mttr_sla_met, dict_mttr_sla_not_met = get_slas(
            selected_month)  # Fetch Data SLA MET
        prio_sla_met_fig = sla_prio(dict_sla_met, dict_sla_not_met)  # Create Graph
        text_sla_met = f'PERCENTAGE SLA MET FOR {value}'  # Write Titel
        # Mean Time to Resolution Cards #
        mttr_c = f'MTTR CRÍTICA {value}'  # Write Titel
        mttr_c_met = f"{round(dict_mttr_sla_met['Crítica'], 1)} H"  # Fetch Data SLA MET
        mttr_c_n_met = f"{round(dict_mttr_sla_not_met['Crítica'], 1)} H"  # Fetch Data SLA NOT MET
        mttr_a = f'MTTR ALTA {value}'  # Write Titel
        mttr_a_met = f"{round(dict_mttr_sla_met['Alta'], 1)} H"  # Fetch Data SLA MET
        mttr_a_n_met = f"{round(dict_mttr_sla_not_met['Alta'], 1)} H"  # Fetch Data SLA NOT MET
        mttr_m = f'MTTR MEDIA {value}'  # Write Titel
        mttr_m_met = f"{round(dict_mttr_sla_met['Media'] / 24, 1)} D"  # Fetch Data SLA MET
        mttr_m_n_met = f"{round(dict_mttr_sla_not_met['Media'] / 24, 1)} D"  # Fetch Data SLA NOT MET
        mttr_b = f'MTTR BAJA {value}'  # Write Titel
        mttr_b_met = f"{round(dict_mttr_sla_met['Baja'] / 24, 1)} D"  # Fetch Data SLA MET
        mttr_b_n_met = f"{round(dict_mttr_sla_not_met['Baja'] / 24, 1)} D"  # Fetch Data SLA NOT MET

        ### Row 3 Inc Types ###
        df_inc_per_type = get_inc_per_type(selected_month)  # Fetch Data Incident Types
        fig_inc_types = inc_type(df_inc_per_type)  # Create Graph
        titel_text_inc_types = f'TYPES OF CAUSED INCIDENTS IN {value}'  # Write Titel

        ### Return everything to the output  ###
        return raised_prio_pie, all_raised, text_total_raised, \
               closed_prio_pie, all_closed, text_total_closed, \
               backlog_prio_pie, all_backlog, text_total_backlog, \
               prio_sla_met_fig, text_sla_met, \
               mttr_c, mttr_c_met, mttr_c_n_met, mttr_a, mttr_a_met, mttr_a_n_met, mttr_m, mttr_m_met, mttr_m_n_met, mttr_b, mttr_b_met, mttr_b_n_met, \
               fig_inc_types, titel_text_inc_types

    # --------------------------------- Run App  --------------------------------- #
    if __name__ == '__main__':
        dash_app.run_server(debug=True)

    return dash_app



def return_stylings():

    NAV = {'right': 7, 'left': 5, 'top':5, "background": "#da162a", "border-radius": "25px", 'position': "fixed",
           'height': 80, 'zIndex': 990, 'opacity': 0.95, 'box-shadow': '0 10px 20px 0 rgba(0,0,0,0.2)'}
    LOGO = {'height': 80,'width': 152,'opacity': 1,'margin-top': 5,'margin-left': 50,"position": "absolute", 'zIndex': 999}
    ICON_GREEN = {'height':50, 'width':50, 'margin-left': 50}
    ICON_RED = {'height': 40, 'width': 40, 'margin-left': 50}
    MENUEBUTTON = {"font-family":"Helvetica Neue", 'float': 'right', 'left': 0, 'display': 'block', 'color': '#f2f2f2',
                   'text-align': 'center', 'padding': 0, 'text-decoration': 'none','transform': 'translate(1%, 50%)',
                    "margin-top":5, "margin-right": 25,"height": 10, 'zIndex': 999}
    GRID_1 = {'display': 'grid', 'gridTemplateColumns': "33% 33% 33%", 'grid-gap': 10, 'margin-top': 90, 'width': "95%", 'margin-left': '2.5%'}
    GRID = {'display': 'grid', 'gridTemplateColumns': "50% 50%", 'grid-gap': 10,  'width': "95%", 'margin-left': '2.5%'}
    GRID_BIG = {'display': 'grid', 'grid-gap': 10, 'width': "95%", 'margin-left': '2.5%'}
    GRID_BIG_BOTTOM = {'display': 'grid', 'grid-gap': 10, 'width': "95%", 'margin-left': '2.5%', 'margin-bottom': 40}
    GRID_CHILD_SMALL = {'display': 'grid', 'gridTemplateColumns': "48% 48%", 'grid-gap': 15, 'margin': "100 100 100 100", 'padding': 10}
    GRID_CHILD = {'padding': 10, 'margin': "100 100 100 100", 'gridTemplateColumns': "auto auto auto auto", 'zIndex': 10}
    GRID_SMALL = {'display': 'grid', 'gridTemplateColumns': "50% 50%"}
    FOOTER = {'position': 'fixed', 'background': '#da162a', 'color': 'white', 'height': 40, 'left': 5, 'bottom': 5,'right': 7,
              'zIndex': 998,  "border-radius": "15px", 'opacity': 0.95, 'box-shadow': '0 10px 20px 0 rgba(0,0,0,0.2)'}
    FOOTERP = {'font-size': 11, 'text-align': 'center','margin-top': 15, 'font-family': "Helvetica Neue",
              'font-weight': 200, 'zIndex': 999}
    CARD = {'box-shadow': '0 10px 20px 0 rgba(0,0,0,0.2)', 'transition': '0.3s', 'padding': '2px 16px',
            "border-radius": "25px",  'zIndex': 10, 'background': '#ffffff'}
    CARD_SMALL = {'box-shadow': '0 10px 20px 0 rgba(0,0,0,0.2)', 'transition': '0.3s', 'padding': '2px 16px',
                  "border-radius": "25px",  'zIndex': 10 , 'background': '#ffffff'}
    GRAPH = {'z-index': -10, 'display': 'none !important', "margin-top": -20}
    TITEL_GRAPH = {"font-family":"Helvetica Neue",'text-align': 'center','font-weight': 50}
    DROP_DOWN = {"font-family":"Helvetica Neue", 'font-weight': 50, 'float': 'right',
                 'margin-top': 0, "margin-right": 50 ,"border-radius": "150px", 'width': '15%',
                 'box-shadow': '0 10px 20px 0 rgba(0,0,0,0.2)'}

    return NAV, LOGO, ICON_GREEN,ICON_RED, MENUEBUTTON, GRID_1, GRID, GRID_BIG,GRID_BIG_BOTTOM, GRID_SMALL, GRID_CHILD_SMALL, GRID_CHILD, FOOTER, FOOTERP, CARD, CARD_SMALL, TITEL_GRAPH, GRAPH, DROP_DOWN
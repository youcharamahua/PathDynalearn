from pyexpat import model
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import json, os
import modules.style as Sty

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

class Config:
    model = "deepseek-reasoner"
    api_key = "your_apikey"
    base_url = "https://api.deepseek.com/v1"
    default_lang = "zh"
    LocalizationDict = {}

def load_localizations(localization_dir):
    LocalizationDict = {}
    for filename in os.listdir(localization_dir):
        if filename.endswith('.json'):
            lang_code = filename.split('.')[0]
            file_path = os.path.join(localization_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                LocalizationDict[lang_code] = json.load(f)
    return LocalizationDict

config = Config()
config.LocalizationDict = load_localizations('Localization')

# Language switch component
lang_switch = html.Div(
    [
        html.Hr(),
        html.Label(id="lang-label", style={"marginRight": "1rem"}),
        dcc.RadioItems(
            id="lang-radio",
            options=config.LocalizationDict[config.default_lang]["lang_options"],
            value=config.default_lang,
            labelStyle={"display": "inline-block", "marginRight": "1rem"},
            style={"marginBottom": "1rem"}
        ),
    ],
    style={"marginBottom": "1.5rem","position":"bottom"}
)

# Sidebar layout
sidebar = html.Div(
    [
        html.H2(id="sidebar-title", className="display-4", style={"fontWeight": "bold", "fontSize": "2rem", "color": "#343a40"}),
        html.Hr(),
        html.P(id="sidebar-desc", className="lead-en", style={"fontSize": "1.1rem", "color": "#495057", "wordBreak": "break-word", "whiteSpace": "normal"}),
        dbc.Nav(
            [
                dbc.NavLink(id="nav-home", href="/", active="exact"),
                dbc.NavLink(id="nav-page1", href="/page-1", active="exact"),
                dbc.NavLink(id="nav-page2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
            style={"marginTop": "2rem"}
        ),
        lang_switch
    ],
    style=Sty.SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=Sty.CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style={"background": "#e9ecef", "minHeight": "100vh"})

# Luage switch callback
@app.callback(
    [
        Output("sidebar-title", "children"),
        Output("sidebar-desc", "children"),
        Output("nav-home", "children"),
        Output("nav-page1", "children"),
        Output("nav-page2", "children"),
        Output("lang-label", "children"),
        Output("lang-radio", "options"),
    ],
    [Input("lang-radio", "value")]
)
def update_sidebar(lang):
    c = config.LocalizationDict[lang]
    return (
        c["title"], c["desc"],
        c["nav"][0], c["nav"][1], c["nav"][2],
        c["lang_label"], c["lang_options"]
    )

# 5. 页面内容多语言
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"), Input("lang-radio", "value")]
)
def render_page_content(pathname, lang):
    c = config.LocalizationDict[lang]
    if pathname == "/":
        return html.Div([
            html.H3(c["home_title"], style={"color": "#007bff"}),
            html.P(c["home_content"], style={"fontSize": "1.1rem"})
        ])
    elif pathname == "/page-1":
        return html.Div([
            html.H4(c["page1_title"], style={"color": "#17a2b8"}),
            html.P(c["page1_content"], style={"fontSize": "1.1rem"})
        ])
    elif pathname == "/page-2":
        return html.Div([
            html.H4(c["page2_title"], style={"color": "#28a745"}),
            html.P(c["page2_content"], style={"fontSize": "1.1rem"})
        ])
    return html.Div(
        [
            html.H1(c["notfound"], className="text-danger"),
            html.Hr(),
            html.P(c["notfound_content"].format(pathname)),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    
    app.run(port=8888)
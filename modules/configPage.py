import dash
from dash import dcc, html

def load_ConfigPage(LocalizationDict):
    return html.Div([
        # 你原有的标题和内容
        html.H3(LocalizationDict["home_title"], style={"color": "#007bff"}),
        html.P(LocalizationDict["home_content"]["content1"], style={"fontSize": "1.1rem"}),
        html.Hr(),
        # 语言模型选择部分
        html.Div([
            html.Label(LocalizationDict["home_content"]["LLM_select"], style={"fontWeight": "bold", "marginTop": "20px"}),
            dcc.Dropdown(
                id='model-select',
                options=[
                    {'label': 'DeepSeek-Reasoner', 'value': 'deepseek-reasoner'},
                    {'label': 'GPT-5', 'value': 'GPT-5'}
                ],
                value='deepseek-reasoner',  # 默认值
                style={"marginTop": "5px", "width": "300px"}
            )
        ]),
        html.Hr(),
        # API密钥输入部分
        html.Div([
            html.Label(LocalizationDict["home_content"]["API_key"], style={"fontWeight": "bold", "marginTop": "15px"})]),
        html.Div([
            dcc.Input(
                id='api-key',
                type='password',
                placeholder=LocalizationDict["home_content"]["API_key_prompt"],
                style={"marginTop": "5px", "width": "300px", "padding": "8px"}
            )
        ]),
        html.Hr(),
    
        # 学习难度选择部分
        html.Div([
            html.Label(LocalizationDict["home_content"]["difficulty"], 
                      style={"marginTop": "15px"}),
            dcc.Dropdown(
                id='difficulty-select',
                options=[
                    {'label': LocalizationDict["home_content"]["difficulty_select"][0], 'value': 'beginner'},
                    {'label': LocalizationDict["home_content"]["difficulty_select"][1], 'value': 'basic'},
                    {'label': LocalizationDict["home_content"]["difficulty_select"][2], 'value': 'advanced'},
                    {'label': LocalizationDict["home_content"]["difficulty_select"][3], 'value': 'expert'}
                ],
                value='basic',  # 默认值
                style={"marginTop": "5px", "width": "200px"}
            )
        ]),
        html.Hr(),
    
        # 学习天数输入部分
        html.Div([
            html.Label(LocalizationDict["home_content"]["days"],
                      style={"marginTop": "15px"}),
            html.P(LocalizationDict["home_content"]["days_prompt"], 
                  style={"color": "#999", "fontSize": "0.8rem", "marginTop": "2px"}),
            dcc.Input(
                id='study-days',
                type='number',
                min=7,
                max=14,
                value=14,  # 默认值
                placeholder='input...',
                style={"marginTop": "5px", "width": "150px", "padding": "8px"}
            )
        ])
    ], style={"padding": "20px"})
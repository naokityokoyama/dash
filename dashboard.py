import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dataset.dataset import Dataset
import plotly.express as px 
from dash.dependencies import Input, Output


dados = Dataset().df

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Eixo X"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": col, "value": col} for col in dados
                    ]
                 
                )
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Eixo Y"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": col, "value": col} for col in dados
                    ]
                    
                )
            ]
        )
      ],
    #body=True,
)

#grafico = dcc.Graph(figure=px.line(dados, x="precos", y="zona"))
grafico1 = dcc.Graph(id='grafico1', config={'displayModeBar':False}, style={'display':'inline-block'})
grafico2 = dcc.Graph(id='grafico2', config={'displayModeBar':False}, style={'display':'inline-block'})

grid1 = html.Div([
    dbc.Row(dbc.Col(dbc.Alert('Barra de inicio', color='primary')))
])

grid2 = html.Div([
    dbc.Row([
        dbc.Col(controls, md=4),
        dbc.Col(grafico1, md=8)
     ], align='center')
])

app.layout = html.Div([
    grid1, grid2
    ])

@app.callback(
    Output('grafico1', 'figure'),
    [Input('x-variable', 'value'),
     Input('y-variable', 'value')]
)

#filtro_df.columns[1]
def criando_grafico(x,y):
    #filtro_df = dados[[x,y]]
    filtro_df = dados.loc[:, [x, y]]
    fig = px.scatter(filtro_df,  x=x, y=y)
    fig.update_layout({'paper_bgcolor':'rgb(28,28,28)'})
    fig.update_layout(font=dict(
        family="Courier New, monospace",
        size=18,
        color="White"))
    return fig

#Disable option v
def filter_options(v):

    return [
        {"label": col, "value": col, "disabled": col == v}
        for col in dados.columns
    ]

# nao repetir X e Y (no dropbox)
app.callback(Output("x-variable", "options"), [Input("y-variable", "value")])(
    filter_options
)
app.callback(Output("y-variable", "options"), [Input("x-variable", "value")])(
    filter_options
)   

if __name__ == '__main__':
    app.run_server(port=8888)








import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', value='请输入些啥吧!', type='text', placeholder='请输入吧'),
    html.Div(id='output')
    ])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)

if __name__ == '__main__':
    app.run_server(debug=True)

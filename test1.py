import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# app.layout = html.Div('Dash 教程')
app.layout = html.Div(
	children=[
		html.H1(children='图表展示'),
		dcc.Graph(
			id = 'yiyi',
			figure = {
				'data':[
				{'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': '部门'},
				{'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': '机构'}
				],
				'layout':{
					'title':'图表标题'
				}

			}
			)
	]
	)




if __name__ == '__main__':
	app.run_server(debug=True)









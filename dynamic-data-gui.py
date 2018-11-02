import datetime
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html


stock = 'TSLA'

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader(stock, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)

# print(df.head())

app = dash.Dash()
app.layout = html.Div(
	children= [
		html.H1(children='Dash动态图表'),
		html.Div(children='''
			Dash: A web application framework for python.
			'''),
		dcc.Graph(
			id = 'yiyi-graph',
			figure={
				'data':[
					{'x': df.index, 'y': df.Close, 'type': 'line', 'name': '特斯拉股价'},
                	# {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
				],
				'layout': {
					'title':'Dash数据可视化'
				}
			}
			)
	]
	)

if __name__ == '__main__':
	app.run_server(debug=True)
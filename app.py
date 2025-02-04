import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd



########### Define your variables ######
myheading = "Best Craft Beers in DC"
mysubheading = "August 2019"
tabtitle = 'python rocks'
filename = 'dc-breweries.csv'
sourceurl = 'https://www.beeradvocate.com/beer/top-rated/us/dc/'
githublink = 'https://github.com/austinlasseter/dash-table-example'



########### Set up the data
df = pd.read_csv(filename)
mydata = [go.Bar(x=list(df['Beer Name'].value_counts().index),
                     y=list(df['Alcohol By Volume (ABV)']),
                     width=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],
                     marker=dict(color='#0FD58A'))]


mylayout = go.Layout(
    #autosize=False,
    #width=1300,
    #height=800,
    title = "ABV",
    xaxis = dict(title = 'Beer Name'),
    yaxis = dict(title = 'ABV')) #nticks=50
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),

    html.Br(),
    dcc.Graph(id='barchart',figure=myfigure),
    html.Br(),



    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Plotly Dash", href='https://plot.ly/python/pie-charts/')
    ]
)



############ Deploy
if __name__ == '__main__':
    app.run_server()

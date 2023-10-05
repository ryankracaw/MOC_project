from dash import Dash, html, dash_table, dcc, callback, Output, Input
from dash import dcc
import pandas as pd
import plotly.express as px

filepath = r'C:\Users\ryan.kracaw\Desktop\COPY_master_data.csv'
df = pd.read_csv(filepath)

grouped_df = df.groupby(['Region', 'Color']).size()
grouped_df = grouped_df.reset_index()
grouped_df = grouped_df.rename(columns = {0 : 'Count'})
new_df = pd.DataFrame({
    'Color' : ['Orange', 'Other', 'Red'],
    'App' : grouped_df.loc[grouped_df['Region'] == 'App']['Count'],
    'East Texas' : grouped_df.loc[grouped_df['Region'] == 'East Texas'].reset_index()['Count'],
    'Mid-Con' : grouped_df.loc[grouped_df['Region'] == 'Mid-Con'].reset_index()['Count'],
    'North Dakota' : grouped_df.loc[grouped_df['Region'] == 'North Dakota'].reset_index()['Count'],
    'Rockies' : grouped_df.loc[grouped_df['Region'] == 'Rockies'].reset_index()['Count'],
    'South Texas' : grouped_df.loc[grouped_df['Region'] == 'South Texas'].reset_index()['Count'],
    'West Texas' : grouped_df.loc[grouped_df['Region'] == 'West Texas'].reset_index()['Count']
})


app = Dash(__name__)

app.layout = html.Div([
    html.H1('MOC Visualizations'),
    html.Hr(),
    dcc.RadioItems(options=['App','East Texas', 'Mid-Con', 'North Dakota', 'Rockies', 'South Texas', 'West Texas'], value='App', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')

    #dcc.Graph(
    #    figure = px.bar(grouped_df, x='Color', y='Count', color='Region',barmode='group', title='New Total MOC Submissions by Region')
    #)
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.bar(new_df, x='Color', y=col_chosen, title=f'Total Number of MOC submission in {col_chosen}', width=1000, height=500)
    fig.update_yaxes(range = [0,4000])
    fig.update_traces(width=0.25)
    return fig

if __name__ == '__main__':
    app.run(debug=True)
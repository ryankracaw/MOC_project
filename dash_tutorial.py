from dash import Dash, html, dash_table, dcc, callback, Output, Input
from dash import dcc
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Read in the csv file
filepath = r'C:\Users\ryan.kracaw\Desktop\COPY_master_data.csv'
df = pd.read_csv(filepath)
df1 = pd.read_excel("Resources\MOC OCR Submissions Report.xlsx", 'Appalachia')

# Create dates Dataframe
dts = df1.iloc[0].dropna()
dts = dts.tolist()
clean_dates = []
for i in dts[:-1]:
    time_data = i
    format_data = "%Y-%m-%d"
    date1 = datetime.strftime(time_data, format_data)
    clean_dates.append(date1)
fixed_dates = clean_dates[:len(clean_dates) - 4]
dates_df = pd.DataFrame({'Date': fixed_dates})

# Set up date variables (3 months, 6 months, and 1 year)
three_month = date.today() + relativedelta(months=-3)
six_months = date.today() + relativedelta(months=-6)
year = date.today() + relativedelta(months=-12)

# Sort the main Dataframe into specific regions
app = df.loc[df['Region'] == 'App']
app_count = pd.merge(dates_df, app, how='left', on='Date')
etx = df.loc[df['Region'] == 'East Texas']
etx_count = pd.merge(dates_df, etx, how='left', on='Date')
okc = df.loc[df['Region'] == 'Mid-Con']
okc_count = pd.merge(dates_df, okc, how='left', on='Date')
nodo = df.loc[df['Region'] == 'North Dakota']
nodo_count = pd.merge(dates_df, nodo, how='left', on='Date')
rock = df.loc[df['Region'] == 'Rockies']
rock_count = pd.merge(dates_df, rock, how='left', on='Date')
stx = df.loc[df['Region'] == 'South Texas']
stx_count = pd.merge(dates_df, stx, how='left', on='Date')
wtx = df.loc[df['Region'] == 'West Texas']
wtx_count = pd.merge(dates_df, wtx, how='left', on='Date')

# Create Dataframe for all dates
app_all = app_count.groupby('Date')['Color'].count().reset_index(name="Appalachia")
etx_all = etx_count.groupby('Date')['Color'].count().reset_index(name="East Texas")
okc_all = okc_count.groupby('Date')['Color'].count().reset_index(name="Mid-Con")
nodo_all = nodo_count.groupby('Date')['Color'].count().reset_index(name="North Dakota")
rock_all = rock_count.groupby('Date')['Color'].count().reset_index(name="Rockies")
stx_all = stx_count.groupby('Date')['Color'].count().reset_index(name="South Texas")
wtx_all = wtx_count.groupby('Date')['Color'].count().reset_index(name="West Texas")

# Create Dataframe for 6 months
app6_df = app_count[(app_count['Date'] > str(six_months)) & (app_count['Date'] < str(date.today()))]
app6_df = app6_df.groupby('Date')['Color'].count().reset_index(name="Appalachia")
etx6_df = etx_count[(etx_count['Date'] > str(six_months)) & (etx_count['Date'] < str(date.today()))]
etx6_df = etx6_df.groupby('Date')['Color'].count().reset_index(name="East Texas")
okc6_df = okc_count[(okc_count['Date'] > str(six_months)) & (okc_count['Date'] < str(date.today()))]
okc6_df = okc6_df.groupby('Date')['Color'].count().reset_index(name="Mid-Con")
nodo6_df = nodo_count[(nodo_count['Date'] > str(six_months)) & (nodo_count['Date'] < str(date.today()))]
nodo6_df = nodo6_df.groupby('Date')['Color'].count().reset_index(name="North Dakota")
rock6_df = rock_count[(rock_count['Date'] > str(six_months)) & (rock_count['Date'] < str(date.today()))]
rock6_df = rock6_df.groupby('Date')['Color'].count().reset_index(name="Rockies")
stx6_df = stx_count[(stx_count['Date'] > str(six_months)) & (stx_count['Date'] < str(date.today()))]
stx6_df = stx6_df.groupby('Date')['Color'].count().reset_index(name="South Texas")
wtx6_df = wtx_count[(wtx_count['Date'] > str(six_months)) & (wtx_count['Date'] < str(date.today()))]
wtx6_df = wtx6_df.groupby('Date')['Color'].count().reset_index(name="West Texas")

# Create Dataframe for 3 months
app3_df = app_count[(app_count['Date'] > str(three_month)) & (app_count['Date'] < str(date.today()))]
app3_df = app3_df.groupby('Date')['Color'].count().reset_index(name="Appalachia")
etx3_df = etx_count[(etx_count['Date'] > str(three_month)) & (etx_count['Date'] < str(date.today()))]
etx3_df = etx3_df.groupby('Date')['Color'].count().reset_index(name="East Texas")
okc3_df = okc_count[(okc_count['Date'] > str(three_month)) & (okc_count['Date'] < str(date.today()))]
okc3_df = okc3_df.groupby('Date')['Color'].count().reset_index(name="Mid-Con")
nodo3_df = nodo_count[(nodo_count['Date'] > str(three_month)) & (nodo_count['Date'] < str(date.today()))]
nodo3_df = nodo3_df.groupby('Date')['Color'].count().reset_index(name="North Dakota")
rock3_df = rock_count[(rock_count['Date'] > str(three_month)) & (rock_count['Date'] < str(date.today()))]
rock3_df = rock3_df.groupby('Date')['Color'].count().reset_index(name="Rockies")
stx3_df = stx_count[(stx_count['Date'] > str(three_month)) & (stx_count['Date'] < str(date.today()))]
stx3_df = stx3_df.groupby('Date')['Color'].count().reset_index(name="South Texas")
wtx3_df = wtx_count[(wtx_count['Date'] > str(three_month)) & (wtx_count['Date'] < str(date.today()))]
wtx3_df = wtx3_df.groupby('Date')['Color'].count().reset_index(name="West Texas")

# Create Dataframe for 1 year
appyear_df = app_count[(app_count['Date'] > str(year)) & (app_count['Date'] < str(date.today()))]
appyear_df = appyear_df.groupby('Date')['Color'].count().reset_index(name="Appalachia")
etxyear_df = etx_count[(etx_count['Date'] > str(year)) & (etx_count['Date'] < str(date.today()))]
etxyear_df = etxyear_df.groupby('Date')['Color'].count().reset_index(name="East Texas")
okcyear_df = okc_count[(okc_count['Date'] > str(year)) & (okc_count['Date'] < str(date.today()))]
okcyear_df = okcyear_df.groupby('Date')['Color'].count().reset_index(name="Mid-Con")
nodoyear_df = nodo_count[(nodo_count['Date'] > str(year)) & (nodo_count['Date'] < str(date.today()))]
nodoyear_df = nodoyear_df.groupby('Date')['Color'].count().reset_index(name="North Dakota")
rockyear_df = rock_count[(rock_count['Date'] > str(year)) & (rock_count['Date'] < str(date.today()))]
rockyear_df = rockyear_df.groupby('Date')['Color'].count().reset_index(name="Rockies")
stxyear_df = stx_count[(stx_count['Date'] > str(year)) & (stx_count['Date'] < str(date.today()))]
stxyear_df = stxyear_df.groupby('Date')['Color'].count().reset_index(name="South Texas")
wtxyear_df = wtx_count[(wtx_count['Date'] > str(year)) & (wtx_count['Date'] < str(date.today()))]
wtxyear_df = wtxyear_df.groupby('Date')['Color'].count().reset_index(name="West Texas")

# Merge Dataframe into 1 main Dataframe
merged6_df = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        pd.merge(
                            app6_df, etx6_df, how='inner', on='Date'
                        ), okc6_df, how='inner', on='Date'
                    ), nodo6_df, how='inner', on='Date'
                ), rock6_df, how='inner', on='Date'
            ), stx6_df, how='inner', on='Date'
        ), wtx6_df, how='inner', on='Date'
)

merged3_df = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        pd.merge(
                            app3_df, etx3_df, how='inner', on='Date'
                        ), okc3_df, how='inner', on='Date'
                    ), nodo3_df, how='inner', on='Date'
                ), rock3_df, how='inner', on='Date'
            ), stx3_df, how='inner', on='Date'
        ), wtx3_df, how='inner', on='Date'
)

mergedyear = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        pd.merge(
                            appyear_df, etxyear_df, how='inner', on='Date'
                        ), okcyear_df, how='inner', on='Date'
                    ), nodoyear_df, how='inner', on='Date'
                ), rockyear_df, how='inner', on='Date'
            ), stxyear_df, how='inner', on='Date'
        ), wtxyear_df, how='inner', on='Date'
)

mergedall = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        pd.merge(
                            app_all, etx_all, how='inner', on='Date'
                        ), okc_all, how='inner', on='Date'
                    ), nodo_all, how='inner', on='Date'
                ), rock_all, how='inner', on='Date'
            ), stx_all, how='inner', on='Date'
        ), wtx_all, how='inner', on='Date'
)

merged6_df['North'] = merged6_df["Appalachia"] + merged6_df['Mid-Con'] + merged6_df['North Dakota'] + merged6_df['Rockies']
merged6_df['South'] = merged6_df['East Texas'] + merged6_df['West Texas'] + merged6_df['South Texas']
merged6_df['Total'] = merged6_df["Appalachia"] + merged6_df['Mid-Con'] + merged6_df['North Dakota'] + merged6_df['Rockies'] + merged6_df['East Texas'] + merged6_df['West Texas'] + merged6_df['South Texas']

merged3_df['North'] = merged3_df["Appalachia"] + merged3_df['Mid-Con'] + merged3_df['North Dakota'] + merged3_df['Rockies']
merged3_df['South'] = merged3_df['East Texas'] + merged3_df['West Texas'] + merged3_df['South Texas']
merged3_df['Total'] = merged3_df["Appalachia"] + merged3_df['Mid-Con'] + merged3_df['North Dakota'] + merged3_df['Rockies'] + merged3_df['East Texas'] + merged3_df['West Texas'] + merged3_df['South Texas']

mergedyear['North'] = mergedyear["Appalachia"] + mergedyear['Mid-Con'] + mergedyear['North Dakota'] + mergedyear['Rockies']
mergedyear['South'] = mergedyear['East Texas'] + mergedyear['West Texas'] + mergedyear['South Texas']
mergedyear['Total'] = mergedyear["Appalachia"] + mergedyear['Mid-Con'] + mergedyear['North Dakota'] + mergedyear['Rockies'] + mergedyear['East Texas'] + mergedyear['West Texas'] + mergedyear['South Texas']

mergedall['North'] = mergedall["Appalachia"] + mergedall['Mid-Con'] + mergedall['North Dakota'] + mergedall['Rockies']
mergedall['South'] = mergedall['East Texas'] + mergedall['West Texas'] + mergedall['South Texas']
mergedall['Total'] = mergedall["Appalachia"] + mergedall['Mid-Con'] + mergedall['North Dakota'] + mergedall['Rockies'] + mergedall['East Texas'] + mergedall['West Texas'] + mergedall['South Texas']

# Start Dash app
app = Dash(__name__)

# Create Dash Layout
app.layout = html.Div([
    html.Div(className='row', children= 'MOC Counts',
              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div(className='row', children=[
        dcc.RadioItems(options=['All', 'North/South', 'Appalachia', 'East Texas', 'Mid-Con', 'North Dakota', 'Rockies', 'South Texas', 'West Texas'],
                       value='All',
                       inline=True,
                       id='radio')
    ]),

    html.Hr(),

    html.Div(children=[
        dcc.Graph(id='display1', style={'display': 'inline-block'}),
        dcc.Graph(id='display2', style={'display': 'inline-block'})
    ]),

    dcc.Graph(id='display3'),
    dcc.Graph(id='display4')
])

@callback(
    Output('display1', 'figure'),
    Output('display2', 'figure'),
    Output('display3', 'figure'),
    Output('display4', 'figure'),
    Input('radio', 'value')
)
def test_function(function):
    if function == 'North/South':
        function = ['North', 'South', 'Total']
    if function == 'All':
        function = ['Appalachia', 'East Texas', 'Mid-Con', 'North Dakota', 'Rockies', 'South Texas', 'West Texas']
    fig1 = px.line(merged6_df, x='Date', y=function, markers=True, title='6 Month Count', height=500, width=930)
    fig2 = px.line(merged3_df, x='Date', y=function, markers=True, title='90 Days Count', height=500, width=930)
    fig3 = px.line(mergedyear, x='Date', y=function, markers=True, title='1 Year Count', render_mode="SVG")
    fig4 = px.line(mergedall, x='Date', y=function, markers=True, title='Max Counts',render_mode="SVG")
    return fig1, fig2, fig3, fig4


if __name__ == '__main__':
    app.run(debug=True)
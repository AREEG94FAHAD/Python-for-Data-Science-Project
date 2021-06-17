from numpy import NaN
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#
# TSLA = yf.Ticker("TSLA")
# tesla_data = pd.DataFrame(TSLA.history(period="max"))
# print(tesla_data)



# TSLA = yf.Ticker("TSLA")
# tesla_data = pd.DataFrame(TSLA.history(period="max"))
# tesla_data.reset_index(inplace=True)
# tesla_data.head(5)



url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
r = requests.get(url, allow_redirects=True).text
soup = BeautifulSoup(r, 'html.parser')

text = 'Tesla Quarterly Revenue'

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in soup.find_all('table',attrs={'class': 'historical_data_table table'}):
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
        for row in table.find_all("tr"):
            col = row.find_all("td")
            if len(col) == 2:
                date = col[0].text
                revenue = col[1].text.replace('$', '').replace(',', '')
                tesla_revenue = tesla_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)

# print(tesla_revenue)


#### get the index of empty row
i = tesla_revenue['Revenue'].loc[lambda x: x==''].index

# drop specific data 
deleteAllEmpty = tesla_revenue.drop(i)
# print(deleteAllEmpty)


# print(deleteAllEmpty.tail(5))

#

# make_graph(tesla_data,deleteAllEmpty,'Tesla')
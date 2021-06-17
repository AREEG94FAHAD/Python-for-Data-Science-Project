import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
import pandas as pd


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





GME = yf.Ticker("GME")
gme_data = pd.DataFrame(GME.history(period="max"))
gme_data.reset_index(inplace=True)
gme_data.head(5)





html_data = requests.get('https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue',allow_redirects=True).text
beautiful_soup = BeautifulSoup(html_data, 'html.parser')
text = 'GameStop Quarterly Revenue'
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for table in beautiful_soup.find_all('table',attrs={'class': 'historical_data_table table'}):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find_all("tr"):
            col = row.find_all("td")
            if len(col) == 2:
                date = col[0].text
                revenue = col[1].text.replace('$', '').replace(',', '')
                gme_revenue = gme_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)


i = gme_revenue['Revenue'].loc[lambda x: x==''].index
gme_revenue = gme_revenue.drop(i)
gme_revenue.tail(5)

# print(gme_revenue.tail(5))

make_graph(gme_data,gme_revenue,'GameStop')
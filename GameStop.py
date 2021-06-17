from numpy import NaN
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#//////////////////////////////////////////////////////////////////////////////////////////////////
# GME = yf.Ticker("GME")
# # gme_data = GME.history(period="max")
#  tesla_data = pd.DataFrame(GME.history(period="max"))
#//////////////////////////////////////////////////////////////////////////////////////////////////
# GME = yf.Ticker("TSLA")
# gme_data = pd.DataFrame(GME.history(period="max"))
# gme_data.reset_index(inplace=True)
# print(gme_data.head(5))
#/////////////////////////////////////////////////////////////////////////////////////////////////

url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
r = requests.get(url, allow_redirects=True).text
soup = BeautifulSoup(r, 'html.parser')

text = 'GameStop Quarterly Revenue'
GameStop_revenue = pd.DataFrame(columns=["Date", "Revenue"])


for table in soup.find_all('table',attrs={'class': 'historical_data_table table'}):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find_all("tr"):
            col = row.find_all("td")
            if len(col) == 2:
                date = col[0].text
                revenue = col[1].text.replace('$', '').replace(',', '')
                GameStop_revenue = GameStop_revenue.append({'Date':date, 'Revenue':revenue}, ignore_index=True)
print(GameStop_revenue.tail(5))

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
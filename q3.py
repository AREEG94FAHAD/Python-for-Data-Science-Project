import yfinance as yf
import pandas as pd

GME = yf.Ticker("GME")
gme_data = pd.DataFrame(GME.history(period="max"))
gme_data.reset_index(inplace=True)
gme_data.head(5)
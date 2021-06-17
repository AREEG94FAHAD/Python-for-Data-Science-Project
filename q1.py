import yfinance as yf
import pandas as pd

TSLA = yf.Ticker("TSLA")
tesla_data = pd.DataFrame(TSLA.history(period="max"))
tesla_data.reset_index(inplace=True)
tesla_data.head(5)

print(tesla_data.head(5))
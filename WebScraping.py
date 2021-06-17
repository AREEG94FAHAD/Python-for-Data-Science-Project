import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AMZN/history?p=AMZN'
r = requests.get(url, allow_redirects=True).text
soup = BeautifulSoup(r, 'html.parser')

# print(soup.head.title)

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])



for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    # print(col)
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

print(amazon_data.head(2))

open_value = amazon_data["Open"].where(amazon_data["Date"] == 'Jun 16, 2021')

print(open_value)
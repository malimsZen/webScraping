import pandas as pd
import json
import requests


url = "https://api.tradingeconomics.com/historical/country/united%20states/indicator/gdp?c=guest:guest&f=csv"

data = requests.get(url)

results = json.loads(data.text)
pd.DataFrame(results)

import pytrends
from pytrends.request import TrendReq
import pandas
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360, timeout=(5,10))

kw = input('Enter your keyword: ')
kw2 = [kw]

pytrends.build_payload(kw2, cat=0, timeframe='today 12-m', geo='US', gprop='')

df = pytrends.interest_over_time()
df = df.reset_index()
fig = px.line(df, x= 'date', y = kw2)
fig.show()

#df.to_csv(f'{kw}.csv')
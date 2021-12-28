import pandas as pd

df = pd.read_csv(r'C:\Users\cbattle\Documents\Projects\APIConnection\5674143645_2021-01-01-2021-10-30.csv')

df['metrics.cost_micros'] = df['metrics.cost_micros'].div(1000000)
df.drop(['customer.currency_code'], axis= 1)
df.to_csv('fixed.csv', index=False)
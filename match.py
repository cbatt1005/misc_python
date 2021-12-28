import pandas as pd

df = r'C:\Users\cbattle\Documents\Projects\APIConnection-1\5674143645_2021-10-01-2021-10-03.csv'

df = pd.read_csv(df)
df = df.groupby(['customer.descriptive_name']).size().reset_index(name= 'count')
df.to_csv('advcount.csv')

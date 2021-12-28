import pandas as pd

df1 = pd.read_csv('advcount.csv')
df2 = pd.read_csv('gaimp.csv')

comp = df2['Account Name'].isin(df1['customer.descriptive_name']).value_counts()

comp.to_csv('compareddf.csv')
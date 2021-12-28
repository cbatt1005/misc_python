import pandas as pd
import sqlalchemy
import psycopg2

print('Starting...')

db1 = sqlalchemy.create_engine("postgresql+psycopg2://radar:RADaR2019!@true-media.cxni7m8twpeg.us-east-2.rds.amazonaws.com/npiregistry")
db2 = sqlalchemy.create_engine("postgresql+psycopg2://radar:RADaR2019!@true-media.cxni7m8twpeg.us-east-2.rds.amazonaws.com/staticdb")

print('Copying table...')

query = '''SELECT * FROM public.facebook_data'''
df = pd.read_sql(query, db1)
df.to_sql('facebook_data', db2, schema= 'public', index= False, if_exists='replace')

print('(1) facebook_data copied')
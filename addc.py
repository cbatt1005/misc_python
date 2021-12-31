import pandas as pd
import os

path = r'C:\Users\cbattle\Documents\EDITED_PO_OCT2021\RNDC'
files = os.listdir(path)

for file in files:
    df1 = pd.read_csv(path + '\\' + file)
    df1['filename'] = file
    df1.to_csv(f'{file}.csv', index= None, header= True)
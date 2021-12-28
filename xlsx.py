import pandas as pd
import os

dic = r'C:\Users\cbattle\Documents\EDITED_PO_OCT2021\RNDC'
for file in os.listdir(dic):
    
    fp = os.path.join(dic, file)
    if fp.endswith('.xlsx'):
        file = pd.read_excel(fp)
        file.to_csv(f'{fp}.csv',
        index= None,
        header= True)
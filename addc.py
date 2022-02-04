import pandas as pd
import os

#path = r'C:\Users\cbattle\Desktop\2021\JAN\btwi'

for path, currentDirectory, files in os.walk(r'\Users\cbattle\Desktop\2021\jul'):
    for file in files:
        if file.endswith('.csv'):
            fp= os.path.join(path, file)
            df1 = pd.read_csv(fp, encoding= 'latin-1', error_bad_lines=False, sep=',')
    #df1['new']= ''
    #df2 = pd.DataFrame({'Description':df1['Description'].iloc[::2].values, 'new':df1['Description'].iloc[1::2].values}, orient= 'index')
            df1['Order Name'] = file
            df1['Order Name'] = df1['Order Name'].str.replace(r'.csv','')
    #df1.drop('filename',1)
            df1.to_csv(f'{file}', index= None, header= True)    
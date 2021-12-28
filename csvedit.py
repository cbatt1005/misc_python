import os
import pandas as pd

dic = r'C:\Users\cbattle\Documents\Projects\misc_python\attachment'
for file in os.listdir(dic):
    
    fp = os.path.join(dic, file)
    if fp.endswith('.csv'):
        df = pd.read_csv(fp)
        #                    df = df[:18]
        df = df.drop(df.index[range(13)])
        
        df.to_csv(f'{fp}', index= False)



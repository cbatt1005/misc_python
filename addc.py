import pandas as pd
import os

path = r'C:\Users\Chris Breezy\Documents\projects\misc_python\csv'

for file in os.listdir(path):
    fp= os.path.join(path, file)
    df1 = pd.read_csv(fp)
    df1['filename'] = file
    df1.to_csv(rf'C:\Users\Chris Breezy\Documents\projects\misc_python\csv\{file}', index= None, header= True)
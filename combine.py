import os
import glob
import pandas as pd
os.chdir(r'C:\Users\cbattle\Documents\Projects\misc_python\gcmdatapull')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
import pdftables_api
import tabula as tb
import os

dic = r'C:\Users\cbattle\Documents\Projects\misc_python\attachment'

for file in os.listdir(dic):
    fp = os.path.join(dic, file)

    conversion = pdftables_api.Client('92npigigk6q6')
    conversion.csv(fp, f'{fp}')


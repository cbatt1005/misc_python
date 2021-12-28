import requests
from requests.auth import HTTPBasicAuth
import os


dic = r'C:\Users\cbattle\Documents\Projects\misc_python\attachment'
for file in os.listdir(dic):
    
    fp = os.path.join(dic, file)
    if fp.endswith('.pdf'):
        
        
        api_key = '455f2daca8fa3bdb281d520152ef8b817dc37096'
        endpoint = "https://sandbox.zamzar.com/v1/jobs"

        target_format = 'csv'
        file_content = {'source_file': open(fp, 'rb')}
        data_content = {'target_format': target_format}
        res = res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))

        job_id = 23276786
        file_id = 114290136
        api_key = '455f2daca8fa3bdb281d520152ef8b817dc37096'
        endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

        response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))

        try:
            with open(fp, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()

                        print ("File downloaded")

        except IOError:
            print ("Error")
        

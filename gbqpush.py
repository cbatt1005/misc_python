import pandas as pd
import pandas_gbq
import os
from google.cloud import bigquery
credential_path = r"C:\Users\cbattle\Downloads\fitvinewine-01-755c2c71118c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
inp = input('fOLDER NAME: ')
inp2 = input('input gbq table name: ')
file_path = rf'C:\Users\cbattle\Desktop\2021\JAN_CL\{inp}\combined_csv.csv'

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = f"fitvinewine-01.po.{inp2}"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
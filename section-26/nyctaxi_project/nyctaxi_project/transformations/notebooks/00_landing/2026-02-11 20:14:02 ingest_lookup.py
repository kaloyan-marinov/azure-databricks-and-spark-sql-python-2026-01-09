# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to download the `taxi_zone_lookup.csv` file into the `/Volumes/nyctaxi/00_landing/data_sources/` volume
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/00_landing/2026-01-17 16:40:45 load_taxi_zone_lookup`

# COMMAND ----------

import urllib.request
import os
import shutil

try:
    # Construct the URL for the relevant file
    url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

    # Open a connection and stream the remote file
    response = urllib.request.urlopen(url)

    # Define and create the local directory
    dir_path = '/Volumes/nyctaxi/00_landing/data_sources/lookup'
    os.makedirs(dir_path, exist_ok=True)

    # Define the full path for the downloaded file
    local_path = f"{dir_path}/taxi_zone_lookup.csv"

    # Save the streamed file to the local file in binary mode
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(response, f)
    
    dbutils.jobs.taskValues.set(
        key='continue_downstream',
        value='yes',
    )

    print('File successfully downloaded')

except Exception as e:
    dbutils.job.taskValues.set(
        key='continue_downstream',
        value='no',
    )

    print(f'File download failed: {str(e)}')
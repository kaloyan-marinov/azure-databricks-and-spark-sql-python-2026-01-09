# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to download the `taxi_zone_lookup.csv` file into the `/Volumes/nyctaxi/00_landing/data_sources/` volume
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/00_landing/2026-01-17 16:40:45 load_taxi_zone_lookup`

# COMMAND ----------

import os
import sys

print(f"{sys.path = }")

# COMMAND ----------

project_root = os.path.join(
    os.getcwd(),
    '..',
    '..',
    '..',
)
project_root = os.path.abspath(project_root)

if project_root not in sys.path:
    sys.path.append(project_root)

print(f"{sys.path = }")

# COMMAND ----------

from modules.data_loader.file_downloader import download_file

# COMMAND ----------

try:
    # Construct the URL for the relevant file
    url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

    # Define and create the local directory
    dir_path = '/Volumes/nyctaxi/00_landing/data_sources/lookup'

    # Define the full path for the downloaded file
    local_path = f"{dir_path}/taxi_zone_lookup.csv"

    # Download the file
    download_file(url, dir_path, local_path)

    dbutils.jobs.taskValues.set(
        key='continue_downstream',
        value='yes',
    )

    print('File successfully downloaded')

except Exception as e:
    dbutils.jobs.taskValues.set(
        key='continue_downstream',
        value='no',
    )

    print(f'File download failed: {str(e)}')
# Databricks notebook source
# Load the last 6 months of Yellow Taxi trip PARQUET files into the
# `nyctaxi.00_landing.data_sources` volume.

# COMMAND ----------

import os
import shutil
import urllib.request

# COMMAND ----------

dates_to_process = [
    '2024-12',
    '2025-01',
    '2025-02',
    '2025-03',
    '2025-04',
    '2025-05',
    # '2025-06',
]


for date_to_process in dates_to_process:
    dir_path = (
        f"/Volumes/nyctaxi/00_landing/data_sources" 
        f"/nyctaxi_yellow"
        f"/{date_to_process}"
    )
    os.makedirs(dir_path, exist_ok=True)


    filename = f'yellow_tripdata_{date_to_process}.parquet'

    local_path = os.path.join(
        dir_path,
        filename,
    )

    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{filename}"
    response = urllib.request.urlopen(url)

    with open(local_path, 'wb') as f:
        shutil.copyfileobj(response, f)

# COMMAND ----------


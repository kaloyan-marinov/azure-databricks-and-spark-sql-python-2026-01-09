# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to ingest the TLC Yellow Trip data
# MAGIC   for the period[/month] that is 2 months prior to the current date
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/00_landing/2026-01-17 16:26:00 backfill_historical_yellow_trips`

# COMMAND ----------

import os
import sys

project_root = os.path.join(
    os.getcwd(),
    '..',
    '..',
    '..',
)
project_root = os.path.abspath(project_root)

if project_root not in sys.path:
    sys.path.append(project_root)

from modules.data_loader.file_downloader import download_file
from modules.utils.date_utils import get_target_yyyymm

# COMMAND ----------

# Obtain the year-month for 2 months prior to the current month,
# in the yyyy-MM format.
date_to_process = get_target_yyyymm(months_ago=2)

# COMMAND ----------

dir_path = (
    f"/Volumes/nyctaxi/00_landing/data_sources" 
    f"/nyctaxi_yellow"
    f"/{date_to_process}"
)

filename = f'yellow_tripdata_{date_to_process}.parquet'

local_path = os.path.join(
    dir_path,
    filename,
)

try:
    # Check if the file already exists
    dbutils.fs.ls(local_path)

    # If the file exists,
    # signal that the pipeline for incremental processing should terminate.
    dbutils.jobs.taskValues.set(
        key='continue_downstream',
        value='no',
    )

except:
    try:
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{filename}"

        # Download the file
        # Create a local directory for the data from `date_to_process`
        download_file(url, dir_path, local_path)

        dbutils.jobs.taskValues.set(
            key='continue_downstream',
            value='yes',
        )

        print('File successfully donwloaded in current run')
    
    except Exception as e:
        # A likely reason for the following block to get executed would be
        # if the file isn't available in the TLC Trip Record Portal yet.
        dbutils.jobs.taskValues.set(
            key='continue_downstream',
            value='no',
        )

        print(f'File download failed: {str(e)}')
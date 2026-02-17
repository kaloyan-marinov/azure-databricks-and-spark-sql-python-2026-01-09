# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to process the TLC Yellow Trip raw data
# MAGIC   for the period[/month] that is 2 months prior to the current date
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/01_bronze/2026-01-17 16:52:09 yellow_trips_raw`

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

from modules.transformations.metadata import add_processed_timestamp
from modules.utils.date_utils import get_target_yyyymm

# COMMAND ----------

date_to_process = get_target_yyyymm(months_ago=2)

# COMMAND ----------

df = spark.read.load(
    f'/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/{date_to_process}',
    format='parquet',
)

# df.display()

# COMMAND ----------

# Add a column to capture when the data was processed.
df_1 = add_processed_timestamp(df)

# COMMAND ----------

# By default,
# the format for the to-be-created table will be DELTA
# and
# it will be saved as a managed DELTA TABLE.

df_1.write.saveAsTable(
    'nyctaxi.01_bronze.yellow_trips_raw',
    mode='append',
)

# COMMAND ----------

# spark.read.table('nyctaxi.01_bronze.yellow_trips_raw').display()

# COMMAND ----------


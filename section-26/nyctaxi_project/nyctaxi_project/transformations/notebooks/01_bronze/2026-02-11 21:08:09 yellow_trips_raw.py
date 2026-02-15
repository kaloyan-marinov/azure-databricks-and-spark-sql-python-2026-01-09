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
)
project_root = os.path.abspath(project_root)

if project_root not in sys.path:
    sys.path.append(project_root)

from modules.transformations.metadata import add_processed_timestamp

# COMMAND ----------

import datetime as dt

from dateutil.relativedelta import relativedelta


today = dt.date.today()
# Simulate the time when the lecturer recorded the video `134-set-up-for-part-2.md`.
today = dt.date(year=2025, month=8, day=17)

two_months_ago = today - relativedelta(months=2)

date_to_process = two_months_ago.strftime("%Y-%m")

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


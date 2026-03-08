# Databricks notebook source
import os
import sys

# Reach the project root
project_root = os.path.abspath(os.path.join(os.getcwd(), '../..'))

if project_root not in sys.path:
    sys.path.append(project_root)

from modules.utils.date_utils import get_month_start_n_months_ago
from pyspark.sql.functions import (
    date_format,
)

# COMMAND ----------

url_for_external_location = "abfss://nyctaxi-yellow@nyctaxistorage17.dfs.core.windows.net/"
target_folder = 'yellow_trips_export/'

catalog = 'nyctaxi'

source_schema = '02_silver'
source_table = 'yellow_trips_enriched'

target_schema = '04_export'
target_table = 'yellow_trips_export'

# COMMAND ----------

two_months_ago_start = get_month_start_n_months_ago(months_ago=2)

# COMMAND ----------

# Read the table
# and
# filter its contents appropriately.

df = spark.read.table(f'{catalog}.{source_schema}.{source_table}').filter(f"tpep_pickup_datetime > '{two_months_ago_start}'")

# Add a column called `year_month`.

df = df.withColumn(
    'year_month',
    date_format(
        'tpep_pickup_datetime',
        'yyyy-MM',
    ),
)

# COMMAND ----------

# Append the `DataFrame`'s contents to the specified «external table».

df.write.saveAsTable(
    f'{catalog}.{target_schema}.{target_table}',
    path=f'{url_for_external_location}{target_folder}',
    mode='append',
    format='json',
    partitionBy=[
        'vendor',
        'year_month',
    ],
)

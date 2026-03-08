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

two_months_ago_start = get_month_start_n_months_ago(months_ago=2)

# COMMAND ----------

# Read the table
# and
# filter its contents appropriately.

df = spark.read.table('nyctaxi.02_silver.yellow_trips_enriched').filter(f"tpep_pickup_datetime > '{two_months_ago_start}'")

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

df.write.\
    option('path', 'abfss://nyctaxi-yellow@nyctaxistorage17.dfs.core.windows.net/yellow_trips_export/').\
    format('json').\
    mode('append').\
    partitionBy('vendor', 'year_month').\
    saveAsTable('nyctaxi.04_export.yellow_trips_export')

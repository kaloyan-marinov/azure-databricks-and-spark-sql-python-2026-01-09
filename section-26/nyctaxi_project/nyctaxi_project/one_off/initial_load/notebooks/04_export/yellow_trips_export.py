# Databricks notebook source
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

# Add a column called `year_month`.

df = spark.read.table(f'{catalog}.{source_schema}.{source_table}')

df = df.withColumn(
    'year_month',
    date_format(
        'tpep_pickup_datetime',
        'yyyy-MM',
    ),
)

# COMMAND ----------

# Write the `DataFrame` to the specified «external table».

(
    df.write
    .option('path', f'{url_for_external_location}{target_folder}')
    .format('json')
    .mode('overwrite')
    .partitionBy('vendor', 'year_month')
    .saveAsTable(f'{catalog}.{target_schema}.{target_table}')
)

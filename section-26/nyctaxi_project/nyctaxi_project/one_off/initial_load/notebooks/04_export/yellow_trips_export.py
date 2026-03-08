# Databricks notebook source
from pyspark.sql.functions import (
    date_format,
)

# COMMAND ----------

# Add a column called `year_month`.

df = spark.read.table('nyctaxi.02_silver.yellow_trips_enriched')

df = df.withColumn(
    'year_month',
    date_format(
        'tpep_pickup_datetime',
        'yyyy-MM',
    ),
)

# COMMAND ----------

# Write the `DataFrame` to the specified «external table».

df.write.\
    option('path', 'abfss://nyctaxi-yellow@nyctaxistorage17.dfs.core.windows.net/yellow_trips_export/').\
    format('json').\
    mode('overwrite').\
    partitionBy('vendor', 'year_month').\
    saveAsTable('nyctaxi.04_export.yellow_trips_export')

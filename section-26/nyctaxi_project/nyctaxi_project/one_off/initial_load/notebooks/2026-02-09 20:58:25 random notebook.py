# Databricks notebook source
import pyspark.sql.functions as sf

df = (
    spark
    .read
    .table(
        'nyctaxi.02_silver.yellow_trips_cleansed',
    )
    .agg(
        sf.min('tpep_pickup_datetime'),
        sf.max('tpep_pickup_datetime'),
    )
)

# COMMAND ----------

df.display()

# COMMAND ----------

# fmt: off
'''
May is 3 months prior the current date at the time when the lecturer recorded the video `134-set-up-for-part-2.md`.

We are yet to process the data from 2 months ago (relative to the above-mentioned time).

W
'''
# fmt: on
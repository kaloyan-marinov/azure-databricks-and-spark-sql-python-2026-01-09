# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to read and append data
# MAGIC   only for the dates that fall in the month, which is 2 months prior to the current month
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/02_silver/2026-01-18 10:33:21 yellow_trips_cleansed`

# COMMAND ----------

from pyspark.sql.functions import (
    col,
    max,
    min,
    timestamp_diff,
    when,
)


# COMMAND ----------

import datetime as dt

from dateutil.relativedelta import relativedelta

today = dt.date.today()
# Simulate the time when the lecturer recorded the video `134-set-up-for-part-2.md`.
today = dt.date(year=2025, month=8, day=17)

# Get the 1st day of the current month
curr_month_start = today.replace(day=1)

# Get the 1st day of the month from 2 months ago
two_months_ago_start = curr_month_start - relativedelta(months=2)

# Get the 1st day of the month from 1 months ago
one_month_ago_start = curr_month_start - relativedelta(months=1)

# COMMAND ----------

df = spark.read.table('nyctaxi.01_bronze.yellow_trips_raw')

# COMMAND ----------

# df.display()

# COMMAND ----------

# Bearing in mind the raw data files, which were downloaded by the `backfill_historical_yellow_trips` notebook),
# we expect that
# all the values in `tpep_pickup_datetime` should be between 2025-01 and 2025-06.

df_0 = df.agg(
    min('tpep_pickup_datetime'),
    max('tpep_pickup_datetime'),
)

# df_0.display()

# COMMAND ----------

# Filter down to retain only those records,
# where `tpep_pickup_datetime` is during the month, which is 2 months prior to the current month.

df_1 = df.filter(
    f"""
    '{two_months_ago_start}' <= tpep_pickup_datetime
    AND
    tpep_pickup_datetime < '{one_month_ago_start}'
    """
)

# COMMAND ----------

df_2 = df_1.agg(
    min('tpep_pickup_datetime'),
    max('tpep_pickup_datetime'),
)

# df_2.display()

# COMMAND ----------

# Having applied some basic filtering,
# we go on to apply the following transformations:
#
#   (a) alias column names to use `snake_case`
#
#   (b) apply the mappings, which are described in `data_dictionary_trip_records_yellow.pdf`

df_3 = df_1.select(
    (
        when(
            col('VendorID') == 1, 'Creative Mobile Technologies, LLC'
        )
        .when(
            col('VendorID') == 2, 'Curb Mobility, LLC'
        )
        .when(
            col('VendorID') == 6, 'Myle Technologies Inc'
        )
        .when(
            col('VendorID') == 7, 'Helix'
        )
        .otherwise('Unknown')
    ).alias('vendor'),

    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',

    timestamp_diff(
        'MINUTE',
        df_1.tpep_pickup_datetime,
        df_1.tpep_dropoff_datetime,
    ).alias('trip_duration'),

    'passenger_count',
    'trip_distance',

    (
        when(
            col('RatecodeID') == 1, 'Standard Rate'
        )
        .when(
            col('RatecodeID') == 2, 'JFK'
        )
        .when(
            col('RatecodeID') == 3, 'Newark'
        )
        .when(
            col('RatecodeID') == 4, 'Nassau or Westchester'
        )
        .when(
            col('RatecodeID') == 5, 'Negotiated fare'
        )
        .when(
            col('RatecodeID') == 6, 'Group Ride'
        )
        .otherwise(
            'Unknown'
        )
    ).alias('rate_type'),

    'store_and_fwd_flag',

    col(
        'PULocationID',
    ).alias('pu_location_id'),
    col(
        'DOLocationID'
    ).alias('do_location_id'),
    
    (
        when(
            col('payment_type') == 0, 'Flex Fare trip'
        )
        .when(
            col('payment_type') == 1, 'Credit card'
        )
        .when(
            col('payment_type') == 2, 'Cash'
        )
        .when(
            col('payment_type') == 3, 'No charge'
        )
        .when(
            col('payment_type') == 4, 'Dispute'
        )
        .when(
            col('payment_type') == 6, 'Voided trip'
        )
        .otherwise(
            'Unknown'
        )
    ).alias('payment_type'),

    'fare_amount',
    'extra',
    'mta_tax',
    'tolls_amount',
    'improvement_surcharge',
    'total_amount',
    'congestion_surcharge',
    col(
        'Airport_fee'
    ).alias('airport_fee'),
    'cbd_congestion_fee',
    'processed_timestamp',
)

# COMMAND ----------

# df_3.display()

# COMMAND ----------

# For now, we specify `mode='overwrite'`
# (but we will make this _incremental_ in Part 2 of the project).

df_3.write.saveAsTable(
    'nyctaxi.02_silver.yellow_trips_cleansed',
    mode='append',
)

# COMMAND ----------

# spark.read.table('nyctaxi.02_silver.yellow_trips_cleansed').display()

# COMMAND ----------


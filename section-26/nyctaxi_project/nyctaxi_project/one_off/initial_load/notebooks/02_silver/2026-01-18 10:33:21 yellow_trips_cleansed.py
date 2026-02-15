# Databricks notebook source
from pyspark.sql.functions import (
    col,
    max,
    min,
    timestamp_diff,
    when,
)


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

# The min is `2007-12-05T18:45:00.000`, which is outside of the expected range.
# Motivated by that, let us go on to
# apply a filter that ensures that above-mentioned expectation is actually satisfied.

df_1 = df.filter(
    """
    tpep_pickup_datetime >= '2024-12-01'
    AND
    tpep_pickup_datetime < '2025-06-01'
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
    mode='overwrite',
)

# COMMAND ----------

# spark.read.table('nyctaxi.02_silver.yellow_trips_cleansed').display()

# COMMAND ----------


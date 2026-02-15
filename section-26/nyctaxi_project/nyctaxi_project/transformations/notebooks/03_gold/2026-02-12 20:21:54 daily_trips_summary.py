# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to process only the newly-added records
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/03_gold/2026-01-18 11:57:54 daily_trips_summary`

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

# COMMAND ----------

from pyspark.sql.functions import (
    count,
    max,
    min,
    avg,
    sum,
    round,
)

# COMMAND ----------

df = spark.read.table('nyctaxi.02_silver.yellow_trips_enriched')

df = df.filter(
    f"'{two_months_ago_start}' < tpep_pickup_datetime"
)
# TODO: (2026/02/12, 20:22 CET)
#       double-check if the preceding statement should replace the "<" with "<="

# COMMAND ----------

# df.display()

# COMMAND ----------

df_1 = (
    df
    .groupBy(
        (
            df.tpep_pickup_datetime
            .cast('date')
            .alias('pickup_date')
        )
    )
    .agg(
        count('*').alias('total_trips'),
        round(avg('passenger_count'), 1).alias('average_passengers'),
        round(avg('trip_distance'), 1).alias('average_distance'),
        round(avg('fare_amount'), 2).alias('average_fare_per_trip'),
        max('fare_amount').alias('max_fare'),
        min('fare_amount').alias('min_fare'),
        round(sum('total_amount'), 2).alias('total_revenue'),
    )
)

# COMMAND ----------

# The following statement demonstrates that
# the `min_fare` for `pickup_date = '2025-05-03'` was -328,
# so we should probably investigate these numbers
# (but the course instructor thinks that they are probably the result of refunds).

# df_1.display()

# COMMAND ----------

df_1.write.saveAsTable(
    'nyctaxi.03_gold.daily_trip_summary',
    mode='append',
)

# COMMAND ----------

# spark.read.table('nyctaxi.03_gold.daily_trip_summary').display()
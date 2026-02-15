# Databricks notebook source
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
    mode='overwrite',
)

# COMMAND ----------

# spark.read.table('nyctaxi.03_gold.daily_trip_summary').display()

# COMMAND ----------

'''
# 99-gold-layer-processing.md

So that's all of the tables processed for our «NYC Taxi Project».

In the next part of the project (later on in the course),
we'll

  (a) implement
  «slowly-changing dimensions of Type 2»
  and
  «incremental processing»,
  along with

  (b)
  automating the notebooks as «tasks» in a «Databricks job».
'''
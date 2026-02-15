# Databricks notebook source
import pyspark.sql.functions as sf

# COMMAND ----------

# 1. Which vendor makes the most revenue?

df_1_1 = spark.read.table('nyctaxi.02_silver.yellow_trips_enriched')

# df_1_1.display()

# COMMAND ----------

df_1_2 = (
    df_1_1
    .groupBy('vendor')
    .agg(
        sf.round(
            sf.sum('total_amount'),
            2,
        ).alias('total_revenue')
    )
    .orderBy(
        'total_revenue',
        ascending=False,
    )
)

df_1_2.display()

# COMMAND ----------

# 2. What is the most popular pickup borough?

df_2_1 = df_1_1

df_2_2 = (
    df_2_1
    .groupBy('pu_borough')
    .agg(
        sf.count('*').alias('number_of_trips')
    )
    .orderBy(
        'number_of_trips',
        ascending=False,
    )
)

df_2_2.display()

# COMMAND ----------

# 3. What is the most commont journey (borough to borough)?

df_3_1 = df_1_1

df_3_2 = (
    df_3_1
    .groupBy('pu_borough', 'do_borough')
    # .groupBy(
    #     concat('pu_borough', sf.lit(' -> '), 'do_borough').alias('journey')
    # )
    .agg(
        sf.count('*').alias('number_of_trips')
    )
    .orderBy(
        'number_of_trips',
        ascending=False,
    )
)

df_3_2.display()

# COMMAND ----------

# 4. Create a time series chart showing the number of trips and total revenue per day.

df_4_1 = spark.read.table('nyctaxi.03_gold.daily_trip_summary')

df_4_1.display()

# Click on the `+` button and then on `Visualization`.

# COMMAND ----------


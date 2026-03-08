# Databricks notebook source
import pyspark.sql.functions as fs

# COMMAND ----------

df_1 = (
    spark.read.table('nyctaxi.`01_bronze`.yellow_trips_raw')
    .groupBy(
        fs.date_format(
            'tpep_pickup_datetime',
            'yyyy-MM',
        ).alias('year_month')
    )
    .agg(
        fs.count('*').alias('total_records')
    )
    .orderBy('year_month')
)

# COMMAND ----------

# Note that
# the following will reveal:
# (a) the data for 2025/06 has not been processed
# (b) some anomalous records for that same month were present in the raw data
#     (e.g. the raw data for 2025/04 may contain some anomalous records for 2025/06)

df_1.display()

# COMMAND ----------

df_2 = (
    spark.read.table('nyctaxi.`02_silver`.yellow_trips_cleansed')
    .groupBy(
        fs.date_format(
            'tpep_pickup_datetime',
            'yyyy-MM',
        ).alias('year_month')
    )
    .agg(
        fs.count('*').alias('total_records')
    )
    .orderBy('year_month')
)

# COMMAND ----------

df_2.display()

# COMMAND ----------

df_3 = (
    spark.read.table('nyctaxi.`02_silver`.yellow_trips_enriched')
    .groupBy(
        fs.date_format(
            'tpep_pickup_datetime',
            'yyyy-MM',
        ).alias('year_month')
    )
    .agg(
        fs.count('*').alias('total_records')
    )
    .orderBy('year_month')
)

# COMMAND ----------

df_3.display()

# COMMAND ----------

df_4 = (
    spark.read.table('nyctaxi.`03_gold`.daily_trip_summary')
    .groupBy(
        fs.date_format(
            'pickup_date',
            'yyyy-MM',
        ).alias('year_month')
    )
    .agg(
        fs.sum('total_trips').alias('total_records')
    )
    .orderBy('year_month')
)

# COMMAND ----------

df_4.display()

# COMMAND ----------

df_5 = (
    spark.read.table('nyctaxi.`04_export`.yellow_trips_export')
    .groupBy('year_month')
    .agg(
        fs.count('*').alias('total_records')
    )
    .orderBy('year_month')
)

# COMMAND ----------

df_5.display()

# COMMAND ----------

# Demonstrate how «Slowly-Changing Dimensions Type 2» is implemented.

df_6 = spark.read.table('nyctaxi.`02_silver`.taxi_zone_lookup')

# COMMAND ----------

df_6.display()
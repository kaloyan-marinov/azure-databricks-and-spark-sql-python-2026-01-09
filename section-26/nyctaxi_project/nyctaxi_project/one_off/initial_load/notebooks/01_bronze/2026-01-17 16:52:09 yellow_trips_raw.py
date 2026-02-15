# Databricks notebook source
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

df = spark.read.load(
    '/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/*',
    format='parquet',
)

# df.display()

# COMMAND ----------

df_1 = df.withColumn(
    'processed_timestamp',
    current_timestamp(),
)

# COMMAND ----------

# By default,
# the format for the to-be-created table will be DELTA
# and
# it will be saved as a managed DELTA TABLE.

df_1.write.saveAsTable(
    'nyctaxi.01_bronze.yellow_trips_raw',
    mode='overwrite',
)

# COMMAND ----------

# spark.read.table('nyctaxi.01_bronze.yellow_trips_raw').display()

# COMMAND ----------


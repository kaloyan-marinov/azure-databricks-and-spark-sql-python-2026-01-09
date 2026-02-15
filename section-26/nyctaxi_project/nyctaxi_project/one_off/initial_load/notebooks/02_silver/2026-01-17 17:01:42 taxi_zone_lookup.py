# Databricks notebook source
from pyspark.sql.functions import (
    col,
    current_timestamp,
    lit,
)
from pyspark.sql.types import (
    IntegerType,
    TimestampType,
)

# COMMAND ----------

df = spark.read.load(
    '/Volumes/nyctaxi/00_landing/data_sources/lookup/taxi_zone_lookup.csv',
    format='csv',
    header=True,
)

# COMMAND ----------

# Each of the following statements demonstrates that
# all of the columns are of the `string` type.

# df.display()

df.dtypes

# COMMAND ----------

df_1 = df.select(
    col('LocationID').cast(IntegerType()).alias('location_id'),
    col('Borough').alias('borough'),
    col('Zone').alias('zone'),
    col('service_zone'),
    current_timestamp().alias('effective_date'),
    lit(None).cast(TimestampType()).alias('end_date'),
)

# COMMAND ----------

# The `effective_date` and `end_date` columns will allow us
# to implement "slowly-changing dimensions of Type 2"
# (which is something we'll discuss in Part 2 of the project).

# df_1.display()

# COMMAND ----------

df_1.write.saveAsTable(
    'nyctaxi.02_silver.taxi_zone_lookup',
    mode='overwrite',
)

# COMMAND ----------

# spark.read.table('nyctaxi.02_silver.taxi_zone_lookup').display()

# COMMAND ----------


# Databricks notebook source
from delta.tables import DeltaTable

# COMMAND ----------

# Update this so that the date is the start of the month that was 2 months prior to the current date
date_from = '2025-06-01'

condition = f"tpep_pickup_datetime >= {date_from}"

# COMMAND ----------

d_t = DeltaTable.forName(
    spark,
    "nyctaxi.`01_bronze`.yellow_trips_raw",
)

d_t.delete(condition)

# COMMAND ----------

d_t = DeltaTable.forName(
    spark,
    "nyctaxi.`02_silver`.yellow_trips_cleansed",
)

d_t.delete(condition)

# COMMAND ----------

d_t = DeltaTable.forName(
    spark,
    "nyctaxi.`02_silver`.yellow_trips_enriched",
)

dt_t.delete(condition)


# COMMAND ----------

d_t = DeltaTable.forName(
    spark,
    "nyctaxi.`03_gold`.daily_trip_summary",
)

dt.delete(f"pickup_date >= {date_from}")

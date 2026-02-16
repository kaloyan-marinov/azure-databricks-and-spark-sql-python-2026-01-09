# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to process only the newly-added records
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/02_silver/2026-01-18 11:37:00 yellow_trips_enriched`

# COMMAND ----------

import os
import sys

project_root = os.path.join(
    os.getcwd(),
    '..',
    '..',
)
project_root = os.path.abspath(project_root)

if project_root not in sys.path:
    sys.path.append(project_root)

from modules.utils.date_utils import get_month_start_n_months_ago

# COMMAND ----------

# Get the 1st day of the month from 2 months ago
two_months_ago_start = get_month_start_n_months_ago(months_ago=2)

# COMMAND ----------

# fmt: off
'''
df_trips = spark.read.table('nyctaxi.02_silver.yellow_trips_cleansed')

df_trips = df_trips.filter(
    f"'{two_months_ago_start}' < tpep_pickup_datetime"
)
# TODO: (2026/02/12, 20:18 CET)
#       double-check if the preceding statement should replace the "<" with "<="
'''
# fmt: on
df_trips = spark.read.table("nyctaxi.02_silver.yellow_trips_cleansed").filter(f"tpep_pickup_datetime > '{two_months_ago_start}'")

# COMMAND ----------

df_zones = spark.read.table('nyctaxi.02_silver.taxi_zone_lookup')

# COMMAND ----------

# df_trips.display()

# COMMAND ----------

# df_zones.display()

# COMMAND ----------

df_join_1 = (
    df_trips
    .join(
        df_zones,
        on=df_trips.pu_location_id == df_zones.location_id,
        how='left',
    )
    .select(
        df_trips.vendor,
        df_trips.tpep_pickup_datetime,
        df_trips.tpep_dropoff_datetime,
        df_trips.trip_duration,
        df_trips.passenger_count,
        df_trips.trip_distance,
        df_trips.rate_type,
        df_zones.borough.alias('pu_borough'),
        df_zones.zone.alias('pu_zone'),
        df_trips.do_location_id,
        df_trips.payment_type,
        df_trips.fare_amount,
        df_trips.extra,
        df_trips.mta_tax,
        df_trips.tolls_amount,
        df_trips.improvement_surcharge,
        df_trips.total_amount,
        df_trips.congestion_surcharge,
        df_trips.airport_fee,
        df_trips.cbd_congestion_fee,
        df_trips.processed_timestamp,
    )
)

# COMMAND ----------

# df_join_1.display()

# COMMAND ----------

df_join_final = (
    df_join_1
    .join(
        df_zones,
        on=df_join_1.do_location_id == df_zones.location_id,
        how='left',
    )
    .select(
        df_join_1.vendor,
        df_join_1.tpep_pickup_datetime,
        df_join_1.tpep_dropoff_datetime,
        df_trips.trip_duration,  # why doesn't the video lecture have `df_join_1.trip_duration` on this line?!
        df_join_1.passenger_count,
        df_join_1.trip_distance,
        df_join_1.rate_type,
        df_join_1.pu_borough,
        df_zones.borough.alias('do_borough'),
        df_join_1.pu_zone,
        df_zones.zone.alias('do_zone'),
        df_join_1.payment_type,
        df_join_1.fare_amount,
        df_join_1.extra,
        df_join_1.mta_tax,
        df_join_1.tolls_amount,
        df_join_1.improvement_surcharge,
        df_join_1.total_amount,
        df_join_1.congestion_surcharge,
        df_join_1.airport_fee,
        df_join_1.cbd_congestion_fee,
        df_join_1.processed_timestamp,
    )
)

# COMMAND ----------

# df_join_final.display()

# COMMAND ----------

df_join_final.write.saveAsTable(
    'nyctaxi.02_silver.yellow_trips_enriched',
    mode='append',
)

# COMMAND ----------

# spark.read.table('nyctaxi.02_silver.yellow_trips_enriched').display()

# COMMAND ----------


# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: raw ingestion of three delta streams

# COMMAND ----------

import dlt


# Common settings
CATALOG = "bridge_monitoring"

SCHEMA_00_LANDING = "00_landing"
VOLUME = "streaming"
_PARENT_PATH = f"/Volumes/{CATALOG}/{SCHEMA_00_LANDING}/{VOLUME}"

SCHEMA_01_BRONZE = "01_bronze"


@dlt.table(
    name=f"{SCHEMA_01_BRONZE}.bridge_temperature",
    comment="Raw temperature readings",
)
def bronze_bridge_temperature():
    return spark.readStream.format("delta").load(f"{_PARENT_PATH}/bridge_temperature")


@dlt.table(
    name=f"{SCHEMA_01_BRONZE}.bridge_vibration",
    comment="Raw vibration readings",
)
def bronze_bridge_vibration():
    return spark.readStream.format("delta").load(f"{_PARENT_PATH}/bridge_vibration")


@dlt.table(
    name=f"{SCHEMA_01_BRONZE}.bridge_tilt",
    comment="Raw tilt‐angle readings",
)
def bronze_bridge_tilt():
    return spark.readStream.format("delta").load(f"{_PARENT_PATH}/bridge_tilt")

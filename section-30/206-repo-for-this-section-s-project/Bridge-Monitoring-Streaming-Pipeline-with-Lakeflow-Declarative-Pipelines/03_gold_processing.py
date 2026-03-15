# Databricks notebook source

# COMMAND ----------

# Gold: compute aggregations of the silver-layer data records over 10-minute tumbling windows

import dlt
from pyspark.sql.functions import col, window, max, avg, round

# Common settings
SCHEMA_02_SILVER = "02_silver"
BRIDGE_TEMPERATURE = "bridge_temperature"
BRIDGE_VIBRATION = "bridge_vibration"
BRIDGE_TILT = "bridge_tilt"

WIDTH_OF_TIMESTAMP_WINDOW = "10 minutes"
THRESHOLD_OF_LATENESS = "2 minutes"

SCHEMA_03_GOLD = "03_gold"
BRIDGE_METRICS = "bridge_metrics"


@dlt.table(
    name=f"{SCHEMA_03_GOLD}.{BRIDGE_METRICS}",
    comment="10-min avg temperature, max vibration & max tilt per bridge with window start/end",
)
def bridge_metrics():
    # Read data streams from the preceding layer.
    stream_df_temp = dlt.read_stream(
        f"{SCHEMA_02_SILVER}.{BRIDGE_TEMPERATURE}"
    ).withWatermark(
        "event_time",
        THRESHOLD_OF_LATENESS,
    )
    stream_df_vib = dlt.read_stream(
        f"{SCHEMA_02_SILVER}.{BRIDGE_VIBRATION}"
    ).withWatermark(
        "event_time",
        THRESHOLD_OF_LATENESS,
    )
    stream_df_tilt = dlt.read_stream(f"{SCHEMA_02_SILVER}.{BRIDGE_TILT}").withWatermark(
        "event_time",
        THRESHOLD_OF_LATENESS,
    )

    # Perform time-based aggregations based on `(bridge_id, window_start, window_end)`.
    
    # In this aggregation, retain bridge metadata.
    temp_agg = (
        stream_df_temp.groupBy(
            window("event_time", WIDTH_OF_TIMESTAMP_WINDOW),
            col("bridge_id"),
            col("name"),
            col("location"),
        )
        .agg(avg("temperature").alias("avg_temperature"))
        .select(
            col("bridge_id"),
            col("window.start").alias("window_start"),
            col("window.end").alias("window_end"),
            col("avg_temperature"),
            col("name"),
            col("location"),
        )
    )

    vib_agg = (
        stream_df_vib.groupBy(
            window("event_time", WIDTH_OF_TIMESTAMP_WINDOW),
            col("bridge_id"),
        )
        .agg(max("vibration").alias("max_vibration"))
        .select(
            col("bridge_id"),
            col("window.start").alias("window_start"),
            col("window.end").alias("window_end"),
            col("max_vibration"),
        )
    )

    tilt_agg = (
        stream_df_tilt.groupBy(
            window("event_time", WIDTH_OF_TIMESTAMP_WINDOW),
            col("bridge_id"),
        )
        .agg(max("tilt_angle").alias("max_tilt_angle"))
        .select(
            col("bridge_id"),
            col("window.start").alias("window_start"),
            col("window.end").alias("window_end"),
            col("max_tilt_angle"),
        )
    )

    # Combine the streaming aggregates
    # by performing a stream-to-stream `JOIN` on `(bridge_id, window_start, window_end)`.
    # (All of those streaming aggregates use identical window boundaries and «watermarks»,
    # guaranteeing the `JOIN` is perfectly aligned and remains "append only".)
    return (
        temp_agg.alias("t")
        .join(
            vib_agg.alias("v"),
            on=["bridge_id", "window_start", "window_end"],
            how="inner",
        )
        .join(
            tilt_agg.alias("l"),
            on=["bridge_id", "window_start", "window_end"],
            how="inner",
        )
        .select(
            col("bridge_id"),
            col("name"),
            col("location"),
            col("window_start"),
            col("window_end"),
            round(
                col("avg_temperature"),
                2,
            ).alias("avg_temperature"),
            col("max_vibration"),
            col("max_tilt_angle"),
        )
    )

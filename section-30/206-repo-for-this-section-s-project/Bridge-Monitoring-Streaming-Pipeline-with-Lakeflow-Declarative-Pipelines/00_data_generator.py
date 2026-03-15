# Databricks notebook source

"""
This notebook can be run manually
(and independently of the DLT pipeline,
which constitutes a practical implementation of `section-30/204-2-solution-architecture.md`).

It continuously simulates 3 data streams from 3 IoT sensors:
temperature, vibration, and tilt.

Each data stream is written to the «managed volume» within the `00_landing` «schema».
"""

import datetime as dt
import random
import time


def generate_stream(
    path: str,
    column_name: str,
    low: float,
    high: float,
    device_count: int,
    batch_interval_s: int,
    latency_max_s: int,
):
    """
    Simulate a data stream from an IoT sensor.
    
    The emitted readings are appended to a «Delta Table» located at `path`.
    """

    while True:
        now = dt.datetime.now(dt.timezone.utc)
        data = []
        for device_id in range(1, device_count + 1):
            ts = now - dt.timedelta(
                seconds=random.uniform(
                    0,
                    latency_max_s,
                )
            )
            value = round(random.uniform(low, high), 4)
            # build a plain dict so we can infer a schema
            data.append(
                {
                    "device_id": device_id,
                    "event_time": ts,
                    column_name: value,
                }
            )

        df = spark.createDataFrame(data)

        df.write.format("delta").mode("append").save(path)

        time.sleep(batch_interval_s)


# COMMAND ----------

# Launch all three generators concurrently without a wrapper

from concurrent.futures import ThreadPoolExecutor

# Assume generate_stream is already defined above

# Common settings
device_count = 5
batch_interval_s = 60
latency_max_s = 60

# fmt: off
'''
(path, column_name, low, high)
'''
# fmt: on
streams = [
    (
        "/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature",
        "temperature",
        19,
        23,
    ),
    (
        "/Volumes/bridge_monitoring/00_landing/streaming/bridge_vibration",
        "vibration",
        0.005,
        0.05,
    ),
    (
        "/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt",
        "tilt_angle",
        -0.005,
        0.005,
    ),
]

# Start each infinite generator in its own thread
with ThreadPoolExecutor(max_workers=len(streams)) as executor:
    for path, column_name, low, high in streams:
        executor.submit(
            generate_stream,
            path,
            column_name,
            low,
            high,
            device_count,
            batch_interval_s,
            latency_max_s,
        )
    # Context manager will call shutdown(wait=True) here,
    executor.shutdown(wait=True)
    # and block forever because these tasks never return.

# COMMAND ----------

# fmt: off
'''
generate_stream(
                "/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature", 
                'temperature', 
                0, 
                20, 
                5, 
                60, 
                60
                )

generate_stream(
                "/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt", 
                'tilt', 
                0.005, 
                0.05, 
                5, 
                60, 
                60
                )

generate_stream(
                "/Volumes/bridge_monitoring/00_landing/streaming/bridge_vibration", 
                'vibration', 
                -0.005, 
                0.005, 
                5, 
                60, 
                60
                )
'''
# fmt: on

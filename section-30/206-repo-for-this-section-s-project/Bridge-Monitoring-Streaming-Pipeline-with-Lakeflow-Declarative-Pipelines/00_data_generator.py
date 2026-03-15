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


def simulate_data_stream(
    path: str,
    metric_measured_by_sensor: str,
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
        now = dt.datetime.now(tz=dt.timezone.utc)

        data_records = []
        for device_id in range(1, device_count + 1):
            delay_due_to_network_latency = dt.timedelta(
                seconds=random.uniform(
                    0,
                    latency_max_s,
                )
            )
            event_time = now - delay_due_to_network_latency

            sensor_reading = round(random.uniform(low, high), 4)

            # Build a `dict` (to make it possible to infer a schema).
            data_record = {
                "device_id": device_id,
                "event_time": event_time,
                metric_measured_by_sensor: sensor_reading,
            }

            data_records.append(data_record)

        df = spark.createDataFrame(data_record)
        df.write.format("delta").mode("append").save(path)

        time.sleep(batch_interval_s)


# COMMAND ----------

# Launch all three generators concurrently without a wrapper

from concurrent.futures import ThreadPoolExecutor

# Assume simulate_data_stream is already defined above

# Common settings
device_count = 5
batch_interval_s = 60
latency_max_s = 60

# fmt: off
'''
(path, metric_measured_by_sensor, low, high)
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
    for path, metric_measured_by_sensor, low, high in streams:
        executor.submit(
            simulate_data_stream,
            path,
            metric_measured_by_sensor,
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
simulate_data_stream(
                "/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature", 
                'temperature', 
                0, 
                20, 
                5, 
                60, 
                60
                )

simulate_data_stream(
                "/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt", 
                'tilt', 
                0.005, 
                0.05, 
                5, 
                60, 
                60
                )

simulate_data_stream(
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

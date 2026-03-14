# Databricks notebook source
import csv
import datetime as dt
import os
import random
import time
import uuid

# Target directory for your streaming source
catalog = 'streaming_demo'
schema = 'weather_stream'
volume = 'weather_stream_volume'
target_dir = f"/Volumes/{catalog}/{schema}/{volume}/source/live_weather"
os.makedirs(target_dir, exist_ok=True)

cities = ["London", "New York", "Tokyo", "Paris", "Sydney"]

# Define the column order
headers = ["event_id", "timestamp", "city", "temperature_c", "humidity_percent", "wind_speed_kmh"]

while True:
    # Simulate a weather reading.
    event_id = str(uuid.uuid4())
    timestamp = dt.datetime.now().isoformat()
    city = random.choice(cities)
    temperature_c = round(random.uniform(-5, 35), 1)
    humidity_percent = random.randint(30, 90)
    wind_speed_kmh = round(random.uniform(0, 40), 1)

    event = [
        event_id,
        timestamp,
        city,
        temperature_c,
        humidity_percent,
        wind_speed_kmh,
    ]

    # Write the simulated weather reading to a single-row CSV.
    # (Notice how a timestamp is used to construct a filename,
    # which is a safe format for files.)
    ts_filename = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{target_dir}/weather_{ts_filename}.csv"

    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(event)

    print(f"Wrote {file_path}: {event}")

    # Simulate a scenario,
    # in which weather readings are made/collected/emitted every 10 seconds.
    time.sleep(10)

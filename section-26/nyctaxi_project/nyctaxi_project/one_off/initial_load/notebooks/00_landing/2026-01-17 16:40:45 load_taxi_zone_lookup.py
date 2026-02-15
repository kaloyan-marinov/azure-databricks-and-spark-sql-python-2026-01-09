# Databricks notebook source
import os
import shutil
import urllib.request

# COMMAND ----------

dir_path = (
    "/Volumes/nyctaxi/00_landing/data_sources" 
    "/lookup"
)
os.makedirs(dir_path, exist_ok=True)


filename = f'taxi_zone_lookup.csv'

local_path = os.path.join(
    dir_path,
    filename,
)

url = f"https://d37ci6vzurychx.cloudfront.net/misc/{filename}"
response = urllib.request.urlopen(url)

with open(local_path, 'wb') as f:
    shutil.copyfileobj(response, f)

# COMMAND ----------


# 199-trigger-intervals.md



```python
# Databricks notebook source
# MAGIC %md
# MAGIC You can specify the trigger settings of a streaming query to define the timing of streaming data processing, whether the query is going to be executed as micro-batch query with a fixed batch interval or as a continuous processing query. Here are the different kinds of triggers that are supported.
# MAGIC
# MAGIC Trigger settings are applied to the **`writeStream`** part of your query, which controls how and when data is written to the sink.

# COMMAND ----------

# MAGIC %md
# MAGIC ### ProcessingTime trigger with 10-seconds micro-batch interval

# COMMAND ----------

catalog = 'streaming_demo'
schema = 'weather_stream'
volume = 'weather_stream_volume'

# COMMAND ----------

parent_dir_for_sink = f"/Volumes/{catalog}/{schema}/{volume}/sink"
sink_path = f"{parent_dir_for_sink}/live_weather"
checkpoint_location = f"{parent_dir_for_sink}/checkpoints/_live_weather"

(
    df.writeStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("checkpointLocation", checkpoint_location)
    .trigger(processingTime='10 seconds')
    .save(sink_path)
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Available-now trigger

# COMMAND ----------

parent_dir_for_sink = f"/Volumes/{catalog}/{schema}/{volume}/sink"
sink_path = f"{parent_dir_for_sink}/live_weather"
checkpoint_location = f"{parent_dir_for_sink}/checkpoints/_live_weather"

(
    df.writeStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("checkpointLocation", checkpoint_location)
    .trigger(availableNow=True)
    .save(sink_path)
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Continuous Trigger

# COMMAND ----------

parent_dir_for_sink = f"/Volumes/{catalog}/{schema}/{volume}/sink"
sink_path = f"{parent_dir_for_sink}/live_weather"
checkpoint_location = f"{parent_dir_for_sink}/checkpoints/_live_weather"

(
    df.writeStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("checkpointLocation", checkpoint_location)
    .trigger(continuous='1 second')
    .save(sink_path)
)
```

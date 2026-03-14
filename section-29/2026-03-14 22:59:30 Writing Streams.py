# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
# MAGIC - [Structured Streaming Concepts](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts)
# MAGIC - [Structured Streaming Checkpoints](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/checkpoints)

# COMMAND ----------

catalog = 'streaming_demo'
schema = 'weather_stream'
volume = 'weather_stream_volume'

# COMMAND ----------

parent_dir_for_source = f"/Volumes/{catalog}/{schema}/{volume}/source"
source_path = f"{parent_dir_for_source}/live_weather"
schema_location = f"{parent_dir_for_source}/schemas/_live_weather_schema"

df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_location)
    .load(source_path)
)

df.display()

# COMMAND ----------

parent_dir_for_sink = f"/Volumes/{catalog}/{schema}/{volume}/sink"
sink_path = f"{parent_dir_for_sink}/live_weather"
checkpoint_location = f"{parent_dir_for_sink}/checkpoints/_live_weather"

(
    df.writeStream
    .format("parquet")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_location)
    .option("path", sink_path)
    .start()
)

# COMMAND ----------

(
    spark.read
    .format("parquet")
    .load(sink_path)
    .display()
)

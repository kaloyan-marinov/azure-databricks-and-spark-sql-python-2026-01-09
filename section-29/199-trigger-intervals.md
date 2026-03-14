# 199-trigger-intervals.md



## Sources

- https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html#triggers

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/triggers

- https://learn.microsoft.com/en-us/azure/databricks/compute/serverless/limitations#streaming



## Introduction

The trigger settings of a «structured streaming query» define the timing of streaming data processing,
whether the query is going to be executed as a «micro-batch query» with a fixed batch interval
or as a «continuous processing query».

If no trigger setting is explicitly specified (which is the default),
the query will be executed in «micro-batch mode».



## Examples

If you want to adjust the fixed interval «micro-batch», then this actually demonstrates it here:

```python
catalog = 'streaming_demo'
schema = 'weather_stream'
volume = 'weather_stream_volume'


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
```

The following will process all of the available data but then it will stop on its own:

```python
(
    df.writeStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("checkpointLocation", checkpoint_location)
    .trigger(availableNow=True)
    .save(sink_path)
)
```

The following enables low-latency, real-time data processing
by continuously processing data as it arrives (rather than in «micro-batches»):

```python
(
    df.writeStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("checkpointLocation", checkpoint_location)
    .trigger(continuous='1 second')
    .save(sink_path)
)
```



## Important to note

A shorter interval gives you lower latency, but it increases the resource usage.

So it's a trade off.

You should tailor the processing time to balance the cost and performance, especially to avoid frequent checks for small or empty batches.

---

With `Serverless Compute`,
there is no support for default or time-based trigger intervals;
only Trigger.AvailableNow is supported.
That is why all demonstration so far in the current section used an `All-Purpose Compute Cluster`.

---

What that means is spark will start a long running task that continuously reads and processes data.

It then commits the progress every second and it will achieve a millisecond level latency.

So please keep in mind that continuous mode supports only simple transformations and append output mode.
It's best suited for real time applications like monitoring or fraud detection.

---

So when configuring your streaming sink, please choose the trigger mode that best fits your latency,
your resource requirements, and your use case.
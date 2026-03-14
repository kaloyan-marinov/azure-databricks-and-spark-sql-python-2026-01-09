# 195-micro-batch-size.md

## Sources

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/batch-size

## Introduction

Although «Apache Spark Structured Streaming» is referred to as "streaming",
it works based on «micro-batch» processing.

This means that at regular intervals, a batch of data is ingested.

This «micro-batch» architecture ensures high throughput and fault tolerance,
making it suitable for processing continuous data flows.

By default, there are limits on the input rate for «structured streaming queries».
This helps:
- maintain a consistent batch size and
- prevent large batches from causing spill and cascading micro-batch processing delays.

## How to set options

```python
df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.maxFilesPerTrigger", "100")
    .load(source_path)
)
```

```python
df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.maxBytesPerTrigger", "10g")
    .load(source_path)
)
```

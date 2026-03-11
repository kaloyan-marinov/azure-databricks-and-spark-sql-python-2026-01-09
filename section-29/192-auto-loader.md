# 192-auto-loader.md



## Sources

https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/



## Introduction

«Auto Loader» is a feature of «Apache Spark Structured Streaming»
that makes it easy to incrementally and efficiently process new data files
as they arrive in cloud object storage.
(It is designed for ingesting raw files.)

It provides a «Structured Streaming» «source» called `cloudFiles`.

Given an input directory path on the cloud file storage,
the `cloudFiles` «source» automatically processes new files as they arrive,
with the option of also processing existing files in that directory.

> So essentially:
> instead of having to manually
> (a) list files,
> (b) check what is new, and
> (c) manage «schema drift»,
> «Auto Loader» does all of that work for you without any additional setup.



«Auto Loader» supports:

- the various cloud object stores

- these file formats:

  - `JSON`

  - `CSV`

  - `XML`

  - `PARQUET`

  - `AVRO`

  - `ORC`

  - `TEXT`

  - `BINARYFILE`



## Example usage

```python
df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .load(directory_path)
)
```

(Similarly, there is a `spark.writeStream`;
but «Auto Loader» - as its name suggests - is only for reading data streams.)
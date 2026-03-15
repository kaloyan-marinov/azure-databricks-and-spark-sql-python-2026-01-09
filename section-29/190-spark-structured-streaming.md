# 190-spark-structured-streaming.md



## Source

https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts



## Introduction

In this section of the course, we're going to focus on «real-time data streaming».

[«Apache Spark Structured Streaming»](
  https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
) is an engine
that lets you read data streams and write data streams.



## A working definiton of a «data stream»

A data stream is a destination,
which new records are being continuously added to.
It is helpful to conceptualize a data stream as an "unbounded table"
in the sense of a table, which rows are being continuously appended to.

Examples of data streams can be:

- real-time stock prices

- social media feeds such as Twitter posts

- sensor readings from machines



## More details

«Apache Spark Structured Streaming» is a near-real-time processing engine
that offers «end-to-end fault tolerance» with «exactly-once processing guarantees».

- fault tolerance
  := 
  the engine is to recover from failures,
  and continue processing data without loss or corruption

- exactly-once processing guarantees
  :=
  the engine ensures that
  each data record is processed only once
  (and no duplicates are created)

Fundamentally, its stream-processing model is very similar to a batch-processing model.

(a) You express your computation on a data stream
    as a standard batch-like query (as on a static table), but
    
(b) Spark runs it as an incremental query
    on an "unbounded input table"
    =
    The engine performs the computation incrementally
    and
    continuously updates the result as new records get added to the data stream.



## Supported typed of data streams, which you can read from

- data files in cloud object storage

- messages buses and queues

- a «Delta Lake» table



## Supported types of «data sinks», which you can write to

A «data sink» is the target of a streaming write operation.

examples:

- messages buses and queues

- «Delta Lake» tables

- key-value databases

- cloud object storage

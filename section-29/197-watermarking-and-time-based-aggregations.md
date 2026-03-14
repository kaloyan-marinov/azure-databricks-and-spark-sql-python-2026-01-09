# 197-watermarking-and-time-based-aggregations.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/watermarks



## Introduction

This document concerns «stateful streaming operations».

«Watermarks» must be applied to «stateful streaming operations»
in order to avoid infinitely expanding the amount of data kept in state, which can:

- introduce memory issues, or

- increase processing latencies during long-running streaming operations.



## What is a «watermark»?

«Apache Spark Structured Streaming» has a mechanism for handling late-arriving data.
That mechanism boils down to specifying a threshold-of-lateness
when your code is processing updates for a given «state entity»;
that is called a «watermark».

Common examples of «state entities» include:

(a) Aggregations over a specified time window.

(b) Unique keys in a `JOIN` between two data streams.

When you declare a «watermark», you specify
a timestamp field and a threshold-of-lateness
on a streaming `DataFrame`.
As new data arrives, the state manager
tracks the most recent timestamp in the specified field
and
processes all records within the threshold-of-lateness.



```python
import pyspark.sql.functions as Fs


col_timestamp = 'event_timestamp'
threshold_of_lateness = '10 minutes'
duration = '5 minutes'


(
    df
    .withWathermark(col_timestamp, threshold_of_lateness)
    .groupBy(
        fs.window(col_timestamp, duration),
        'id',
    )
    .count()
)
```



## Further reading

https://www.databricks.com/blog/feature-deep-dive-watermarking-apache-spark-structured-streaming

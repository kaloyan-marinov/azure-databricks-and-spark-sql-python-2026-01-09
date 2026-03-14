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

«Apache Spark Structured Streaming» uses «watermarks» to control the threshold
for how long to continue processing updates for a given «state entity».

Common examples of «state entities» include:

(a) Aggregations over a time window.

(b) Unique keys in a `JOIN` between two data streams.

When you declare a «watermark», you specify
a timestamp field and a watermark threshold
on a streaming `DataFrame`.
As new data arrives, the state manager
tracks the most recent timestamp in the specified field
and
processes all records within the lateness threshold.

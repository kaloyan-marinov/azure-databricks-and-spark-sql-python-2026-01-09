# 198-writing-streams.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/checkpoints



## Introduction

Recall the definition of a «data sink».

It is just the destination of where a data stream gets written to.



## Checkpoint location

One thing that is required for streaming writes is a «checkpoint location».



«Checkpoints» and «write-ahead logs» work together to provide processing guarantees for «Apache Spark Structured Streaming» workloads.

The «checkpoint» tracks the information that identifies the query, including state information and processed records.

> Essentially, it is the process of
> saving the state and the progress of a streaming application
> to a reliable storage system.

- If the application crashes or is restarted,
  then Spark can use the «checkpoint» to resume
  from where it left off rather than starting over.

- If you delete the files in a «checkpoint» directory
  or
  change to a new «checkpoint» location,
  the next run of the query begins fresh.



Each query must have a its own «checkpoint» location.
(Multiple queries should never share the same «checkpoint» location.)

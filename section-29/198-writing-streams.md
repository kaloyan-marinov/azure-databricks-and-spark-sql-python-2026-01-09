# 198-writing-streams.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts

- https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/checkpoints



## Introduction

Recall the definition of a «data sink».

It is just the destination of where a data stream gets written to.



## Checkpoint location

One thing that is required for streaming writes is a «checkpoint location».



Checkpoints provide processing guarantees for structured streaming workloads.

The checkpoint tracks the information that identifies the query, including the state information and

the process records.

Essentially, it's the process of saving the state and the progress of a streaming application to a

reliable storage system.

If the application crashes or is restarted, then spark can use the checkpoint data to resume from where

it left off rather than starting over.

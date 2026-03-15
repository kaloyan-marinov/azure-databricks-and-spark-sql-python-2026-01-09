# 203-what-is-lakeflow-declarative-pipelines-aka-delta-live-tables.md



## Overview of some DLT basics

DLT provides a fully «declarative» API,
letting you define tables and transformations with simple decorators and SQL-like commands
(instead of writing «imperative» Spark streaming code).

It focuses on what needs to be achieved,
leaving the underlying system to determine the best way to execute the task.



## Under the hood

In simple words,
you declare your tables with Python or SQL decorators
and then,
<u>under the hood</u>, DLT automatically handles:

- incremental processing

  - For streaming tables,
    incremental processing is built by design

  - For «materialized views»,
    DLT provides "an incremental processing engine"

    to use it,
    you write your transformation logic with «batch semantics»,
    and then
    the engine will only process new data and changes in the data sources whenever possible

- automatic orchestration

  DLT figures out the dependency graph,
  and runs everything in the right order (in parallel wherever possible).

  If a task fails, it retries:
  - at the task level, then
  - the flow level, then
  - the whole pipeline.
  
  No extra retry code is required.

- data quality

  You embed your data-quality expectations directly alongside your transformations.

  Bad records are quarantined or rejected
  before they ever reach downstream tables

> With DLT,
> 
> You spend your time modeling your pipeline and business logic, and
>
> the framework takes care of reliability, monitoring, and performance optimizations for you.



## The core concepts of «Delta Live Tables»

A «flow»:

- is the foundational data-processing concept in DLT

- supports both «batch semantics» and «streaming semantics»

- reads data from a source,
  applies user-defined processing logic,
  and writes the result into a target

«Streaming tables»:

- are «Unity Catalog» tables that
  receive one or more streaming flows
  and
  continuously ingest new data

A «materialized view»:

- is a form of «Unity Catalog»-managed table

- is a «batch target»

- can have one or more materialized-view flows written into it

A «sink»:

- is a streaming target for DLT

- currently supports
  - «Delta Tables»,
  - Apache Kafka Topics, and
  - Azure Event Hubs topics

- can have one or more streaming flows written into it

«Pipelines»:

- tie it all together

  You declare your «flows», «streaming tables», «materialized views» and «sinks» in code;
  
  DLT automatically
  infers dependencies,
  orchestrates execution,
  handles retries,
  and scales infrastructure for you.
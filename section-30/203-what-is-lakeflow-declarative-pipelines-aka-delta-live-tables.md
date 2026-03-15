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
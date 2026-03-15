# 203-what-is-lakeflow-declarative-pipelines-aka-delta-live-tables.md



## Overview of some DLT basics

DLT provides a fully «declarative» API,
letting you define tables and transformations with simple decorators and SQL-like commands
(instead of writing «imperative» Spark streaming code).

- It focuses on what needs to be achieved,
  leaving the underlying system to determine the best way to execute the task.

- In simple words,
  you declare your tables with Python or SQL decorators
  and then,
  under the hood, DLT automatically handles incremental processing

  - For streaming tables,
    incremental processing is built by design

  - For «materialized views»,
    DLT provides "an incremental processing engine"

    to use it,
    you write your transformation logic with «batch semantics»,
    and then
    the engine will only process new data and changes in the data sources whenever possible
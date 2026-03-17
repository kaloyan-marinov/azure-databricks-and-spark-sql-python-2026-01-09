# 212-why-lakeflow-declarative-pipelines-only-runs-on-pipeline-clusters.md

The «Delta Live Tables» module is supported only on a special «pipeline-managed cluster».

It is not supported on:

- an interactive cluster

- a standard-jobs cluster

When you write declarative pipeline code (by using `import dlt`),
you are not just writing Spark code -
you are giving Databricks a declarative specification of a data pipeline.



A «pipeline-managed cluster» is not just about the compute;
it's the execution environment that gives Databricks the hooks it needs to:

- build the Directed Acyclic Graph

- manage the checkpoints

- guarantee reliability

- enforce expectations

- scale automatically



So, your DLT code can be run only by first building an «ETL pipeline».

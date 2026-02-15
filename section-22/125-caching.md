# 125-caching.md


The first time you read a file,
Spark pulls it from its origin, which is the data store,
and stores it in a nearby cache.
This can be
- in memory
- or on a local, solid-state drive in your executor.

On subsequent reads,
Spark skips the remote-fetch entirely,
and it serves it straight from the cache.

This can be thought of as
inserting a "pit stop" between your compute and the slow storage layer.
That can speed up reads of the same dataset.



On Databricks,
Spark workloads benefit from 2 complimentary caching mechanisms.

- Disk cache

- Spark cache (Spark's classic in-memory cache)

https://docs.databricks.com/aws/en/optimizations/disk-cache#disk-cache-vs-spark-cache



The recommendation from Databricks is to use the <u>disk cache</u>,
which is automatically enabled.



(
FYI:
In `All-Purpose Compute Cluster`s and `Job Compute Cluster`s (but not in `Serverless Compute` Environments),
it is possible to turn off <u>disk cache</u>
and instead use <u>Spark Cache</u>.
)

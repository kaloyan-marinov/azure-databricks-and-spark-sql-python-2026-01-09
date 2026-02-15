# 131-1-liquid-clustering.md



## Introduction

`Liquid Clustering` is a more recent performance optimization technique
that replaces table partitioning and `Z Ordering`.

It can be applied to Delta Files and Tables.

Both `Z Ordering` and `Liquid Clustering` aim to keep related rows together on disk,
but they work in different ways:
  - `Z Ordering` must be run periodically, whenever your data changes,
  to stay effective
  - `Liquid Clustering` does its work continuously in the background

## When to use liquid clustering

source: https://docs.databricks.com/aws/en/delta/clustering

Databricks recommends `Liquid Clustering` for all new tables,
including streaming tables and materialized views.

The following scenarios particularly benefit from `Liquid Clustering`:

  - Tables that are often filtered by high cardinality columns.

  - Tables that have skew in data distribution.

  - Tables that grow quickly and require maintenance and tuning effort.

  - Tables that have concurrent write requirements.

  - Tables that have access patterns that change over time.

  - Tables where a typical partition key could leave the table with too many or too few partitions.

## Important to know

Clustering is not compatible with table partitioning or `Z Ordering`.

Databricks recommends allowing the platform
to manage all layout and optimization operations for data in your table.

## How to create tables with `Liquid Clustering`

source: https://docs.databricks.com/aws/en/delta/clustering#create-tables-with-clustering

The Python API exposes a `clusterBy` method,
which you can use when you're writing your data as a table or as a file.

# Automatic `Liquid Clustering`

source: https://docs.databricks.com/aws/en/delta/clustering#automatic-liquid-clustering

There's also a feature called <u>Automatic `Liquid Clustering`</u>.

This feature allows Databricks
to intelligently choose clustering keys to optimize query performance.

source: https://docs.databricks.com/aws/en/delta/clustering#enable-or-disable-automatic-liquid-clustering

The Python API enables you to specify
```python
(
df.write
    .format("delta")
    .option(
        "clusterByAuto",
        "true",
    )
    .saveAsTable(...)
)
```

If you also use `Liquid Clustering` in addition to enabling this automatic feature,
then Databricks will use the specified columns as suggestions or hints.
(It won't necessarily pick those, but it will use them as suggestions.
Ultimately, Databricks will intelligently decide how to cluster your data.)

# What actually trigger the clustering

```sql
OPTIMIZE table_name;

OPTIMIZE delta.`{file_path}`;
```

When you call the `clusteBy` method
or
when you enable the `"clusterByAuto` option,
that tells Databricks _how_ to cluster your data.

It's actually running the `OPTIMIZE` command which performs the clustering.



If you have «predictive optimization» enabled,
then Databricks will automatically run the `OPTIMIZE` command in the background.
As per [this page](
    https://docs.databricks.com/aws/en/optimizations/predictive-optimization#check-po-enabled
):

> Predictive optimization is enabled by default
> if your account was created on or after November 11, 2024.
> Databricks began enabling existing accounts starting on May 7, 2025.
> This enablement is rolling out gradually and is expected to be completed by February 2026.
> If you're unsure if your account is already enabled,
> see [Check whether predictive optimization is enabled](https://docs.databricks.com/aws/en/optimizations/predictive-optimization#check-po-enabled).



`Liquid Clustering` is incremental,
meaning that `OPTIMIZE` only rewrites data as necessary to accommodate data that needs clustering.
In plain English, what that means is
`Liquid Clustering` tracks which files have already been optimized
and
each `OPTIMIZE` run will only re-write the files that have not been compacted before.
(This makes it much less resource-intensive than `Z Ordering`.)



# Demo

Enabling `Liquid Clustering` causes the output files to be smaller in number and larger in size;
additionally and crucially, inspecting the metadata within the `_delta_log` reveals how the data is grouped together:

```
{"add":{"path":"part-00000-ac9a07ef-8371-49a8-bd0d-b25fdf9f0c53.c000.snappy.parquet",
...
\"minValues\":{
    ...
    \"o_orderdate\":\"1996-04-21\",
    ...
},
\"maxValues\":{
    ...
    \"o_orderdate\":\"1997-01-21\",
    ...
    }
}
{"add":{"path":"part-00001-4716e1a1-6b8c-45e4-afeb-cb1f1d7c75d7.c000.snappy.parquet",
...
\"minValues\":{
    ...
    \"o_orderdate\":\"1995-07-07\",
    ...
},
\"maxValues\":{
    ...
    \"o_orderdate\":\"1996-04-20\",
    }
}



{"add":{"path":"part-00002-bd58e51b-d585-45a1-8532-8f95e91a1877.c000.snappy.parquet","partitionValues":{},"size":686327510,"modificationTime":1770581137000,"dataChange":true,"stats":"{\"numRecords\":17900340,\"minValues\":{\"o_orderkey\":5,\"o_custkey\":1,\"o_orderstatus\":\"F\",\"o_totalprice\":884.11,\"o_orderdate\":\"1994-06-19\",\"o_orderpriority\":\"1-URGENT\",\"o_clerk\":\"Clerk#000000001\",\"o_shippriority\":0,\"o_comment\":\" Tiresias above the fluffily unu\"},\"maxValues\":{\"o_orderkey\":30000000,\"o_custkey\":749999,\"o_orderstatus\":\"P\",\"o_totalprice\":565520.21,\"o_orderdate\":\"1995-07-06\",\"o_orderpriority\":\"5-LOW\",\"o_clerk\":\"Clerk#000005000\",\"o_shippriority\":0,\"o_comment\":\"zzle; ironic accounts affix slyl\"},\"nullCount\":{\"o_orderkey\":0,\"o_custkey\":0,\"o_orderstatus\":0,\"o_totalprice\":0,\"o_orderdate\":0,\"o_orderpriority\":0,\"o_clerk\":0,\"o_shippriority\":0,\"o_comment\":0},\"tightBounds\":true}","tags":{"MAX_INSERTION_TIME":"1770581134000002","INSERTION_TIME":"1770581134000002","LIQUID_METADATA_ID":"0aeab72d-9ff4-496a-8937-00d0ea391a06","MIN_INSERTION_TIME":"1770581134000002","OPTIMIZE_TARGET_SIZE":"268435456"},"baseRowId":26406120,"defaultRowCommitVersion":0,"clusteringProvider":"liquid_ai"}}
```

Specifically, the data records have been grouped in such a way that
those with `o_orderdate`s close to each other are in the same `PARQUET` file.



# Note

Even with «predictive optimization» enabled,
we can still run
```python
spark.sql(
    "OPTIMIZE delta.`/Volumes/population_metrics/landing/datasets/output_dataset/delta_lake/orders_with_LQ`"
)
```
manually
to ensure that any "straggler files" are optimized.

So it may still be a good idea to include this command
every time you insert records into your Delta Files.
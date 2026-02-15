# 130-Z-ordering.md



## Introduction

`Z Ordering` is a performance optimization technique.

It can be applied to `DELTA` Files and Tables
in order to co-locate related information (based on a specified column or columns)
in the same set of files on storage.

This co-locality is automatically used
by `DELTA LAKE`
on Databricks' <u>data-skipping</u> algorithms
to dramatically reduce the amount of data that needs to be read
(when executing queries that filter on the specified columns).

If you expect a column to be frequently used in query predicates
and if that column has a high cardinality
(= has a high number of distinct values, which might make it ineffective for partitioning),
then you should apply `Z Ordering` based on that column.

Recall that
statistics are collected for the first 32 columns of every `PARQUET` file,
so one of those columns should be used
when you perform a `Z Ordering` optimization.

The way `Z Ordering` works is that it
- compacts small files together
- and co-locates the data related to the specified columns.

You can specify more than 1 column,
but that will drastically reduce the effectiveness.
So you should optimize on 1 column, if possible.



## Visual illustration

Consider the following example:

```
# file 1
USA         330'000'000
Germany      80'000'000

# file 2
Thailand     70'000'000
Egypt       101'000'000

# file 3
Japan       126'000'000
Columbia     50'000'000

# file 4
Brazil      210'000'000
UK           67'000'000
```

If you want to filter `WHERE population > 100_000_000`,
Spark will scan all 4 files.



If you apply `Z Ordering` on the `population` column, it will

- move the data closer together based on `population` values,
  causing rows with similar population values to get placed in the same file

- and compacts the smaller files

```
# file 1
USA         330'000'000
Egypt       101'000'000
Japan       126'000'000
Brazil      210'000'000

# file 2
Germany      80'000'000
Thailand     70'000'000
Columbia     50'000'000
UK           67'000'000
```

Now, if we want to filter in the same way,
Spark will scan only 1 of the 2 files.



## The Syntax

```sql
OPTIMIZE
    catalog.schema.table
ZORDER BY
    (column_1[, ..., column_N])
;



OPTIMIZE
    delta.`{file_path}`
ZORDER BY
    (column_1[, ..., column_N])
;
```



## Closing remarks

(a) `Z Ordering` is a post-write optimization

  - you don't apply it
    when you first write the table or files

  - it is a separate tidy-up step
    which you run after having written the table or files

(b) `Z Ordering` needs to be applied regularly
    if new data is flowing in

  - you can implement it as a regular maintenance job

  - it could run
    once a week
    or
    every time there's an `INSERT` in your data

(c) the default file-compaction size is around 1 GB,
    but it can be changed via

  ```python
  spark.conf.set(
      "spark.databricks.delta.optimize.maxFileSize",
      "128mb",
  )
  ```



Last but not least,
we won't go into too much detail on `Z Ordering` and we'll end it here.
The reason for this is
because there's a new technique called `Liquid Clustering`,
which has replaced `Z Ordering`.

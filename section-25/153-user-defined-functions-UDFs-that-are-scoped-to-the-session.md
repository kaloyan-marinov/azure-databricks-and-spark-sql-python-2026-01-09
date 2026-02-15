# 153-user-defined-functions-UDFs-that-are-scoped-to-the-session.md



## Introduction

User-defined functions (UDFs) make it possible
to write your own custom functions (e.g. in Python),
which are difficult to express with built-in Apache Spark functions.

Databricks recommends UDFs for
- ad-hoc queries,
- manual data cleansing,
- exploratory data analysis,
- and operations on small to medium-sized datasets.
Common use cases for UDFs include
- data encryption,
- decryption,
- hashing,
- JSON parsing,
- and validation.

Use Apache Spark methods for
operations on very large datasets
and
any workloads that run regularly or continuously,
including ETL jobs and streaming operations.



## More details

https://learn.microsoft.com/en-us/azure/databricks/udf/



## Summary

Under the hood,
Spark treats a UDF as <u>a column expression</u>.

When a UDF is called within a `DataFrame.withColumn` or `DataFrame.select` method,
Spark will
_ship_ that UDF to the executors
and
apply it _row-by-row_ on the `DataFrame` partitions.

Spark wraps UDFs in its Catalyst Engine
so they can be part of the execution plan.



<u>Spark SQL functions are faster.</u>

- Python UDFs run _row-by-row_ in a separate Python process

- Python UDFs cannot be optimized by the Catalyst Engine,
  which is Spark's optimizer,
  so performance tuning such as predicate pushdown doesn't apply [to Python UDFs]

- there's also _serialization overhead_:

  - Spark itself is written in Scala and Java
    and
    it runs on a Java Virtual Machine

  - your Python UDF logic is written in Python
    and,
    therefore, it runs in a separate Python interpreter

  - this is the extra cost of constantly converting data
    between
    Spark's Java Virtual Machine
    and
    the Python process for every row
    (before Spark can continue with the rest of the `DataFrame` operations)



In general,
Python UDFs should only be used
when Spark SQL functionality doesn't suffice
(i.e. when there is no Spark SQL functionality that achieves your objective).

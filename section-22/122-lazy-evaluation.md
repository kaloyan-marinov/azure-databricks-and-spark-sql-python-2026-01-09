# 122-lazy-evaluation.md


<u>Lazy Evaluation</u> is a feature in Spark
which holds off on executing <u>transformations</u>
until an <u>action</u> is called.



This means that,
when you call a <u>transformation</u> on a `DataFrame`,
Spark doesn't immediately read data or run that operation -
instead, it records the <u>transformation</u> in a plan.



Only when you invoke an <u>action</u>
does Spark actually go out and
load data,
apply every <u>transformation</u> in one go,
and produce results.



```python
# Cell 1
# (Spark only builds up the execution plan
# but it does not run it.)
df = (
    spark
    .read.table("population_metrics.default.countries_consolidated")
    .groupBy("region")
    .sum("population")
)
```

```python
# Cell 2
# (Since the following is an <u>action</u>,
# this will cause Spark to run the execution plan.)
df.display()
```



In summary:

- <u>transformations</u> do not trigger the execution of the code

- only <u>actions</u> do



The way to distinguish between a <u>transformation</u> and an <u>action</u>:

- <u>transformations</u> will produce another `DataFrame` or a data object

- an <u>action</u> is a method on the `DataFrame` which
  returns a value or result,
  or writes data to an external storage system

  - `write` operation
  - `display` operation
  - `show` operation
  - return a count of the number of rows



Q: Why does Spark do <u>Lazy Evaluation</u>?

A: By waiting until an <u>action</u> to execute,
   Spark avoids unnecessary intermediate work;
   it can fuse multiple operations together for efficiency,
   and push predicates,
   and prune columns
   before any data even moves.

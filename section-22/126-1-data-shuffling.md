# 126-1-data-shuffling.md



<u>Data Shuffling</u> (or simply <u>Shuffling</u>) refers to the process
when data is moved around between your nodes or Executors - during query execution! -
causing additional time to your queries due to network I/O overhead.



## What causes data <u>shuffling</u>

"wide" transformations such as:

- `groupBy()`

- `join()`

- `orderBy()`

- `distinct()`



## What does NOT cause <u>shuffling</u>

"narrow" transformations such as:

- `filter()`



## Example 1:

- A transformation which doesn't trigger a <u>shuffle</u>.

- A "narrow" transformation.

- Each Executor can perform its task indepdently.

- `DataFrame.filter`

Imagine we have 3 Executors.
Reading in the data causes each Executor to hold 1 partition of the whole dataset.
The letters represent different values in a particular column.

```
data source ---     Executor 1
            |
            |       Red
            |       Yellow
            |       Green
            |       Black
            |
            |--     Executor 2
            |
            |       Red
            |       Red
            |       Green
            |       Black
            |
            |--     Executor 3
            |
            |       Yellow
            |       Red
            |       Yellow
            |       Green
            |       Black
```

If we try to `filter` out the records represented by `Red`,
then each Executor can _independently_ drops its `Red` records.
(No data needs to be move between the Executors.)



## Example 2:

- A transformation that causes a <u>shuffle</u>.

- `DataFrame.groupBy`

- First, each Executor can perform a local grouping on its own partition(s) of the loaded dataset.
  Then, a (global) <u>shuffle</u> needs to be triggered
  b/c other matching records were loaded by different Executors.

```
data source ---     Executor 1          Executor 1              Executor 1                          Executor 1
            |
            |       Red        -------- Red         (shuffle)   Red     (from Executor 1) --------  Red
            |       Yellow     -------- Yellow      (shuffle)   Red     (from Executor 2) __/
            |       Green      -------- Green       (shuffle)   Yellow  (from Executor 1) --------  Yellow
            |       Black      -------- Black       (shuffle)   Yellow  (from Executor 3) __/
            |
            |--     Executor 2          Executor 2              Executor 2                          Executor 2
            |
            |       Red        -------- Red         (shuffle)   Green   (from Executor 1) --\
            |       Red        __/                  (shuffle)   Green   (from Executor 2) --------  Green
            |       Green      -------- Green       (shuffle)   Green   (from Executor 3) __/
            |       Black      -------- Black
            |
            |--     Executor 3          Executor 3              Executor 3                          Executor 3
            |
            |       Yellow     -------- Yellow      (shuffle)   Black   (from Executor 1) --\
            |       Yellow     __/                  (shuffle)   Black   (from Executor 2) --------  Black
            |       Green      -------- Green       (shuffle)   Black   (from Executor 3) __/
            |       Black      -------- Black
```



## Example 3:

- A transformation that causes a <u>shuffle</u>.

- `DataFrame.join`

  - Without any hints, Spark will shuffle all partitions of both tables
    so that matching keys land on the same Executor
    (regardless of how many partitions each Executor held, to begin with).

  - However, if one table is small enough,
    Spark can <u>broadcast</u> it (:= cause it to be sent) to each Executor's memory,
    which will eliminate the need to <u>shuffle the data</u>.



## Summary

In many cases, <u>shuffling</u> is unavoidable.

So it is good to understand what causes it so you can mitigate it as much as possible.

  (a) use a single-node worker, or fewer, more powerful worker nodes

  (b) filter your data as much as possible
      (to reduce the amount of data that might need to be <u>shuffled</u>)

  (c) prune columns
      (that are unnecessary)

  (d) de-normalize your datasets
      (if the cause of a <u>shuffle</u> is due to `JOIN`s)

  (e) partition your data
      by the columns that trigger <u>shuffles</u> most frequently
      (so that related rows stay on the same Executor,
      avoiding unnecessary data movement)

One of the benefits of Adaptive Query Execution (AQE) is that
it can automatically perform a <u>broadcast `JOIN`</u>
(to prevent the need for <u>shuffling</u> during `JOIN`s).
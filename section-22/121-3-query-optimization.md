# 121-3-query-optimization.md

How Spark
takes the declarations in your DataFrame or SQL code
and
incrementally refines them into the fastest possible execution plan.


```
    query
    |
    |
    V
    unresolved logical plan     Metadata Catalog
    |
    |
    V
|-> logical plan                Metadata Catalog    (purely declarative description of what you want to compute)
|   |
|   |
|   V
|   optimized logical plan
|   |
|   |                           Catalyst Optimizer  (applies filters as early as possible; re-writes the plan to read the minimal data; and avoids redundant computations)
|   V
|   multiple physical plans     (each representing a different way to carry out your operations)
|   |
|   |                           Cost-Based Optimizer    (uses table and file statistics to estimate the costs and I/Os of the plans, and selects the one with the lowest expected resource footprint)
|   V
|   selected physical plan
|   |
|-- | ------------------------- query execution (the Tugsten Engine is Spark's high-performance engine that speeds up your jobs by keeping data in simple, tightly-packed formats in-memory and turning the operations into one streamlined routine)
    V
    result
```

Finally, as your `Job` finally runs,
Adaptive Query Execution (AQE)
collects real runtime statistics
(e.g. shuffle sizes, partition counts, task durations)
and then
feeds them back into <u>the execution pipeline</u>.
It is a runtime feature which
watches your query while it's running
and
makes automatic tweaks to keep things running smoothly.


More on the Catalyst Optimizer: it applies a series of rule-based re-writes,
- pushing down filters to the data source,
- pruning away unused columns,
- and folding columns.
(See `121-4-the-catalyst-optimizer.jpeg`.)

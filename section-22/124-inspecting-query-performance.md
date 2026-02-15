# 124-inspecting-query-performance.md



How to inspect performance of queries
when using `Serverless` compute or an `All-Purpose Compute Cluster`. 



## using `Serverless` compute

- Click on the cell that runs an <u>action</u>

- Click on `Show performance (...)`

- Click on the statement of interest

  (at the time of recording, the reported metrics are only available for `Serverless` compute)



If you click on "query profile",
the numbering may be confusing:
```
#1 Result Query Stage

#2 Limit

#3 Columnar to Row

#4 Grouping Aggregate

#5 Scan Table
```
b/c `#5` is actually the first operation that was performed.



Another place where you can check the performance of this query is
by clicking on `Query History` in the left sidebar.



# using an `All-Purpose Compute Cluster`

You will have to click on that cluster directly
and then go to the `Spark UI` tab.

# 111-overview-and-demo-of-lakeflow-jobs.md



The topic of this lecture is «Lakeflow Jobs».
They used to be called «Databricks Jobs».
The name might change again in the future,
so we'll try to refer to them simply as «Jobs».

A «Job» makes it possible to schedule and orchestrate «Tasks».

  - can create a workflow of «Tasks»
    (by creating a directed acyclic graph (DAG)),
    with each «Task» being a script or notebook

  - can schedule frequent, repeatable Jobs

  - can specify
    «Tasks»,
    their order or dependencies,
    and cluster settings



Navigate to `Jobs & Pipelines`.
Click on `Create`.



Each created `Job` has a unique `Job ID`.
For example:
```
Job ID
380885752234008
```

You can also select the `Performance optimized` options:

  - this only available when you're using `Serverless` compute

  - but please note that it's more expensive



Under `Schedules & Triggers`, we can `Add trigger`.

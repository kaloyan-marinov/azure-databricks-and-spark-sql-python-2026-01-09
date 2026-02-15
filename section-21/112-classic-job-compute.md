# 112-classic-job-compute.md



In the previous lecture,
we used `Serverless` compute for our Lakeflow Job.

In this lecture,
we'll configure a `Classic Job Compute` cluster.
Those are lightweight, ephemeral clusters
which

  - spin up on-demand to run `Task`s

  - run in isolation

  - are fully managed

  - only work for the purpose of a given `Job`



Select the Job, which we created in the previous lecture,
and
edit the `Compute` for each of its `Task`s.



Trigger the job
and
note the following entry under `Compute`:
    ```
    job-380885752234008-run-1003135680009780-classic_job_compute_f4
    ```



With a `Classic Job Compute` cluster,
what we can do (that we cannot do with `Serverless` compute)
is
to make Spark configurations
and
to set environment variables.



A special note:

  - under `Compute`,
    you're also able to select from `Existing All-Purpose Compute` clusters

  - however, that's not recommended,
    b/c
    all-purpose compute clusters are optimized for interactive development
    and
    they're not intended for be used for scheduled tasks
    and
    they're more expensive than `Classic Job Compute` clusters
    and
    they're likely to be shared across different resources (and thus risk interference from other workloads)

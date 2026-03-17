# 213-difference-between-development-and-production.md



## Introduction

If you click on your «(Lakeflow Declarative) Pipeline»,
you will notice a `Development | Production` toggle.

That toggle controls how the pipeline is executed and managed.
It affects the cluster behavior, performance, and your overall cost.



## `Development` mode

This mode is for experimenting, debugging, or adding new tables and fast feedback.

- you get faster iteration

- it is designed for building and testing pipelines

- you get a smaller ephemeral cluster
  that starts faster
  
- w.r.t. execution,
  it prioritizes interactivity,
  but it may not be fully optimized for scale

  you can see results quickly;

  while it's still reliable,
  it's geared towards quick debugging rather than efficiency

  limited auto-scaling

- it is intended for one developer testing changes



## `Production` mode

This mode is your live pipeline delivering data to consumers with SLAs.
(That pipeline must be stable, scalable, and efficient.)

- it optimizes execution.

  it is designed for running at scale in a reliable, cost-efficient way

- you get a production-optimized pipeline cluster with
  better autoscaling, stability, and resource management

- w.r.t. execution,
  it prioritizes throughput and resilience

- retries and recovery are tuned for continuous operation

- w.r.t. monitoring,
  you get full operational logging metrics and event reporting
  for observability



## Conclusion

- use `Development` mode to build and test a «pipeline»

- you are happy with it,
  switch it over to `Production` mode

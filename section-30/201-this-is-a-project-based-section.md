# 201-this-is-a-project-based-section.md



## Introduction

This section covers «Lakeflow Declarative Pipelines»,
but it does that in a purely project-based way.

(
Occasionally, Databricks makes updates to their products.

«Lakeflow Declarative Pipelines»
used to be called
«Delta Live Tables» (DLT).
)

> As a disclaimer:
> 
> This is not going to cover every aspect of the topic,
> because that would require a full course in itself.
>
> But it will cover all of the key concepts
> in a way that will enable you to continue learning on your own.



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/dlt/
  which redirects to
  https://learn.microsoft.com/en-us/azure/databricks/ldp/



## Overview of «Lakeflow Declarative Pipelines»

- «Lakeflow Declarative Pipelines» is a framework for creating batch and streaming data pipelines.

- You can do it in SQL or Python.

- Instead of writing «imperative» pipeline code
  (where you explicitly control the order of operations, checkpoints, and execution),
  you use a «declarative» style, i.e.
  
  - you describe what the data flow should look like

    (which includes the inputs, the transformations, and the outputs)
    
  - and then Databricks will figure out how to execute it efficiently and reliably



## More details about «Lakeflow Declarative Pipelines»

- declarative definition of tables

  You define datasets as live tables or views.

  You specify the transformations, but you don't manage the execution order.

  The pipeline engine builds the directed acyclic graph (DAG) of dependencies automatically.

- Databricks also manages the reliability

  Things like retries, checkpoints, and incremental refresh are handled automatically.
  
  For streaming pipelines,
  the state and the checkpoints are tracked
  without you writing any Spark checkpoint code.

- built-in data quality and expectations

  data-quality rules, expectations, and transformations
  can be embedded in the pipeline definition

- simplified operations

  You get automatic lineage monitoring and error handling.

  The system takes care of the orchestration, the cluster scaling, and the recovery.



> [in summary]
>
> With «Lakeflow Declarative Pipelines»,
>
> you declare your tables and your transformations, and
>
> Databricks manages the execution lifecycle dependencies and reliability.
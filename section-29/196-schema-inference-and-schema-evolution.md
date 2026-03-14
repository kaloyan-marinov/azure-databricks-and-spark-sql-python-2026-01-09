# 196-schema-inference-and-schema-evolution.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema



## Introduction

You can configure «Auto Loader» to automatically detect the schema of loaded data,
allowing you to:

(a) initialize tables without explicitly declaring the data schema and

(b) evolve the table schema as new columns are introduced.

This eliminates the need to manually track and apply schema changes over time.



> When you use «Auto Loader»,
> simply specifying a target directory for the `cloudFiles.schemaLocation` option
> causes «schema inference» and «schema evolution» to be enabled.



## «Schema inference»

«Schema inference» is the process
by which Spark or «Auto Loader» automatically detects the structure of incoming data (including column names and data types)
without requiring you to manually define the schema.

- «Auto Loader» will scan the input files -
  either the first 50 GB or 1000 files it discovers, whichever limit is crossed first

- «Auto Loader» will store the schema information in the directory
  (represented by the value of `cloudFiles.schemaLocation`)

> That is usefule when
>
> (a) you don't want to manually define the schema, and
>
> (b) «schema evolution» may take place over time.



## «Schema evolution»

«Schema evolution» is a feature of «Auto Loader»
that enables it to detect the addition of new columns as it processes incoming data.

«Auto Loader» supports the following modes for «schema evolution»,
which you set in the `cloudFiles.schemaEvolutionMode` option:

- `none`

  > This value is the default when a schema is provided.

- `addNewColumns`

  > This value is the default when a schema is not provided.

  When «Auto Loader» detects a new column, these things take place:

  1. «Auto Loader» performs «schema inference» on the latest «micro-batch» of data
     and
     updates the schema location with the latest schema by merging new columns to the end of the schema.
   
     The data types of existing columns remain unchanged.

  2. The stream fails/stops with an `UnknownFieldException`

- `rescue`

- `failOnNewColumns`

> The «schema evolution» feature can
> imbue a data-processing system with
> the ability to adapt to changes in the structure of incoming data over time,
> without breaking the pipeline.



Databricks recommends
configuring «Auto Loader» streams with «Lakeflow Jobs» to restart automatically after such schema changes.

# 196-schema-inference-and-schema-evolution.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema



## «Schema inference»

When you use «Auto Loader»,
simply specifying a value for `cloudFiles.schemaLocation` causes «schema inference» to be enabled.

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

«Schema evolution» refers to the ability of data processing system to adapt to changes in the structure of incoming data over time,
without breaking the pipeline.

This can be adding a new column to the streaming source, for example.

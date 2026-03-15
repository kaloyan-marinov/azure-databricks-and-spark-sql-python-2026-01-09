# 200-delta-table-streaming-reads-and-writes.md



## Sources

https://learn.microsoft.com/en-gb/azure/databricks/structured-streaming/delta-lake



## Introduction

«Delta lake» is deeply integrated with «Apache Spark Structured Streaming».

That integration is implemented through:
- `readStream`
- `writeStream`

It is possible to use «Delta Lake» tables
as «streaming sources» and «streaming sinks».

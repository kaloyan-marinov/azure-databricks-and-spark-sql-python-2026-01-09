# 181-2-managed-tables.md

## Source

- https://docs.databricks.com/aws/en/tables/managed ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/tables/managed

## Introduction

«Managed tables» are the default and recommended table type in Databricks.

Databricks recommends using «managed tables» to take advantage of:

- Reduced storage and compute costs.

- Faster query performance across all client types.

- Automatic table maintenance and optimization.

- Secure access for non-Databricks clients via «open APIs».

  - and via «credential vending»,
    «Unity Catalog» enables external engines to access «managed tables»

    examples of such external engines:

    - Trino

    - DuckDB

    - Apache Spark

    - Daft

    - Iceberg REST catalog-integrated engines like Dremio and Snowflake

- Support for «Delta Lake» and «Apache Iceberg» formats.

- Automatic upgrades to the latest platform features.

## Features that are unique to «managed tables» (and that are not available for «external tables» and «foreign tables»)

- predictive optimization

- automatic liquid clustering

- metadata caching

- automatic file deletion after a `DROP TABLE` command

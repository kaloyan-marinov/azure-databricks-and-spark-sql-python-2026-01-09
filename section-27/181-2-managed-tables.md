# 181-2-managed-tables.md

## Source

- https://docs.databricks.com/aws/en/tables/managed ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/tables/managed

- https://docs.databricks.com/aws/en/tables/delta-table#managed-tables

## Introduction

«Managed tables» are the default and recommended table type in Databricks.

Databricks recommends using «managed tables»
to take advantage of:

0. Support for «Delta Lake» and «Apache Iceberg» formats.

1. Automatic upgrades to the latest platform features.

2. the following suite of features, which «managed tables» provide:

   - Automatic optimization for reduced storage and compute costs

   - Faster query performance across all client types

   - Automatic table maintenance and optimization

   - Secure access for non-Databricks clients via «open APIs»

     - through «open APIs» and «credential vending»,
       «Unity Catalog» enables external engines to access «managed tables»

       > examples of such external engines:
       >
       > - Trino
       >
       > - DuckDB
       >
       > - Apache Spark
       >
       > - Daft
       >
       > - Iceberg REST catalog-integrated engines like Dremio and Snowflake

       ---

       > The following «open APIs» provide external systems access to «Unity Catalog» «managed tables»:
       >
       > - «Unity REST API»
       >
       >   Provides read-only access for «Delta clients» to «managed tables»
       >
       > - «Iceberg REST Catalog (IRC)»
       >
       >   Provides
       >
       >   (a) read and write access for «Iceberg clients» to managed Iceberg tables, and
       >
       >   (b) read-only access to Delta tables with «Iceberg reads enabled (UniForm)».

     - For external clients that don't support «open APIs»,
       you can use «Compatibility Mode» to read «managed tables»
       using any «Delta Lake client» or «Iceberg client»



## Features that are unique to «managed tables» (and that are not available for «external tables» and «foreign tables»)

- predictive optimization

- automatic liquid clustering

- metadata caching

- automatic file deletion after a `DROP TABLE` command

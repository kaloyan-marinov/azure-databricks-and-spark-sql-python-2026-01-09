# 181-3-external-tables.md

## Sources

- https://docs.databricks.com/aws/en/tables/external

- https://docs.databricks.com/aws/en/tables/delta-table#external-tables

## Introduction

In «Unity Catalog»,
an «external table» stores its underlying data files
in cloud object storage within your cloud tenant.

- «Unity Catalog» manages the table's metadata,
  ensuring data governance across all queries

- «Unity Catalog» does NOT manage
  the data's lifecycle, optimization, storage location, or layout

- «external tables» support several formats:

  - «Delta Lake» format (recommended)
  
  - CSV, JSON, AVRO, PARQUET, ORC, and TEXT formats

    «External tables» based on those formats lack
    the transactional guarantees and performance optimizations of «Delta Lake».

## When to use «external tables»

Databricks recommends using «external tables»
when you need to:

- Register existing data that is not compatible with «managed tables»

- allow for
  direct access to the data
  from non-Databricks clients that do not support other external access patterns
  
  > «Unity Catalog» privileges are NOT enforced
  > when users access data files from external systems.

  ---

  > If you update «external table» metadata
  > using a non-Databricks client or using path-based access from within Databricks,
  > that metadata does not automatically sync state with «Unity Catalog».
  >
  > Databricks recommends against such metadata updates;
  > but if you do perform one,
  > you must run `MSCK REPAIR TABLE <table-name> SYNC METADATA`
  > to bring the schema in «Unity Catalog» up to date.

## Before you can create an «external table», ...

... you must first configure an «external location»
that grants access to your cloud storage

"When you define a Unity Catalog external table, you must specify a storage location. This location is an external location registered in Unity Catalog."

## Further reading

- To convert an «external table» to a «managed table»,
  see https://docs.databricks.com/aws/en/tables/convert-external-managed

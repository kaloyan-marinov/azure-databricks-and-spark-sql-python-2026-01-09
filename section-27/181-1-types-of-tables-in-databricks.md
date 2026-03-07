# 181-1-types-of-tables-in-databricks.md

## Source

https://docs.databricks.com/aws/en/tables/delta-table

## Introduction

«Unity Catalog» supports several primary table types.
Each type differs in

(a) how its underlying data files are stored;

(b) how the lifecycle of those files is managed;

(c) how those files are optimized
    (for the purpose of reducing storage and compute costs);

## Overview

| feature                 | «managed tables»        | «external tables» | «foreign tables»        |
| ----------------------- | ----------------------- | ----------------- | ----------------------- |
| storage                 | «Unity Catalog» manages | you specify       | external system         |
| lifecycle management    | «Unity Catalog» manages | you manage        | external system manages |
| automatic optimizations | yes                     | limited           | none                    |

## Remarks

- Generally speaking,
  Databricks recommends using «managed tables»
  (and they are the default)

  1. «Unity Catalog» manages the storage location, data lifecycle, and optimizations

  2. when you drop a «managed table»,
     both its metadata and underlying data files are deleted

  3. «managed tables» are backed by «Delta Lake» or «Apache Iceberg»

  4. «managed tables» provide a suite of features:

     - Automatic optimization for reduced storage and compute costs

     - Faster query performance across all client types

     - Automatic table maintenance

     - Secure access for non-Databricks clients via «open APIs»

     - Automatic upgrades to the latest platform features

- But «external tables» do have their use cases.

  1. «Unity Catalog» governs data access

  2. «Unity Catalog» does NOT manage the storage layout, data lifecycle, or optimizations

  3. when you drop a «external table»,
     only its metadata is deleted
     (but its underlying data files remain)

  4. «external tables» support several formats:
  
     - «Delta Lake» format (recommended)
     
     - CSV, JSON, AVRO, PARQUET, ORC, and TEXT formats

       «External tables» based on those formats lack
       the transactional guarantees and performance optimizations of «Delta Lake».

  5. Use «external tables» when you need to:

     - Register existing data that is not compatible with «managed tables»

     - Provide direct data access from non-Databricks clients
       that do not support other external access patterns

- «foreign tables»: ...

- other table types:

  - «streaming tables»: ...

  - «materialized views»: ...

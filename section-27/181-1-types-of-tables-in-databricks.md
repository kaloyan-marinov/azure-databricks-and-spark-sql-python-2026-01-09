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

- But «external tables» do have their use cases.

register data stored in cloud object storage that you manage

  1. «Unity Catalog» governs data access

  2. when you drop a «external table»,
     only its metadata is deleted
     (but its underlying data files remain)

- «foreign tables»: ...

- other table types:

  - «streaming tables»: ...

  - «materialized views»: ...

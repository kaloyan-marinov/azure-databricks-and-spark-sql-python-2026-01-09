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

- «managed tables»

  1. «Unity Catalog» manages the following:
     storage location; storage layout; data lifecycle; optimizations;

  2. when you drop a «managed table»,
     both its metadata and underlying data files are deleted

  3. «managed tables» are backed by «Delta Lake» or «Apache Iceberg»

- «external tables»

  1. creating an «external table»
     means
     creating a table in the «Unity Catalog» «metastore»,
     with said table being underpinned/"backed" by
     data files which reside in cloud object storage
                                a cloud-based object store

  2. «Unity Catalog»:
  
     - manages the table's metadata
       
       (which includes but is not limited to
       ensuring data governance across all queries)

     - does NOT manage any of the following:
       storage location; storage layout; data lifecycle; optimizations;

  3. when you drop an «external table»,
     only its metadata is deleted
     (but its underlying data files remain)

- «foreign tables»: ...

- other table types:

  - «streaming tables»: ...

  - «materialized views»: ...

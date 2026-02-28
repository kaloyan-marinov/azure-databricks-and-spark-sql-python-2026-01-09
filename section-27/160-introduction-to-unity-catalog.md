# 160-introduction-to-unity-catalog.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/#-the-unity-catalog-object-model .)

## Recall

We've actually been using <u>Unity Catalog</u>
since pretty much the beginning of this course -
we've used:

- catalogs
- schemas
- volumes, tables and views

Those are all objects in <u>Unity Catalog</u>.



But <u>Unity Catalog</u> is much more than just that.
It's a centralized data catalog that provides:

- access control
- auditing
- lineage
- quality monitoring, and
- data discovery capabilities

across your Databricks workspaces.



## Introduction

<u>Unity Catalog</u> is the governance solution for data-and-AI «securable objects» on Databricks.



«Data governance» is the framework of roles, policies, and controls
that decide

- who can do what with which data,
- for what purpose, and
- how it's verified.



## The key features

1. Define once, secure everywhere

   - offers a single place to administer data-access policies
     that apply across all Databricks workspaces in a region

2. Standards-compliant security model

   - its security model is based on standard ANSI SQL

3. Built-in auditing and lineage

   - automatically captures user-level audit-logs

   - captures lineage data

4. Data discovery

   - lets you tag and document data assets

   - provides a search interface to help data consumers find data assets

5. System tables

   - lets you easily access and query your account's *operational data*,
     including:

     - audit logs
     
     - billable usage

     - lineage

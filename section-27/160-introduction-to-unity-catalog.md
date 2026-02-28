# 160-introduction-to-unity-catalog.md

## Remarks about the sources for this file

sources:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/ ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/



## Recall some theoretical background

To paraphrase a portion of `section-00/00-01-databricks.md`:
«data governance» is a framework of policies, processes, and technical controls
that
- maintain data quality
- decide
  - who can do what with which data,
  - for what purpose, and
  - how it's verified.

To paraphrase a portion of `section-00/00-02-databricks-components.md`,
«Unity Catalog» is an open-source «data governance» solution deeply integrated into Databricks,
which
- is comprised of [a "catalog" of] data-and-AI «securable objects» and related capabilities;
- spans your «Databricks workspaces».



## Practical manifestations

We've actually been using «Unity Catalog»
since pretty much the beginning of this course -
we've used:

- catalogs
- schemas
- volumes, tables and views

Those are all «securable objects» in «Unity Catalog».



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

   - lets you tag and document "data assets"

   - provides a search interface to help data consumers find "data assets"

5. System tables

   - lets you easily access and query your account's *operational data*,
     including:

     - audit logs
     
     - billable usage

     - lineage

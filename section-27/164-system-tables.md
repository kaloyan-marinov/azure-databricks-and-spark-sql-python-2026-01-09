# 164-system-tables.md



## Introduction

<u>System tables</u> are a Databricks-hosted, read-only store
of your Databricks account's operational data.

They:

- are exposed in every <u>Unity Catalog</u> <u>metastore</u>
  under a built-in `CATALOG` named `system`

- enable you to query things such as

  - audit events

  - billable usage

  - lineage

  - compute history
  
  - jobs

  - query history

  - etc.

- are accessible only from a Databricks workspace
  which has been enabled for <u>Unity Catalog</u>

- aggregated data
  from all Databricks workspaces in the same cloud region

  <u>
  TODO: (2026/02/21, 09:04 CET): 
  
  is the above statement actually correct?

  shouldn't it be changed to
  "across all Databricks workspaces attached to a <u>Unity Catalog</u> <u>metastore</u>"
  ?
  </u>



## Examples

The `system.information_schema` contains information about
objects across all `CATALOG`s within the <u>metastore</u>.

The `system.access.audit` (table) includes
records for all audit events from Databricks workspaces in your region.

The `system.lakeflow.job_run_timeline` (table) tracks
the start and end times of all job runs,
as well as the `result_state`, `run_type`, etc.



## Further information

https://learn.microsoft.com/en-us/azure/databricks/admin/system-tables/

# 163-data-discovery-and-lineage.md

This lecture is a demonstration of how <u>Unity Catalog</u> enables

- data discovery, and

- lineage

## Data discovery

Search for "data assets"
by using the search bars in the web UI of your Databricks workspace.


## Lineage

- click on «Catalog» in the side panel

- click on a table

- go to the «Lineage» tab

  - lineage is aggregated across all Databricks workspaces attached to a <u>Unity Catalog</u> <u>metastore</u>
    (i.e. lineage captured in one Databricks workspace is visible
    in any other Databricks workspace that shares that <u>metastore</u>)

  - lineage data includes

    - notebooks

    - jobs

    - dashboards

    - etc.

  - cick on «See lineage graph»

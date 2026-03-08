# 184-simulate-the-existence-of-the-ADLS-gen-2-account-owned-by-team-B.md

## In the Azure Portal

- create an Azure Resource Group
  called (something similar to) `rg-nyctaxi-export-westeurope`

- within `rg-nyctaxi-export-westeurope`,
  create an ADLS Gen 2 account
  called (something similar to) `nyctaxistorage17`

  - specify the same region

  - specify `Redundacy` as `Locally-redundant storage (LRS)`
    (b/c it is perfectly adequate for the purposes of this course)

  - check the `Enable hierarchical namespace` option

    > Hierarchical namespace, complemented by Data Lake Storage Gen2 endpoint:
    > - enables file and directory semantics,
    > - accelerates big data analytics workloads, and
    > - enables access control lists (ACLs).

- within `nyctaxistorage17`,
  create a container
  called (something similar to) `nyctaxi-yellow`

---

- within `rg-dataengineering-sandbox-westeurope`,
  create an «Access Connector for Azure Databricks»
  called (something similar to) `nyctaxi-export-access-connector`

  - specify the same region as your «Databricks workspace»

- within `nyctaxistorage17`:

  - go to «Access Control (IAM)»

  - click on «Add» and then on «Add role assignment»
  
  - select the «Storage Blob Data Contributor» role

  - under «Assign access to»,
    select «Managed identity»

  - under «Members»,
    select `nyctaxi-export-access-connector`

## In the «Databricks workspace»

click on «Catalog»:

- create a «storage credential»
  called (something similar to) `nyctaxi-storage-credential`

  - under «Access connector ID`,
    provide the «Resource ID» of `nyctaxi-export-access-connector`

- create an «external location»
  called (something similar to) `nyctaxi-yellow-ext-location`

  - under «URL»,
    specify `abfss://nyctaxi-yellow@nyctaxistorage17.dfs.core.windows.net/`

  - under «Storage credential»,
    select `nyctaxi-storage-credential`



click on «Catalog»:

- in the `nyctaxi` «catalog»,
  create a new «schema» called `04_export`

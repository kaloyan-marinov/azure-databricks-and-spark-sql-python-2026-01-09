# 161-1-metastore.md



## Something familiar

When we provisioned an `Azure Databricks` service
(which, e.g., we may have named `dbw-dataengineering-sandbox-westeurope-001`),
that:

- caused the following Azure resources to get created:
  - the `dbw-dataengineering-sandbox-westeurope-001` service itself (and, inside of that service "aka Databricks workspace", also a <u>metastore</u> in the same region as the workspace)
  - an additional `Azure Resource Group` (which, sticking with the earlier example, may have been named something along the lines of `databricks-rg-dbw-dataengineering-sandbox-westeurope-001-o7zhdxdmqk4qy`), which in turn contains:
    - an `Azure Storage account` resource
    - an `Azure Access Connector for Azure Databricks` resource
    - an `Azure Managed identity` resource
    - an `Azure Network security group` resource
    - an `Azure Virtual network` resource

- enabled the Databricks workspace for <u>Unity Catalog</u>
  by assigning it to the created <u>metastore</u>



## What is a metastore?

(A lot of this section comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/#-the-unity-catalog-object-model .)

In <u>Unity Catalog</u>, a <u>metastore</u> is a top-level container, whose purpose is to register
(a) metadata about data and AI assets,
and
(b) the permissions that govern access to those assets.

The way to enable Databricks workspace for <u>Unity Catalog</u>
is
to attach it to a <u>metastore</u> in the same cloud region (as the Databricks workspace itself).

Remarks:

- That means that <u>metastores</u> are regional.

  - Only one <u>metastore</u> per region is allowed.

- A Databricks workspace can be attached to only one <u>metastore</u>,
  and they need co-located in the same region.

- Any number of Databricks workspaces can be attached to the same <u>metastore</u>.

  - This is what enables multiple Databricks workspaces in the same region
    to see the same data and AI assets

- The <u>metastore</u> "sits above" all of its attached Databricks workspaces.

  - Objects (such as catalogs; schemas; volumes, tables, and views)
    that are created via a Databricks workspace
    are registered in the <u>metastore</u> (not in a single Databricks workspace).

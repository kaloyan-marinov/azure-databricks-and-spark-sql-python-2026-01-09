# 161-1-metastore.md



## Something familiar

When we provisioned an `Azure Databricks` service
(which, e.g., we may have named `dbw-dataengineering-sandbox-westeurope-001`),
that:

- caused the following Azure resources to get created:
  - the `dbw-dataengineering-sandbox-westeurope-001` service itself and, inside of that service (aka «Databricks workspace»), also a «metastore» in the same region as the service
  - an additional `Azure Resource Group` (which, sticking with the earlier example, may have been named something along the lines of `databricks-rg-dbw-dataengineering-sandbox-westeurope-001-o7zhdxdmqk4qy`), which in turn contains:
    - an `Azure Storage account` resource
    - an `Azure Access Connector for Azure Databricks` resource
    - an `Azure Managed identity` resource
    - an `Azure Network security group` resource
    - an `Azure Virtual network` resource

- enabled the «Databricks workspace» for «Unity Catalog»
  by assigning it to the created «metastore»



## What is a «metastore»?

It is worthwhile to re-read the relevant portion of `section-00/00-02-databricks-components.md`
in order to recall what a «metastore» is.

The contents of a «metastore»
are organized in a 3-level hierarchy.


```
metastore

    # non-data «securable objects»
    # for managing access to external data sources
    service credential
    storage credential
    external location
    external metadata

    # data-and-AI «securable objects» (aka "data assets")
    catalog                                 # the top level in the data-isolation scheme

        schema (aka databases)              # organize "data assets" into logical categories
                                            # that are more granular than catalogs
            table
            view
            volume
            function (including models)

    # non-data «securable objects»
    # for managing access to shared assets
    share
    recipient
    provider
    connection
    clean room
```




## Practical aspects of working with a «metastore»

sources:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/ ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/

The way to enable a «Databricks workspace» for «Unity Catalog»
is
to attach it to a «metastore» in the same cloud region (as the «Databricks workspace» itself).

Remarks:

- That means that «metastores» are regional.

  - Only one «metastore» per region is allowed.

- A «Databricks workspace» can be attached to only one «metastore»,
  and they need co-located in the same region.

- Any number of «Databricks workspaces» can be attached to the same «metastore».

  - This is what enables multiple «Databricks workspaces» in the same region
    to see the same data-and-AI «securable objects»

- The «metastore» "sits above" all of its attached «Databricks workspaces».

  - Objects (such as «catalogs»; «schemas»; «volumes», «tables», and «views»; etc.)
    that are created via a «Databricks workspace»
    are registered in the «metastore» (not in a single «Databricks workspace»).

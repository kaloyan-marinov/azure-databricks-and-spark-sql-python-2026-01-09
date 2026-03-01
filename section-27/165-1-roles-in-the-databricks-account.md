# 165-roles-in-the-databricks-account.md

sources:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/admin-privileges

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/



## An overview

An «account admin» controls the «Databricks account».
(This includes being able to delegate itself as either of the following roles.)

«Metastore admin» controls a specific «Unity Catalog» «metastore».

«Workspace admin» controls a specific «Databricks workspace».



## A more detailed look

«Account admin»:

- is a highly privileged role that you should distribute carefully

- have the following privileges:

  - can create «metastores»

    (
    
    and, by default, become the initial «metastore admin»

    = when you create your very first «Databricks workspace»,
    Databricks automatically creates a «metastore» for you in that region
    and
    the «account admin» is automatically given the «metastore admin» role for that «metastore»
    
    )

  - can link «metastores» to «Databricks workspaces»

  - can assign the «metastore admin» role

  - can grant privileges on «metastores»

  - can enable «Delta Sharing» for a «metastores»

  - can set up «storage credentials» (for accessing cloud storage)

  - enable «system tables» and control who can access them



«Metastore admin»:

- is a highly privileged role that you should distribute carefully

- owns a specific «Unity Catalog» «metastore»

  - can create all top-level «securable objects» (within that «metastore»)



«Workspace admin»:

- is a highly privileged role that you should distribute carefully

- focuses on the operations at the level of an individual «Databricks workspace»

  - can add users, service principals, and/or groups to the «Databricks workspace»

  - can assign the «workspace admin» role to users, service principals, and/or groups

  - can manage job ownership

  - can view and manage Databricks-workspace objects (such as notebooks, queries, etc.)

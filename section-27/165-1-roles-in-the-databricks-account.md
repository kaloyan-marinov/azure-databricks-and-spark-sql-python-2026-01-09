# 165-roles-in-the-databricks-account.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/admin-privileges .)

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/



## An overview

An <u>account admin</u> controls the Databricks account.
(This includes being able to delegate itself as either of the following roles.)

<u>Metastore admin</u> controls a specific <u>Unity Catalog</u> <u>metastore</u>.

<u>Workspace admin</u> controls a specific Databricks workspace.



## A more detailed look

<u>Account admin</u>:

- is a highly privileged role that you should distribute carefully

- have the following privileges:

  - can create <u>metastores</u>

    (
    
    and, by default, become the initial <u>metastore admin</u>

    = when you create your very first Databricks workspace,
    Databricks automatically creates a <u>metastore</u> for you in that region
    and
    the <u>account admin</u> is automatically given the <u>metastore admin</u> role for that <u>metastore</u>
    
    )

  - can link <u>metastores</u> to Databricks workspaces

  - can assign the <u>metastore admin</u> role

  - can grant privileges on <u>metastores</u>

  - can enable Delta Sharing for a <u>metastores</u>

  - can set up <u>storage credentials</u> (for accessing cloud storage)

  - enable <u>system tables</u> and control who can access them



<u>Metastore admin</u>:

- is a highly privileged role that you should distribute carefully

- owns a specific <u>Unity Catalog</u> <u>metastore</u>

  - can create all top-level <u>securable objects</u> (within that <u>metastore</u>)



<u>Workspace admin</u>:

- is a highly privileged role that you should distribute carefully

- focuses on the operations at the level of an individual Databricks workspace

  - can add users, service principals, and/or groups to the Databricks workspace

  - can assign the <u>workspace admin</u> role to users, service principals, and/or groups

  - can manage job ownership

  - can view and manage Databricks-workspace objects (such as notebooks, queries, etc.)

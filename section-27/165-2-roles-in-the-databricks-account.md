# 165-1-roles-in-the-databricks-account.md

sources:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/ ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/admin-privileges



## An overview

In Datatricks,
there exist several «admin roles».

- An «account admin» controls the entire «Databricks account».
  (This includes being able to delegate itself as either of the following roles.)

- «Metastore admin» controls a specific «Unity Catalog» «metastore».

  It is optional.

  Databricks recommends assigning the «metastore admin» role to a «group».

- «Workspace admin» controls an individual «Databricks workspace».

<u>Each of those is a highly privileged role that you should distribute carefully.</u>



## «Account admin»

  - can create «metastores»
    (and, by default, become the initial «metastore admin»)

  - can link «metastores» to «Databricks workspaces»

  - can assign the «metastore admin» role

  - can grant privileges on «metastores»

  - can enable «Delta Sharing» for a «metastores»

  - can set up «storage credentials» (for accessing cloud storage)

  - enable «system tables» and control who can access them

  ---

  - can restrict the privileges of the «workspace admin» role
    (using the `RestrictWorkspaceAdmins` setting)



## «Workspace admin»

  - can add users, service principals, and/or groups to the «Databricks workspace»

  - can assign the «workspace admin» role to users, service principals, and/or groups

  - can manage job ownership

  - can view and manage Databricks-workspace objects (such as notebooks, queries, etc.)

  ---

  If your «Databricks workspace» was created
  with [automatic enablement of «Unity Catalog»](
    https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started#enablement
  ),
  then:

  - Databricks automatically creates a «metastore» for you in the same region as the «Databricks workspace»

  - the «Databricks workspace» is attached to that «metastore»

  - the «metastore» is created without a «metastore admin»

  - the «workspace admin» role has the following privileges on the attached «metastore» by default:

    ...



## «Metastore admin»

- manage privileges of all «securable objects» within a specific «metastore»

- transfer ownership of all «securable objects» within said «metastore»

- ...

- delete said «metastore»

---

The following actions CANNOT be performed by any other role,
INCLUDING «account admins» or «workspace admins»:

...

If any of those actions need to be performed,
then the «metastore admin» role must be assigned to at least one «Databricks identity».

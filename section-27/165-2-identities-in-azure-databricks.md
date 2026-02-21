# 165-2-identities-in-azure-databricks.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/best-practices .)



There are three types of Azure Databricks identity:

Users: User identities recognized by Azure Databricks and represented by email addresses.
Service principals: Identities for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms.
Groups: Groups simplify identity management, making it easier to assign access to workspaces, data, and other securable objects.
Databricks recommends creating service principals to run production jobs or modify production data. If all processes that act on production data run using service principals, interactive users do not need any write, delete, or modify privileges in production. This eliminates the risk of a user overwriting production data by accident.

It is best practice to assign access to workspaces and access-control policies in Unity Catalog to groups, instead of to users individually. All Azure Databricks identities can be assigned as members of groups, and members inherit permissions that are assigned to their group.

The following are the administrative roles that can manage Azure Databricks identities:

Account admins can add users, service principals, and groups to the account and assign them admin roles. They can give users access to workspaces, as long as those workspaces use identity federation.
Workspace admins can add users, service principals to the Azure Databricks account. They can also add groups to the Azure Databricks account if their workspaces are enabled for identity federation. Workspace admins can grant users, service principals, and groups access to their workspaces.
Group managers can manage group membership. They can also assign other users the group manager role.
Service principal managers can manage roles on a service principal.
Databricks recommends that there be a limited number of account admins per account and workspace admins in each workspace.

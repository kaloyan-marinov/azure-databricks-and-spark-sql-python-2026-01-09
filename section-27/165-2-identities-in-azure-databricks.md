# 165-2-identities-in-azure-databricks.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/best-practices .)

(The following resource might even be a more well-written version of the previous resource: https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/#identity-model )


## Azure Databricks identities

There are three types of <u>Azure Databricks identity</u>:

- <u>Users</u>

  This type of identity is represented by an email address.

- <u>Service principals</u>

  This type of identity is intended to be used with
  - jobs,
  - automated tools, and
  - systems such as scripts, apps, and CI/CD platforms.

- <u>Groups</u>

  This type of identity plays an auxiliary but important role in that
  its aim is to simplify identity management
  (making it easier to assign access to workspaces, data, and other securable objects).



## How to manage Azure Databricks identities

The following are <u>the administrative roles</u> that can manage <u>Azure Databricks identities</u>:

- <u>Account admins</u> can

  - add users, service principals, and groups to the account
    and
    assign them admin roles

  - give users access to workspaces, as long as those workspaces use identity federation

- <u>Workspace admins</u> can

   - add users, service principals to the Azure Databricks account
   
   - add groups to the Azure Databricks account if their workspaces are enabled for identity federation
   
   - grant users, service principals, and groups access to their workspaces

- <u>Group managers</u> can

   - manage group membership
   
   - assign <u>the group manager role</u> to other users

- <u>Service principal managers</u> can

   - manage roles on a <u>service principal</u>



## Opinionated perspective on how to best configure identity in Azure Databricks

Before proceeding,
it might be helpful to re-read `section-27/165-1-roles-in-the-databricks-account.md`.



Databricks recommends:

- that there be a limited number of

  - <u>account admins</u> per account and
  
  - <u>workspace admins</u> in each workspace

- creating <u>service principals</u> to run production jobs or modify production data.

  > If all processes that act on production data run using service principals,
  > interactive users do not need any write, delete, or modify privileges in production.
  > This eliminates the risk of a user overwriting production data by accident.

- assigning
  access to workspaces and access-control policies in Unity Catalog
  to <u>groups</u>, instead of to <u>users</u> individually.
  All <u>Azure Databricks identities</u> can be assigned as members of <u>groups</u>,
  and members inherit permissions that are assigned to their <u>group</u>.

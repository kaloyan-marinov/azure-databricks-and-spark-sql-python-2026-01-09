# 165-2-identities-in-azure-databricks.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/best-practices .)

(The following resource might even be a more well-written version of the previous resource: https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/#identity-model )


## Databricks identities

Recall from `section-00/00-02-databricks-components.md`:
Databricks supports three «Databricks identities»
for authentication and access control:

- «Users»

- «Service principals»

- «Groups»



Remarks:

- every «user» you add to a Databricks workspace
  is automatically put in
  the built-in «Users» group

- by default, the built-in «Users» group gets workspace access
  (allowing its members to create notebooks, Lakeflow jobs, and so on)



## Identity federation

source:
- https://docs.databricks.com/aws/en/admin/users-groups/
- https://docs.databricks.com/aws/en/admin/users-groups/best-practices

«Identity federation» is a feature,
which can be enabled in the Configuration tab of a «Databricks workspace».

- «Identity federation» allows you to
  (a) configure «Databricks identities» once in the «Databricks account» console,
  and
  (b) when you go to the admin settings of a specific «Databricks workspace»,
  select from the «Databricks identities» that exist in your «Databricks account»

  (
  
  = manage «Databricks identities» centrally at the «Databricks account» level
  and
  assign them to «Databricks workspaces»

  = configure «Databricks identities» in the «Databricks account» console,
  and then allow those «Databricks identities» to access to specific «Databricks workspaces»

  = not have to repeat the configuration of the same «Databricks identities»
  separately in each «Databricks workspace»

  )
  

- Databricks began to
  enable new «Databricks workspaces» for «identity federation» and «Unity Catalog» automatically
  on November 8, 2023

- If your «Databricks workspace» is enabled for «identity federation» by default,
  it cannot be disabled.



## How to manage Azure Databricks identities

The following are <u>the administrative roles</u> that can manage <u>Azure Databricks identities</u>:

- <u>Account admins</u> can

  - add users, service principals, and groups to the account
    and
    assign them admin roles

  - give users access to Databricks workspaces, as long as those Databricks workspaces use <u>identity federation</u>

- <u>Workspace admins</u> can

   - add users, service principals to the Azure Databricks account
   
   - add groups to the Azure Databricks account if their Databricks workspaces are enabled for <u>identity federation</u>
   
   - grant users, service principals, and groups access to their Databricks workspaces

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

  > If all processes that act on production data run using <u>service principals</u>,
  > interactive users do not need any «write privileges», «delete privileges», or «modify privileges» in production.
  > This eliminates the risk of a user overwriting production data by accident.

- assigning
  access to Databricks workspaces and access-control policies in <u>Unity Catalog</u>
  to <u>groups</u>, instead of to <u>users</u> individually.

  > All <u>Azure Databricks identities</u> can be assigned as members of <u>groups</u>,
  > and members inherit permissions that are assigned to their <u>group</u>.



## Other account-level roles

- <u>marketplace admins</u>

- <u>billing admins</u>

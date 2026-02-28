# 165-2-identities-in-azure-databricks.md

(A lot of this file comes from https://docs.databricks.com/aws/en/admin/users-groups/best-practices , which is _essentially_ the same as https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/best-practices .)

(The following resource might even be a more well-written version of the previous resource: https://docs.databricks.com/aws/en/admin/users-groups/ , which is _essentially_ the same as https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/#identity-model )

  - https://docs.databricks.com/aws/en/admin/users-groups/scim/

    - https://simplecloud.info/ = System for Cross-domain Identity Management (SCIM)

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

## How to manage Databricks identities

sources:
- primary: https://docs.databricks.com/aws/en/admin/users-groups/best-practices
- secondary: https://docs.databricks.com/aws/en/admin/users-groups/

To manage «Databricks identities», you must have one of the following roles:

- «Account admins» can

  - add users, service principals, and groups to the account
    and
    assign them admin roles

  - give users access to Databricks workspaces, as long as those Databricks workspaces use «identity federation»

- «Workspace admins» can

   - add users, service principals to the Databricks account
   
   - add groups to the Databricks account if their Databricks workspaces are enabled for «identity federation»

   > Whenever a new user or service principal is added to a workspace using workspace-level interfaces, that user or service principal is synchronized to the account-level. This enables you to have one consistent set of users and service principals in your account.
   
   - grant users, service principals, and groups access to their Databricks workspaces

- «Group managers» can

   - manage group membership
   
   - assign «the group manager role» to other users

- «Service principal managers» can

   - manage roles on a «service principal»



## Opinionated perspective on how to best configure identity in Databricks

Before proceeding,
it might be helpful to re-read `section-27/165-1-roles-in-the-databricks-account.md`.

https://docs.databricks.com/aws/en/admin/users-groups/best-practices

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

  > All <u>Databricks identities</u> can be assigned as members of <u>groups</u>,
  > and members inherit permissions that are assigned to their <u>group</u>.



## Other account-level roles

- <u>marketplace admins</u>

- <u>billing admins</u>

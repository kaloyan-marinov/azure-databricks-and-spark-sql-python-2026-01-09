# 165-2-identities-in-azure-databricks.md



## Remarks about the sources for this file

sources:

- primary:
  
  https://docs.databricks.com/aws/en/admin/users-groups/ ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups

- secondary:
  
  https://docs.databricks.com/aws/en/admin/users-groups/best-practices ,
  which is _essentially_ the same as https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/best-practices

  - https://docs.databricks.com/aws/en/admin/users-groups/scim/

    - https://simplecloud.info/ = System for Cross-domain Identity Management (SCIM)

- there is some overlap between the above-mentioned sources

- in my opinion,
  the primary source is written in a clearer way than the secondary source



## Databricks identities

Recall from `section-00/00-02-databricks-components.md`:
Databricks supports three «Databricks identities»
for authentication and access control:

- «Users»

- «Service principals»

- «Groups»



Remarks:

- every «user» you add to a «Databricks workspace»
  is automatically put in
  the built-in «Users» group

- by default, the built-in «Users» group gets workspace access
  (allowing its members to create notebooks, Lakeflow jobs, and so on)



## Identity federation

sources:
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
https://docs.databricks.com/aws/en/admin/users-groups/

To manage «Databricks identities»,
you must have one of the following «admininistrative roles»
(aka «admin roles»).

(The capabilities of each «admin role» are listed below.)

- «Account admins»

  - Add, update, and delete
    «users», «service principals», and «groups»
    to the «Databricks account».

  - Assign «admin roles»
    and
    grant «users» access to «Databricks workspaces»

    > as long as those «Databricks workspaces» are enabled for «identity federation»
    > (as per https://docs.databricks.com/aws/en/admin/users-groups/best-practices)

  - Automatically have
    - the «group manager» role on each «group» in the «Databricks account»
    - the «service principal manager» role on each «service principals» in the «Databricks account»

- «Workspace admins»

   - Add
     «users», «service principals», and «groups»
     to the «Databricks account»

     > Provided that the «Databricks workspace» in question is enabled for «identity federation»:
     >
     > Whenever a new «user» or «service principal» is added to a «Databricks workspace» (using workspace-level interfaces),
     > that «user» or «service principal» is synchronized to the «Databricks account» level.
     > This enables you to have one consistent set of «users» and «service principals» in your «Databricks account».
     > (as per https://docs.databricks.com/aws/en/admin/users-groups/best-practices)
   
   - Cannot update or delete
     «users» or «service principals»
     in the «Databricks account»

   - Grant
     «users», «service principals», and «groups»
     access to the «Databricks workspace» in question

   - Automatically have
     - the «group manager» role on «groups» they create
     - «service principal manager» role on «service principals» they create

   - Manage legacy «workspace-local groups»

- «Group managers»

   - Manage memberships and delete «groups».
   
   - Assign the «group manager» role to other «users».

- «Service principal managers»

   - Add, update, and remove roles on «service principals».



## Opinionated perspective on how to best configure identity in Databricks

Before proceeding,
it might be helpful to re-read `section-27/165-1-roles-in-the-databricks-account.md`.


sources:
https://docs.databricks.com/aws/en/admin/users-groups/best-practices



Databricks recommends:

- that there be a limited number of

  - «account admins» per account and
  
  - «workspace admins» in each workspace

- creating «service principals» to run production jobs or modify production data.

  > If all processes that act on production data run using «service principals»,
  > interactive users do not need any «write privileges», «delete privileges», or «modify privileges» in production.
  > This eliminates the risk of a user overwriting production data by accident.

- assigning
  access to «Databricks workspaces» and access-control policies in «Unity Catalog»
  to «groups», instead of to «users» individually.

  > All «Databricks identities» can be assigned as members of «groups»,
  > and members inherit permissions that are assigned to their «group».



## Other account-level roles

- «marketplace admins»

- «billing admins»

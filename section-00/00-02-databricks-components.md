# 00-02-databricks-components.md

## Accounts and workspaces

source:
https://docs.databricks.com/aws/en/getting-started/concepts

A «Databricks workspace» is
a Databricks deployment in the cloud
that functions as an environment for your team to access « data and AI «securable objects» ».
(Your organization can choose to have either multiple workspaces or just one,
depending on its needs.)

A «Databricks account» represents a single entity
that can include multiple «Databricks workspaces».
(A «Databricks account» enabled for «Unity Catalog»
can be used to manage users and their access to data
centrally across all of the «Databricks workspaces» in said account.)

## Identities

source:
https://docs.databricks.com/aws/en/admin/users-groups/

Databricks supports three «Databricks identities»
for authentication and access control:

- «Users»

  This is represented by an email address.

- «Service principals»

  This is intended to be used with
  - jobs,
  - automated tools, and
  - systems such as scripts, apps, and CI/CD platforms.

- «Groups»

  This plays an auxiliary but important role in that
  its make easier (and streamlines) the task of managing access to «securable objects».

## «Securable objects» and «access control systems»

source:
https://docs.databricks.com/aws/en/security/auth/

In Databricks,
there are different types of «securable objects»
and, for each type, there is different «access control system».

| type of «securable objects»         | «access control system»           |
| ----------------------------------- | --------------------------------- |
| workspace-level «securable objects» | Access control lists (ACLs)       |
| account-level «securable objects»   | Account role based access control |
| data and AI «securable objects»     | «Unity Catalog»                   |

## Revisit «Databricks workspaces»

A «Databricks workspace» is an environment, which:

- organizes workspace-level «securable objects»
  (such as notebooks, libraries, dashboards, and experiments)
  into folders

- provides access
  to data and AI «securable objects»
  and
  to computational resources

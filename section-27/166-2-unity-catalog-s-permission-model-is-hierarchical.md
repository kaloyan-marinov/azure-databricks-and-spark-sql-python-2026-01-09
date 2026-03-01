# 166-2-unity-catalog-s-permission-model-is-hierarchical.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/ .)



## Introduction

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#inheritance

«Securable objects» in «Unity Catalog» are hierarchical,
and privileges are inherited downward.

The highest-level object that privileges are inherited from is the «catalog».

- This means that
  granting a privilege on a «catalog» (respectively, «schema»)
  automatically grants the privilege to all current and future objects within the «catalog» (respectively, «schema»).

- For example,
  if you give a user the `SELECT` privilege on a «catalog»,
  then that user will be able to select (= read) all tables and views in that «catalog».



BUT: it's also worth noting that
privileges that are granted on a «Unity Catalog» «metastore» are NOT inherited.



## How to grant privileges

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant

You can grant privileges to
- a user,
- a group,
- or a service principal
in a number of ways.

Those ways are:
- use the UI of the Databricks workspace in the «Catalog» explorer
- use ANSI SQL syntax

```sql
-- Show a user's grants on an securable object.
SHOW GRANTS
    `<user>@<domain-name>`
ON
    <securable-type> <securable-name>
;
```

```sql
-- Grant a privilege.
GRANT
    <privilege-type>
ON
    <securable-type> <securable-name>
TO
    <principal>
;



-- Concrete examples of granting a privilege.
GRANT
    CREATE TABLE
ON
    SCHEMA main.default
TO
    `finance-team`
;

GRANT
    USE SCHEMA
ON
    SCHEMA main.default
TO
    `finance-team`
;

GRANT
    USE CATALOG
ON
    CATALOG main
TO
    `finance team`
;
```

```sql
-- Revoke a privilege.
REVOKE
    <privilege-type>
ON
    <securable-type> <securable-name>
FROM
    <principal>
;



-- A concrete example of revoking a privilege.
REVOKE
    CREATE TABLE
ON
    SCHEMA main.default
FROM
    `finance-team`
;
```

# 167-workspace-access-control-lists-ACLs.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/security/auth/access-control/ .)

## Introduction

There are different <u>Databricks workspace objects</u>.
They:

- are the assets that you interact with in your Databricks workspace

- are listed at the above-mentioned webpage

- include

  - notebooks

  - Lkeflow jobs

  - compute (clusters)

  - etc.



## How to grant privileges on <u>Databricks workspace objects</u>

Those assets are stored and secured
by <u>the Databricks workspace's own Access Control List (ACL) system</u>.

- grant
  permissions on each <u>Databricks workspace objects</u>
  to users or groups

- please don't confuse this with <u>Unity Catalog</u> <u>securable objects</u>

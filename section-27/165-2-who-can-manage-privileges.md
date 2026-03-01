# 165-2-who-can-manage-privileges.md

sources:

- https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/ ,
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/

---

Initially, users have no access to data in a «metastore».

Databricks «account admins», «workspace admins», and «metastore admins»
have default privileges for managing «Unity Catalog».
(For details, see `section-27/165-3-roles-in-the-databricks-account.md`.)

---

All «securable objects» in «Unity Catalog» have an «owner».

- Object «owners» have all privileges on that object,
  including the ability to grant privileges to other principals.

- «Owners» can grant other users the `MANAGE` privilege on the object,
  which allows users to manage privileges on the object.

Privileges can be granted by any of the following:

- A «metastore admin».
- A user with the `MANAGE` privilege on the object.
- The «owner» of the object.
- The «owner» of the «catalog» or «schema» that contains the object.

---

«Account admins» can also grant privileges directly on a «metastore».
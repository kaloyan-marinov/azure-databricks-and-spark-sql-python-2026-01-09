# 166-1-unity-catalog-s-permission-model-aka-privileges-on-securable-objects.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges .)



## Recall

«The securable objects» in «Unity Catalog» were listed in `section-27/161-2-the-unity-catalog-object-model.md`.

Essentially, they:

- are your "data assets" under «Unity Catalog» governance

- all live within a «metastore»



## «Unity Catalog»'s permission model

«The securable objects»:

- are subject to «Unity Catalog»'s permission model

- are at the «metastore» level,
  so they are not bound to a Databricks workspace

  - as a semi-concrete-but-hopefully-still-helpful example:
  
    - are independent of «Workspace Access Control»
      (which is discussed in `section-27/167-workspace-access-control-lists-ACLs.md`)

    - the permissions on a «securable object»
      are not linked to
      which Databricks workspace is used to access it

  - as a concrete example:

    - suppose you `GRANT` the `CREATE SCHEMA` privilege to a user in a «catalog»

    - the user has access to multiple Databricks workspaces

    - that «catalog» is available in [at least 2 of] those Databricks workspaces

    - then:
    
      - the privilege is not bound by the Databricks workspace;

      - the user can create a new «schema» in that «catalog»
        from any Databricks workspace they have access to;
        that «catalog» and «schema» will be available in all of the Databricks workspaces;


Different «securable objects» have different permission types.
The following table lists the privilege types
that apply to each «securable object» in «Unity Catalog».
https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges#privilege-types

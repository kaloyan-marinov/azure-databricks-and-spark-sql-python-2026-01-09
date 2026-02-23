# 166-1-unity-catalog-s-permission-model-aka-privileges-on-securable-objects.md

(A lot of this file comes from https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges .)



## Recall

<u>The securable objects</u> in <u>Unity Catalog</u> were listed in `section-27/161-2-the-unity-catalog-object-model.md`.

Essentially, they:

- are your data assets under <u>Unity Catalog</u> governance

- all live within a <u>metastore</u>



## <u>Unity Catalog</u>'s permission model

<u>The securable objects</u>:

- are subject to <u>Unity Catalog</u>'s permission model

- are at the <u>metastore</u> level,
  so they are not bound to a Databricks workspace

  - as a semi-concrete-but-hopefully-still-helpful example:
  
    - are independent of «Workspace Access Control»
      (which is discussed in `section-27/167-workspace-access-control-lists-ACLs.md`)

    - the permissions on a <u>securable object</u>
      are not linked to
      which Databricks workspace is used to access it

  - as a concrete example:

    - suppose you `GRANT` the `CREATE SCHEMA` privilege to a user in a <u>catalog</u>

    - the user has access to multiple Databricks workspaces

    - that <u>catalog</u> is available in [at least 2 of] those Databricks workspaces

    - then:
    
      - the privilege is not bound by the Databricks workspace;

      - the user can create a new <u>schema</u> in that <u>catalog</u>
        from any Databricks workspace they have access to;
        that <u>catalog</u> and <u>schema</u> will be available in all of the Databricks workspaces;


Different <u>securable objects</u> have different permission types.
The following table lists the privilege types
that apply to each <u>securable object</u> in <u>Unity Catalog</u>.
https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges#privilege-types


https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/

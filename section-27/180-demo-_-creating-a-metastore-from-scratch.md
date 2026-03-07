# 180-demo-_-creating-a-metastore-from-scratch.md



## Sources

- https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/create-metastore ,
  which is _approximately_ the same as
  https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore

  - those two are not "_essentially_ the same"

  - they help one draw some parallels between AWS and Azure:

    (a) what AWS calls an «S3 bucket»
        =
        what Azure calls a «storage container»
        (aka a «container in an ADLS account», aka a «container in an Azure storage account)
    
    (b) what AWS calls an «IAM role»
        =
        what Azure calls a «managed identity»



## Introductory remarks

- Recall that
  you can only have one «metastore» per region

- Technically, you don't need to create a «metastore»
  (b/c Databricks will automatically create one for you
  when you create your first «Databricks workspace» (in your chosen region))

- But it's good to be able to create a «metastore» in advance
  so you can configure it with your own «ADLS account»



## Preparation

Take steps 1, 2, and 3,
which are recorded in `section-27/179-3-2026-03-01-21-33-46-UTC-plus-1-.md`.



## Create a new «metastore»

Having logged in to the Databricks Account console as a user who has the «account admin» role,
click on «Catalog» and then «Create metastore».

- specify a name

- specify a region

- specify the «ADLS Gen 2 path» as the `abfss` path to the «container» in the «ADLS account»,
  both of which were created as part of the preceding section

- specify the «Access Connector Id» as the «Resource ID» of the «Access Connector for Azure Databricks» resource,
  which was created as part of the preceding section



When you click «Create»,
Databricks will automatically:

- create a «storage credential» (which references the specified «Access Connector Id»)

- create an «external location» (which references the specified «ADLS Gen 2 path»)



## Assign the newly-created «metastore» to at least 1 «Databricks workspace»

In the Azure Portal,
create a «Databricks workspace» in the same region as the newly-created «metastore»

In the Databricks Account console,
click on «Catalog»;
click on the newly-created «metastore»;
and assign it to the newly-created «Databricks workspace».

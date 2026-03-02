# 177-1-ADLS-Gen-2-set-up-and-data-upload.md

## Objective

To learn how to access external data from the Databricks environment.

Here, "external data" refers to files stored in an ADLS Gen 2 account.

## Make some preparations

> Recall that,
> back in the lecture titled `Introduction to Azure Data Lake Storage Gen 2`,
> we created an Azure Resource Group for this course
> and, within that, we provisioned a
> (a) «Databricks workspace» service
> and
> (b) an ADLS Gen 2 account with the `Hierarchical namespace` property enabled.
>
> e.g.
> ```
> rg-dataengineering-sandbox-westeurope
>
>     dbw-dataengineering-sandbox-westeurope-001    # Azure Databricks service
>     externalstorage17                             # Storage account
> ```

- Go to the storage account

- Click on `Data storage`

- Click on `Containers`

- Click on `Add container`

- Call it `population-data`

---

- In that container, create a folder called `country-data`

- Upload the `section-27/*-countries_population.snappy.parquet` file into that folder.
  (The file is attached in the course materials for this lecture.)

## Re-iterate the objective

The following lectures will show
how to enable the «Databricks workspace» to access the file,
which is present within the storage account.

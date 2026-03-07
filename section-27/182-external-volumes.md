# 182-external-volumes.md



## Sources

- https://docs.databricks.com/aws/en/volumes/
  which is _essentially_ the same as
  https://learn.microsoft.com/en-us/azure/databricks/volumes/



## Introduction

«Tables» and «volumes» are among the «securable object» types in «Unity Catalog».

Up until now, we have worked quite a bit with «tables».
As the name suggests,
they are intended to be used
when you need to work with (and govern) <u>tabular data</u> in «Unity Catalog».

«Volumes» represent a logical volume of storage in a cloud-based object store.
They govern <u>non-tabular data</u> of any format, including
- structured;
- semi-structured;
- unstructured.

Databricks recommends using «volumes» to govern access to all <u>non-tabular data</u>.



## Types of volumes

«Volumes» are available in two types:

- «Managed volumes»: For simple Databricks-managed storage

- «External volumes»: For adding governance to existing cloud object storage locations

  > essentially:
  >
  > - you're simply bringing a location from a cloud-based object store
  >   into the Databricks environment
  >
  > - you can then control access to the volume
  >   using the «Unity Catalog» permission model

They provide nearly identical experiences when using Databricks tools, UIs, and APIs.
The main differences are summarized in the following table
(wherein «Unity Catalog» is abbreviated as UC):

| feature           | «managed volumes»                                          | «external volumes»                                        |
| ----------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| storage location  | Created inside the UC-managed storage for the schema       | Registered against an existing cloud object storage path  |
| data lifecycle    | UC manages layout and deletion (7-day retention on delete) | Data remains in cloud storage when you drop the volume    |
| access control    | All access goes through UC                                 | UC governs access, but external tools can use direct URIs |
| migration needed? | No                                                         | No — use existing storage paths as-is                     |
| Typical use case  | Simplest option for Databricks-only workloads              | Access by both Databricks and external systems            |



## Why use «managed volumes»?

- Default choice for Databricks-only workloads.

- No need to manage cloud credentials or storage paths manually.

- Simplest option for creating governed storage locations quickly.



## Why use use «external volumes»?

- Adding governance where data already resides, without requiring a data copy.

- Governing files produced by other/external systems that must be ingested or accessed by Databricks.

- Governing data produced by Databricks that must be accessed directly from cloud object storage by other/external systems.

Databricks recommends using «external volumes» to store <u>non-tabular data</u> files
that are read or written by both Databricks and other/external systems.

> At the risk of stating the obvious:
>
> «Unity Catalog» does NOT govern reads and writes,
> which get performed directly against cloud object storage by external systems.
>
> Governing those
> is achieved by
> configuring additional policies and credentials directly in your cloud account
> (so as to ensure such data governance policies are respected outside Databricks).

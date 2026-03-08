# Introduction

This repository contains materials about «Azure Databricks».

«Azure Databricks» is an integration

- of a cloud-based platform for data processing,
  which is offered by a company called «Databricks, Inc.»

- with «Microsoft Azure»



# «Databricks, Inc.»

Before we dive into «Azure Databricks»,
it is very worthwhile to build a basic understanding of «Databricks, Inc.» as a company.

(The remainder of this file comes from https://en.wikipedia.org/wiki/Databricks .)



## The company at a glance

Databricks, Inc.:

- is an American privately-held software company based in San Francisco

- was founded in 2013 by the original creators of «Apache Spark»

- offers a cloud-based platform for data analytics and artificial intelligence

- developed the «data lakehouse» architecture,
  which combines elements of «data warehouses» and «data lakes»
  for managing structured data and unstructured data

  ---

  from a paper titled
  "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics":
  > "cloud data lakes, such as S3, ADLS and GCS"

  therefore, a cloud-based «data lake» is a cloud-based object store

  ---

- develops «Delta Lake»,
  an open-source project that adds «ACID transaction support» to «data lakes»

  ---

  > from
  > the paper cited above
  > and
  > an earlier paper titled "Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores"

  an open-source storage layer over cloud-based object stores, which:

  - was initially developed at Databricks

  - imbues/endows/provides a cloud-based object store
    with management and performance features,
    which are traditionally available only in analytical DBMSs;
    such features include but are not limited to:

    - ACID guarantees for transactions

    - query optimization

    - time travel

    - fast metadata operations
      (e.g., the ability to quickly search billions of table partitions for those relevant to a query)
    
    - etc.

  ---



## History

Databricks grew out of the «AMPLab project» at University of California, Berkeley
that was involved in building «Apache Spark»
(= an open-source distributed computing framework built atop Scala).



## Integrations

2017:
«Microsoft Azure» integrated Databricks as «Azure Databricks»

2024:
Databricks decided to run their products
on top of «AWS» via the new button called "Buy with AWS"

2025:
Databricks announced a partnership with «Google Cloud Platform»
to integrate its platform with Google Cloud services



## Products

Databricks, Inc. has created:

- a cloud data platform referred to as a «data lakehouse»

  - built on the open-source «Apache Spark» framework,
    enabling «analytical» queries on «semi-structured data»
    without requiring a traditional «database schema»

- «Databricks SQL» (previously called «SQL Analytics»)

  - for running business intelligence and analytics reporting
    on top of «data lakes»
    
  - enables analysts to
  
    - query datasets with standard SQL, or
    
    - use connectors to integrate with business intelligence tools
      (like Holistics, Tableau, Qlik, Sigma, Looker, and ThoughtSpot)

- a platform for other workloads, including

  - machine learning,
  
  - data storage and processing,
  
  - streaming analytics, and
  
  - business intelligence

- open-source projects
  that span data engineering, data science and machine learning

  - «Delta Lake»

  - MLflow

  - Koalas



## Remarks about the code within this repository

- within this repository,
  all code resides within the `section-26/nyctaxi_project/` folder

- take note of the commit, which wrote the current section of the `README.md` file

  - as of that commit,
    the above-mentioned code is an implementation of «Part 3 of the Project»

  - from that commit onwards,
    the above-mentioned code will be modified <u>in-place</u>
    so as to "grow into" an implemenation of «Part 4 of the Project»

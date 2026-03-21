# 00-10-data-warehouse.md



---



(https://www.databricks.com/glossary >> «Data Warehouse»)
redirects to
https://www.databricks.com/discover/data-warehouse

# What is a data warehouse?

A «data warehouse» is a data management system
that stores current and historical data from multiple sources
in a business-friendly manner for easier insights and reporting.

# variations of a data warehouse

From "less comprehensive" to "more comprehensive":

- «Operational data store» (ODS): A type of data warehouse that focuses on the latest operational or transactional data.

- «Data mart»: A simplified version of the data warehouse that serves a single line of business (LOB) or a single project. A data mart is smaller than an EDW, but the number of data marts typically grows as an organization grows, and LOBs want to self-service.

- «Enterprise data warehouse» (EDW): A centralized data warehouse that is used by many different teams in an organization. It is often the single source of truth for BI, analytics and reporting.

# What are «data warehouses» used for?

«Data warehouses» are used in "data applications" such as:

- BI,

- analytics,

- reporting,

- data applications,

- preparing data for machine learning,

- and data analysis

(to extract and summarize data from «operational databases»)



Data from «operational systems» (such as point-of-sale systems, inventory management systems, or marketing or sales databases) may:
- pass through an ODS
- require data cleansing to ensure data quality
- be uploaded to «data warehouses»



# What is «ETL» in a data warehouse?
 

A «data warehouse» requires data.

(That data must be loaded into the «data warehouse» (or referenced, with a concept called «lakehouse federation»).)

The process of
extracting data from source systems, transforming the data, and then loading the data into the «data warehouse»
is called «ETL» (extract, transform, load).
«ETL» is typically used for integrating structured data from multiple sources into a predefined schema.

(
«Query federation», which is sometimes also called «data virtualization», is a style of «ETL»
that is used to run queries against data sources from multiple sources and across multiple clouds.
You can view and query all the data from one place
without needing to migrate all data to a unified system.
)



# What is the difference between a «database» and a «data warehouse»?

A «database» (or a «database management system» (DBMS)) is a collection of structured data,
extending beyond text and numbers to images, videos and more.
A DBMS is the storage system for data that feeds applications and analytics.

A «data warehouse» is a structured repository
that provides data for business intelligence and analytics.
Data is cleansed, transformed and integrated into a schema that is optimized for querying and analysis
(including adding common aggregations).



# What data warehouse benefits can businesses expect?

- The consolidation of data obtained from many sources [into] a single point of access for all data

- Separate "analytics processing" from "transactional databases",
  improving the performance of both systems

- historical intelligence



# Challenges with data warehouses

- Limited to no support for unstructured data

- As data warehouses grow,
  they slow down — and in the cloud, that gets expensive quickly with cloud compute costs

  Commercial data warehouses charge you for storing your data, and also for analyzing it.
  Storage and compute costs are therefore still tightly coupled together.

- No support for AI and machine learning

  Data warehouses are purpose-built and optimized for common data warehouse workloads, including historical reporting, BI and querying —
  they were never designed for or intended to support machine learning workloads.

- SQL only

  Data warehouses typically offer no support for Python or R,
  the languages of choice for app developers, data scientists and machine learning engineers.
  


# Data warehouse architecture
 

A common model for a «data warehouse architecture» is multi-tiered.
This architecture was created by Bill Inmon,
the computer scientist often considered the father of the data warehouse.

- Bottom tier

  - is comprised of data sources and data storage;
  
  - includes data access methods
    (like APIs, gateways, ODBC, JDBC and OLE-DB)
    
  - includes «Data ingestion» or «ETL»

- Middle tier

  - is comprised of an OLAP server,
    which is either relational (ROLAP), or multi-dimensional (MOLAP), or a hybrid OLAP (HOLAP)

- Top tier

  - is comprised of the front-end clients
    (for querying, BI, dashboarding, reporting and analysis)



<u>TODO (2026/03/21, 11:26): "in its native format" and "raw data in its original format"</u>

<u>TODO (2026/03/21, 11:28): "a dimension" and "a fact"</u>



# types of data warehouses

- Traditional «data warehouse»:

  stores only structured data
  
  enables users to quickly and easily access data for reporting and analytics

- Intelligent «data warehouse» (aka modern «data warehouse»):

  is built on a lakehouse architecture
  
  has an intelligent and automatically optimizing platform
  
  not only provides access to AI and ML models
  but also uses AI to
  
  - assist with queries,
  - dashboard creation, and
  - performance and sizing optimization

# What solutions does Databricks have for data warehousing?

Databricks provides an intelligent «data warehouse», [Databricks SQL](
  https://www.databricks.com/product/databricks-sql
)

Databricks SQL is part of an integrated platform, Databricks' [Data Intelligence Platform](
  https://www.databricks.com/product/data-intelligence-platform
)



---



https://www.databricks.com/glossary/edw

<u>TODO (2026/03/21, 12:16): re-read `talk-by-andrew-ng-on-the-state-of-artificial-intelligence-AI/` and re-watch the talk</u>



# Context

The following terms will be used interchangeably:

- a company

- an organization (and an entire organization)

- a business

- an enterprise (and an entire enterprise)



The constituent parts of an enterprise will be called
by any one of the following names:

- business units

- departments

- functions

- business areas

(Examples include finance, operations, etc.)



# Glossary / Terminology / Vocabulary / Definitions

The term «Enterprise Data Warehouse» (EDW) is widely used in professional and technical contexts,
but you may encounter other similar-sounding terms,
such as «data warehouse» (DW) or «data warehousing» (DWH).

- Those terms are sometimes used interchangeably.

- Stricly speaking, those terms do not have the same meaning.

- Whenever someone uses the terms DW and/or DWH,
  you need more context to know for sure what they are talking about.

  As an extension of that point:
  
  Whenever someone uses the terms EDW, DW and/or DWH,
  it would be advisable to ask them to clarify what specific meaning they encapsulate within each of those terms.

---

A DW is
a storage system that
serves a single department.

---

An EDW is
a storage system that
brings together data from all of an enterprise's constituent departments.
(
In other words:
An EDW is
a centralized repository for all departments' data.
)

Its primary purpose is
to provide a single source of truth for
cross-functional "data-driven decision making".
(
In other words:
Its primary purpose is
to provide a single source of truth for
analyzing the past and forecasting the future in a cross-functional manner.
)

---

Be advised that that
the following phrases are synonyms or near-synonyms
of the phrase "data from all of an enterprise's constituent departments":

- [ used in https://www.databricks.com/blog/what-is-edw ]
  
  - multiple sources
  
  - disparate systems
  
  - data across a variety of departments
  
  - a wide range of sources
  
  - isolated silos
  
  - everyday business systems
  
  - systems that record business activities
  
  - source systems
  
  - data across multiple business areas
  
  - data across all departments
  
  - diverse enterprise systems

  - siloed systems

- [ used in https://www.databricks.com/discover/data-warehouse ]
  
  - various sources
  
  - many sources
  
  - dozens or even hundreds of individual data stores

Concrete examples of those include:

- [ as per https://www.databricks.com/blog/what-is-edw ]

  - customer relationship management (CRM) systems/platforms

  - enterprise resource planning (ERP) systems/platforms

  - transactional databases

  - software‑as‑a‑service (SaaS) applications

  - other operational databases

- [ as per https://www.databricks.com/discover/data-warehouse ]
  
  - operational systems such as point-of-sale systems, inventory management systems, or marketing or sales databases

  - operational data store[s]
```
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

(Examples include finance, operations, sales, etc.)



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




## Key characteristics of an EDW

By consolidating information into one system, an EDW ensures that executives, analysts and operational teams are working from the same definitions and datasets. This consistency is vital for accurate forecasting, regulatory compliance and strategic planning.

This helps ensure that insights reflect the full scope of business rather than isolated silos.

By enforcing standards and integrating data, an EDW allows all users — from executives to analysts —to work from the same vetted information.

They also support online analytical processing (OLAP), which is ideal for trend analysis and forecasting, as opposed to online transaction processing (OLTP) systems that handle day‑to‑day transactions.

EDWs organize data around key business subjects such as customers, products or sales. This subject focus makes analysis more intuitive and aligns the warehouse with how the business actually operates.



# How an EDW works = How an EDW operates = EDW operations

EDW operations involve an essentially continuous process that moves data
from «everyday business systems»
to a centralized environment.



There are different ways for realizing/implementing that process in practice:

- Extract-Transform-Load (ETL) + Analyze

  ---

  extract data from «everyday business systems»

  transform data

  load it in the EDW

  \+ analyze the finalized data

- Extract-Load-Transform (ELT) + Analyze

  ---

  extract data from «everyday business systems»

  load the raw data in the EDW

  within the EDW, transform the loaded raw data

  \+ analyze the finalized data



> (
>
> It is important to note that,
> regardless of the implementation,
> the process follows a clear, repeatable sequence.
>
> )



Last but not least,
let us clarify that "transform data" means the following:

- Data cleansing

  removing duplicates
  
  fixing errors

- Standardization

  enforcing consistent formats for dates, currencies, codes, etc.

  (application of "business" rules for)
  aligning data with "organizational" definitions

- Integration

  combining related data from multiple «everyday business systems»  



> (
>
> ETL is often considered the "traditional" approach.
> 
> However, many cloud platforms now often favor ELT,
> because
> 
> (a)
> on cloud platforms,
> storage and compute are separated,
> which makes it possible to scale each (of those resources) independently,
> 
> which causes
> 
> (b)
> on cloud platforms,
> ELT to be faster and more scalable.
>
> )



# How an EDW is architected

The classic EDW design is built on three tiers — bottom, middle and top — each serving a distinct purpose.

- The bottom tier

  This is considered the data integration layer, which is where raw data is captured and prepared for storage.
  
  ETL or ELT processes integrate data from «everyday business systems» and move it to the EDW.
  
  Modern data pipeline tools such as Fivetran, Airbyte and Matillion provide connectors to «everyday business systems».

- The middle tier

  is the actual storage layer (within the EDW itself) where processed data resides
  
  traditionally relied on relational databases optimized for "analytics";
  key techniques/features of such databases,
  which make analytical workloads efficient and scalable,
  include
  
    columnar storage (storing data by column rather than row for faster queries)
    
    compression (reducing storage size)
    
    partitioning (splitting data into manageable segments)

- The top tier

  is the query and presentation layer
  
  this is where users interact directly with the data
  to build dashboards and generate reports
  using
  
    various BI tools
    
    query engines with massively parallel processing
    
    APIs or
    
    user interfaces

Additionally, an EDW should be supplemented with a «governance layer», which
enables/provides strong security practices
and
thus helps achieve compliance with regulations (like GDPR or HIPAA)

- role‑based access controls

- metadata management

- column-level security or dynamic data masking (for highly sensitive data, such as personal identifiable information (PII))

- end‑to‑end encryption to protect data at rest and in transit

- audit logs that track every query and access event

- multi‑factor authentication (MFA) to help prevent unauthorized access

- regular security audits and compliance reviews

How data is modeled and organized inside an EDW can
dramatically improve query speed
and
make the EDW easier to navigate for non‑technical users.

- Most EDWs use «dimensional modeling»,
  which is designed to structure data for optimal query performance and user understanding
  using «fact tables» and «dimension tables».

  «Fact tables» store data for measurable transactions and events,
  such as sales revenue, order quantities or units sold.
  
  «Dimension tables» store data that provides descriptive context,
  such as customer location or age, order history and order dates.

- Data is also typically organized into schemas aligned to (!)business units(!) that reflect the (!)company(!)'s (!)operational structure(!). 

  This makes working with the data more intuitive for analysts and managers.
  (With data organized in «fact tables» and «dimension tables»,
  they can more easily conduct analysis activities
  such as comparing sales by region, product or customer segment.)



# Closing remarks

A «data mart» is a storage system, which:

- holds pre-aggregated data tailored to a specific department's needs

- addresses a single subject area or serves a single department

- is often sourced from an EDW

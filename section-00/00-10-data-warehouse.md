# 00-10-data-warehouse.md



## Sources

- https://www.databricks.com/glossary/edw

- <u>TODO (2026/03/21, 12:16): re-read `talk-by-andrew-ng-on-the-state-of-artificial-intelligence-AI/` and re-watch the talk</u>



## [WIP] Background

online analytical processing (OLAP), which is ideal for trend analysis and forecasting, as opposed to online transaction processing (OLTP) systems that handle day-to-day transactions.
- <u>TODO (2026/03/22, 11:31): re-read `introduction-to-the-parquet-file-format/2024-03-12-20-43-06-summary.txt`</u>
- <u>TODO (2026/03/22, 11:34): re-read`resources-about-database-normalization/2025-06-04-10-00-10-UTC-plus-2-database-normalization.txt`</u>



## Context

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

(Examples include finance, operations, sales, marketing, etc.)



## Glossary / Terminology / Vocabulary / Definitions

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

[Source for this paragraph: https://www.databricks.com/discover/data-warehouse ]
Its primary purpose is
to provide a single source of truth for
department-level "data-driven decision making".
Examples include but are not limited to:

- business intelligence (BI)

- analytics

- reporting

- "data applications"

- preparing data for machine learning

- data analysis

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

  - data sources

Concrete examples of those include:

- [ as per https://www.databricks.com/blog/what-is-edw ]

  - customer relationship management (CRM) systems/platforms

  - enterprise resource planning (ERP) systems/platforms

  - transactional databases

  - software-as-a-service (SaaS) applications

  - other operational databases

- [ as per https://www.databricks.com/discover/data-warehouse ]
  
  - operational systems such as point-of-sale systems, inventory management systems, or marketing or sales databases

  - operational data store[s]



## What does an EDW "do"?

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

  (application of "business rules" for)
  aligning data with "organizational definitions"

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



> (
>
> [Source for this parenthetical remark: https://www.databricks.com/discover/data-warehouse ]
>
> «Query federation», which is sometimes also called «data virtualization», is a style of «ETL»
> that is used to run queries against multiple data sources and across multiple clouds
> without needing to migrate all data to a unified system.
>
> [«Lakehouse Federation»](https://docs.databricks.com/aws/en/query-federation)
> is the «query federation» sub-system within Databricks.
> It makes it possible to connect to the following data sources:
> - another «Databricks workspace»
> - MySQL
> - PostgreSQL
> - Microsoft SQL Server
> - Oracle
> - Snowflake
> - Google BigQuery
> - Amazon Redshift
> - Azure Synapse (SQL Data Warehouse)
> - Salesforce Data 360
> - Teradata
>
> )



## Why would an enterprise build/implement an EDW?

This section explains what benefits an enterprise can expect to reap from implementing/building an EDW.

- single source of truth for
  analyzing the past and forecasting the future

    - enables all users - from executives to analysts - to work from the same vetted information

    - improves confidence and trust data outputs for the entire enterprise

- improved data quality and consistency

    - cf. "Data cleansing" above

    - cf. "Standardization" above

- [Source for this point: https://www.databricks.com/discover/data-warehouse ] (!)Separate "analytics processing" from "transactional databases",
  improving the performance of both systems(!)

- enhanced BI

    - i.e. analyzing the past and forecasting the future in a cross-functional manner

      insights reflect the full scope of (!)business(!)
      (rather than different (and possibly isolated) departments' «everyday business systems»)

    - is made possible by «self-service analytics»,
      which in turn is made possible by an EDW

      «self-service analytics» consists in
      enabling users to explore the data within an EDW (!)independently(!) without having to rely on IT support

- support for ML and AI

    - by construction, an EDW contains high-quality, consistent historical data;
      that data can be utilized for machine learning applications
      (e.g. to train models for forecasting demand, predicting customer churn or detecting fraud)



## How is an EDW architected? What components is it made up of?

A common architecture for an EDW is a multi-tiered one,
with each layer serving a distinct purpose.

- The bottom tier

  - this is the data ingestion layer

  - this is where ETL or ELT processes are run
  
  > (
  >
  > Modern data pipeline tools such as Fivetran, Airbyte and Matillion
  > provide connectors to «everyday business systems».
  >
  > )

- The middle tier

  - this is the actual storage layer (within the EDW itself)
    where *"ELT-processed"* data resides
  
  - traditionally, it relied on relational databases optimized for "analytics"
    (aka an OLAP server,
    which is either relational (ROLAP), or multi-dimensional (MOLAP), or a hybrid OLAP (HOLAP));
    key techniques/features of such databases,
    which make (!)analytical workloads(!) efficient and scalable,
    include
  
    - columnar storage (storing data by column rather than row for faster queries)
    
    - compression (reducing storage size)
    
    - partitioning (splitting data into manageable segments)

- The top tier

  - this is the query and presentation layer
  
  - this is where users interact directly with the data
    to build dashboards and generate reports
    using
  
    - various BI tools
    
    - query engines with massively parallel processing
    
    - APIs or
    
    - user interfaces

> (
>
> [Source for this parenthetical remark: https://www.databricks.com/discover/data-warehouse ]
>
> This architecture was created by Bill Inmon,
> the computer scientist often considered the father of the DW.
>
> )

> (
>
> [Source for this parenthetical remark: https://www.databricks.com/discover/data-warehouse ]
>
> What is the difference between a «database» and a DW?
> 
> - A «database» (or a «database management system» (DBMS)) is a collection of structured data,
>   extending beyond text and numbers to images, videos and more.
>   A DBMS is the storage system for data that feeds applications and analytics.
> 
> - A DW is a structured repository
>   that provides data for business intelligence and analytics.
>   Data is cleansed, transformed and integrated into a schema that is optimized for querying and analysis
>   (including adding common aggregations).
>
> )

Additionally:

- an EDW should be supplemented with a «governance layer», which
  enables/provides strong security practices
  and
  thus helps achieve regulatory compliance
  (for example, with GDPR or HIPAA)

- how data is modeled and organized inside an EDW can
  dramatically improve query speed
  and
  make the EDW easier to navigate for non-technical users



## Implementation considerations

Implementing/building an EDW is a significant undertaking in terms of
(a) technical complexity,
(b) timelines, and
(c) coordination across multiple teams.

The remainder of this section provides practical steps for success.

- Best practices:

  - an enterprise must define "business rules"
    <u>before</u> before implementing the "T" in ELT or ETL;
    (recall the "improved data quality and consistency" sub-section mentioned earlier)

    (!)Continuous monitoring (with alerts for anomalies) helps maintain quality over time.(!)

  - As enterprises grow,
    data volumes inevitably expand.

    An EDW should be designed from the beginning with this growth in mind.

  - (!)Because EDWs concentrate so much sensitive information in one place(!),
    it is essential for it to be supplemented with a «governance layer»
    (which was mentioned above)

    it should be used to implement these strong security practices:
    
    - role-based access controls
      that follow [the Principle of Least Privilege](
        https://en.wikipedia.org/wiki/Principle_of_least_privilege
      )

    - metadata management

    - column-level security or dynamic data masking (for highly sensitive data, such as personal identifiable information (PII))

    - end-to-end encryption to protect data at rest and in transit

    - audit logs that track every query and access event

    - multi-factor authentication (MFA) to help prevent unauthorized access

    - regular security audits and compliance reviews

  - pay careful attention to how data is modeled and organized inside an EDW

    - Most EDWs use «dimensional modeling»,
      which is designed to structure data for optimal query performance and user understanding
      using «fact tables» and «dimension tables».

      «Fact tables» store data for measurable transactions and events,
      such as sales revenue, order quantities or units sold.
      
      «Dimension tables» store data that provides descriptive context,
      such as customer location or age, order history and order dates.

    - Data is also typically organized into schemas aligned to (!)business units(!) that reflect the (!)company(!)'s (!)operational structure(!). 

      This makes working with the data more intuitive for all users - from executives to analysts.
      (With data organized in «fact tables» and «dimension tables»,
      they can more easily conduct analysis activities
      such as comparing sales by region, product or customer segment.)

      (!)EDWs organize data around key business subjects such as customers, products or sales. This subject focus makes analysis more intuitive and aligns the warehouse with how the business actually operates.(!)

- Approaches to overcoming common adoption challenges:

  | Row # | Challenge | Solution |
  | - | - | - |
  | 1 | Depending on how they are deployed, EDW projects can take from one to five years to fully deploy. | While that may seem daunting, a phased approach will help manage expectations and sustain progress. Start with a high-value use case, such as sales reporting, to demonstrate ROI and expand from there. |
  | 2 | Change management is another significant challenge if users are resistant to new tools or processes. | Invest in training, secure and communicate executive-level sponsorship and celebrate early wins to build momentum. |
  | 3 | Data integration is often complex because organizations rely on many systems. | Modern data pipeline tools (like the ones mentioned above) simplify this work, and teams should prioritize the most important sources first. |
  | 4 | Cost concerns can slow adoption. | Cloud platforms offer a lower entry point, and demonstrating early ROI helps justify continued investment. |



## Conclusion

Implementing/building an EDW is a significant undertaking.

Doing that successfully requires
both coordination across multiple teams
and realistic expectations.

If done successfully,
an EDW can be a strategic asset
that helps (!)organizations(!) turn data into valuable insights.



## Miscellaneous remarks

A «data mart» is a storage system, which:

- holds pre-aggregated data tailored to a specific department's needs

- addresses a single subject area or serves a single department

- is often sourced from an EDW



Possible deployment environments for an EDW:

- cloud-based approach

  - flexibility

  - lower upfront costs

    shift spending
    from «capital expenditures» to «operating expenditures»,
    making costs more predictable
    and
    enabling enterprises to adapt quickly to changing data demands with large infrastructure investments

  - deployment is typically faster than other options
    (and is often completed in 6 to 12 months)

- on-premises approach
  
  (= within an enterprise's own data centers)

  - agility and scalability are often limited,
    which can slow innovation and adaptation to change
  
  - costs are generally higher than other approaches
  
    upfront investment ranging from $500,000 to more than $5 million,
    plus ongoing maintenance
  
  - deployments have long timelines
    (often lasting a year and sometimes as many as 5)
  
  - provides maximum control over infrastructure and data
  
    so it is well-suited to meeting strict compliance or sovereignty requirements

    some enterprises are bound by regulatory requirements to use on-premises storage;
    and those with existing infrastructure investments may also find the on-premises approach to be the most practical;

- hybrid approach

  - For example,

    (a)
    sensitive data can be stored on-premises
    to achieve regulatory compliance, while
    
    (b)
    cloud platforms handle (!)analytical workloads(!)
  
  - may require integration across environments,
    which can introduce complexity
    (that makes operations and management of your EDW more difficult)
  
  - typically best-suited for:
  
    - enterprises that are transitioning from legacy systems to cloud;
    
    - enterprises that need both "data sovereignty" and scalability;



> (
>
> [Source for this parenthetical remark: https://www.databricks.com/discover/data-warehouse ]
>
> Challenges with DWs
> 
> - Limited to no support for unstructured data
> 
> - As DWs grow,
>   they slow down — and in the cloud, that gets expensive quickly with cloud compute costs
> 
>   Commercial DWs charge you for storing your data, and also for analyzing it.
>   Storage and compute costs are therefore still tightly coupled together.
> 
> - No support for AI and machine learning
> 
>   DWs are purpose-built and optimized for common (!)DW workloads(!) (including historical reporting, BI and querying);
>   they were never designed for or intended to support (!)machine learning workloads(!).
> 
> - SQL only
> 
>   DWs typically offer no support for Python or R,
>   the languages of choice for app developers, data scientists and machine learning engineers.
>
> )



[Source for this paragraph: https://www.databricks.com/discover/data-warehouse ]
A «data lakehouse» is a platform for data processing:

- whose architecture combines the benefits of a DW and a «data lake»

- which

  - both allows for the storage of raw data in its original format (like a «data lake» does)
  
  - and provides data processing and analytics capabilities like a DW



> (
>
> [Source for this parenthetical remark: https://www.databricks.com/discover/data-warehouse ]
>
> - types of data warehouses
> 
>   - Traditional «data warehouse»:
> 
>     stores only structured data
>     
>     enables users to quickly and easily access data for reporting and analytics
> 
>   - Intelligent «data warehouse» (aka modern «data warehouse»):
> 
>     is built on a «lakehouse architecture»
>     
>     has an intelligent and automatically optimizing platform
>     
>     not only provides access to AI and ML models
>     but also uses AI to
>     
>     - assist with queries,
>     - dashboard creation, and
>     - performance and sizing optimization
> 
> - What solutions does Databricks have for data warehousing?
> 
>   - Databricks provides an intelligent «data warehouse», [Databricks SQL](
>       https://www.databricks.com/product/databricks-sql
>     )
> 
>   - Databricks SQL is part of an integrated platform, Databricks' [Data Intelligence Platform](
>       https://www.databricks.com/product/data-intelligence-platform
>     )
>
> )
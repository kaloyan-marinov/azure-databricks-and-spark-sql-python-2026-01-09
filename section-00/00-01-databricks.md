# section-00/00-1-databricks.md

## Source

- https://docs.databricks.com/aws/en/introduction/

- https://learn.microsoft.com/en-us/azure/databricks/introduction/

- those webpages have identical contents;
  the only difference is that
  (relevant) occurrences of "Databricks" in the former
  are replaced with
  "Azure Databricks" in the latter

## The «Databricks Data Intelligence Platform»

It is worthwhile to re-read (`./README.md` >> the `Introduction` section).

Databricks:

- is
  a cloud-based platform for processing <u>enterprise-grade</u> data
  <u>at scale</u>

- integrates with cloud storage and security in your cloud account

- manages and deploys cloud infrastructure for you

## «Databricks, Inc.» is committed to the open-source community

The following technologies are open-source projects,
which were originally created by «Databricks, Inc.» employees:

- «Apache Spark» and «Structured Streaming»

- «Delta Lake» and «Delta Sharing»

- «Unity Catalog»

- «MLflow»

- «Redash»

«Databricks, Inc.» manages updates of open-source integrations with releases of the «Databricks Runtime».

## Common use cases

The following use cases highlight
some of the ways customers use Databricks
to accomplish tasks essential to storing, processing, and analyzing data
(that drives critical business functions and decisions).

- Build an enterprise «data lakehouse»

  can serve as the single source of truth
  
  (
  for data engineers, data scientists, analysts, and production systems,

  providing access to consistent data
  and
  reducing the complexities of building, maintaining, and syncing many distributed data systems
                                                                  [= the multiple systems' data]
  )

- ETL and data engineering

  «data engineering» provides the backbone for data-centric companies by making sure data is available, clean, and stored in data models for efficient discovery and use

  Databricks combines the power of «Apache Spark» and «Delta Lake» and custom tools to make it possible to:
  - compose ETL logic (implemented in SQL, Python, and Scala), and
  - orchestrate scheduled job deployment with a few clicks

- «Data governance» and secure data sharing

  > «Data governance» is a framework of policies, processes, roles, and technical controls that ensures your organization's data is secure, trustworthy, and used responsibly throughout its lifecycle. Effective data governance enables you to maintain data quality, protect sensitive information, meet regulatory requirements, and maximize the value of your data assets.

  «Unity Catalog» provides a unified «data governance» model for the «data lakehouse».

  - «Cloud administrators» configure and integrate coarse access control permissions for «Unity Catalog», and then
  
  - «Databricks administrators» can manage permissions for teams and individuals.

  - Privileges are managed with access control lists (ACLs)
    through:
    - either user-friendly UIs, or
    - SQL syntax.

  [That] makes data sharing within your organization as simple as
  granting query access to a table or view.

- DevOps, CI/CD, and task orchestration

  - «Jobs» schedule Databricks notebooks, SQL queries, and other arbitrary code.
  
  - «Databricks Asset Bundles» allow you to define, deploy, and run Databricks resources such as jobs and pipelines programmatically.
  
  - «Git folders» let you sync Databricks projects with a number of popular Git providers.

  For CI/CD best practices and recommendations, see [Best practices and recommended CI/CD workflows on Databricks](
    https://docs.databricks.com/aws/en/dev-tools/ci-cd/best-practices
  ).
  
  For a complete overview of tools for developers, see [Develop on Databricks](
    https://docs.databricks.com/aws/en/developers/
  ).

---

- Data warehousing, analytics, and BI

  Administrators configure scalable compute clusters as «SQL warehouses»,
  allowing «end users» to execute queries
  without worrying about any of the complexities of working in the cloud.

  «SQL users» can run queries:
  - using «the SQL query editor», or
  - in notebooks (which support Python, R, Scala, SQL)

---

- Real-time and streaming analytics

  Databricks leverages «Apache Spark Structured Streaming»
  to work with streaming data and incremental data changes.

- Online transactional processing

  «Lakebase»:
  
  - is an online transactional processing (OLTP) database
    that is fully integrated with the Databricks

  - is a fully managed Postgres database

  - allows you to create and manage OLTP databases stored in Databricks-managed storage

---

- Machine learning, AI, and data science

  The «Databricks Runtime for Machine Learning» includes libraries
  that allow you
  to integrate existing pre-trained models (or other open source libraries) into your workflow.

## Further reading - intriguing but not urgent

https://docs.databricks.com/aws/en/developers/

https://docs.databricks.com/aws/en/dev-tools/ci-cd/best-practices

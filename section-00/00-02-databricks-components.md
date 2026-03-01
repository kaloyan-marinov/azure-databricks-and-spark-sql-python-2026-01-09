# 00-02-databricks-components.md

## Accounts and workspaces

source:
https://docs.databricks.com/aws/en/getting-started/concepts

A «Databricks workspace» is
a Databricks deployment in the cloud
that functions as an environment for your team to access data-and-AI «securable objects».
(Your organization can choose to have either multiple workspaces or just one,
depending on its needs.)

A «Databricks account» represents a single entity
that can include multiple «Databricks workspaces».
(A «Databricks account» enabled for «Unity Catalog»
can be used to manage users and their access to data
centrally across all of the «Databricks workspaces» in said account.)

## Identities

source:
https://docs.databricks.com/aws/en/admin/users-groups/

Databricks supports three «Databricks identities»
for authentication and access control:

- «Users»

  This is represented by an email address.

- «Service principals»

  This is intended to be used with
  - jobs,
  - automated tools, and
  - systems such as scripts, apps, and CI/CD platforms.

- «Groups»

  This plays an auxiliary but important role in that
  it makes easier (and streamlines) the task of managing access to «securable objects».

## «Securable objects» and «access control systems»

source:
https://docs.databricks.com/aws/en/security/auth/

In Databricks,
there are different types of «securable objects»
and, for each type, there is different «access control system».

| type of «securable objects»         | «access control system»           |
| ----------------------------------- | --------------------------------- |
| workspace-level «securable objects» | Access control lists (ACLs)       |
| account-level «securable objects»   | Account role based access control |
| data-and-AI «securable objects»     | «Unity Catalog»                   |

## Revisit «Databricks workspaces»

source:
https://docs.databricks.com/aws/en/getting-started/concepts

A «Databricks workspace» is an environment, which:

- organizes workspace-level «securable objects»
  (such as Notebooks, libraries, dashboards, and experiments)
  into folders

- provides access
  to computational resources
  and
  to data-and-AI «securable objects»

## Data engineering

source:
https://docs.databricks.com/aws/en/getting-started/concepts

- «Databricks workspace»

- «Git folder»

## Computation management

source:
https://docs.databricks.com/aws/en/getting-started/concepts

- Cluster

  - a set of computation resources and configurations
    on which you run Notebooks and Jobs

  - There are two types of clusters:

    - «all-purpose clusters»

      [aka "data-analytics clusters"]

    - «job clusters»

      [aka "data-engineering clusters"]

- «Databricks Runtime»

  - the set of core components
    that run on the «clusters» managed by Databricks

  - there exist the following runtimes:

    - «Databricks Runtime»
    
      includes «Apache Spark»
      
      but also adds a number of components and updates
      that improve the usability, performance, and security of "big data analytics"
    
    - «Databricks Runtime for Machine Learning»
    
      is built on «Databricks Runtime»
      
      and provides prebuilt machine learning infrastructure
      that is integrated with all of the capabilities of the «Databricks workspace»
      
      It contains multiple popular libraries,
      including TensorFlow, Keras, PyTorch, and XGBoost.

- Jobs

  a non-interactive mechanism for orchestrating and scheduling workflows

- Lakeflow Spark Declarative Pipelines

  a declarative framework
  for building reliable, maintainable, and testable data-processing pipelines

- Workload

  the amount of processing capability needed to perform a task or group of tasks

## Data management

source:
https://docs.databricks.com/aws/en/getting-started/concepts

- «Unity Catalog»

  ---

  ( as per https://docs.databricks.com/aws/en/data-governance/unity-catalog/ )

  a unified/centralized «data governance» solution on Databricks,
  which (a) is comprised of

  (a.1) a catalog of data-and-AI «securable objects»

  (a.2) related capabilities for
    - access control
    - auditing
    - lineage
    - quality monitoring
    - discovery (of data-and-AI «securable objects»)

  and which (b) spans your «Databricks workspaces»

  ---

  ( as per https://docs.databricks.com/aws/en/data-governance/ )

  - is open-source (cf. https://www.unitycatalog.io/ )

  - supports multiple platforms

  - is deeply integrated into Databricks

- «metastore»

  A «metastore» is a top-level container (within "the «Unity Catalog» object model"),
  whose purpose is to register:

  (a) «securable objects» (including but not limited to data-and-AI «securable objects») plus metadata about those, and

  (b) the permissions that govern access to those assets.

  The contents of a «metastore»
  are organized in a 3-level hierarchy.

    - «catalogs» that contain «schemas» (aka «databases»),
      which in turn contain data-and-AI «securable objects», like «tables», «volumes», etc.
      
    - This hierarchy is represented as a namespace,
      which is comprised of levels (e.g. `catalog.schema.table`).

- «Delta tables»

  By default, all tables created in Databricks are «Delta tables». 

  «Delta tables» are based on the «Delta Lake» open source project,
  a framework for high-performance ACID table storage over cloud object stores.
  A «Delta table» stores data as a directory of files on cloud object storage
  and
  registers table metadata to the «metastore» (within a «catalog» and «schema»).

## Data warehousing

source:
https://docs.databricks.com/aws/en/getting-started/concepts

- Query

  a valid SQL statement that allows you to interact with your data

- «SQL warehouse»

  a computation resource on which you run SQL queries

- Query history

  a list of executed queries and their performance characteristics

- etc.

## AI and machine learning

source:
https://docs.databricks.com/aws/en/getting-started/concepts

- ...
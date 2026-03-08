# 183-3-overview-of-part-4.md



## Introduction

This is Part 4 of the Project.
This is also its final phase.



## The premise

Imagine that:

- everything, which has been built in the Project so far,
  was built by Team A at some company

- you are part of Team A

- Team B is another team at the same company
  and
  they have submitted a requirement to Team A

---

Requirement:

Team B asks for an export of the `nyctaxi.02_silver.yellow_trips_enriched` table. That export should be:

- delivered into Team B's ADLS Gen 2 account

  - the account is named `nyctaxistorage<suffix-to-make-its-name-unique>`

  - within that account, there is a container called `nyctaxi-yellow`

  - within the container, there is a folder called `nyctaxi_yellow_export/`

- in the JSON format

- partitioned by «vendor» and «month»



## Breakdown of Part 4 of the Project into stages

What we will build.

1. Simulate the existence of Team B and, more specifically, of their ADLS Gen 2 account and container

2. Link Team B's container to Team A's «Databricks workspace»
   (by creating a «Storage Credential» and «External Location»
   within Team A's «Databricks workspace»)

3. Team A will create a new schema `nyctaxi.04_export`
   and
   an «external table» backed by the data files written into Team B's container
   
   The motivation/justification/rationale for that is
   to enable Team A to:

   - browse, query, and manage access (from within their own «Databricks workspace»)
   
   - perform analysis, data quality checks, and monitoring activities
     directly on the data files

4. Export job/notebook:

   To our project code we'll add a notebook task to our `nyctaxi_job` that will upload the JSON files to the location every time the pipeline runs, which is once a month. We'll register an external table that points to the location so we can append the data to the location each time

5. One off scripts:

   We will also create initial load scripts to load historical data

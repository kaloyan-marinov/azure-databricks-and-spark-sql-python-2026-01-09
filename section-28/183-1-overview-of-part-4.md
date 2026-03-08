# 183-1-overview-of-part-4.md



## Introduction

This is Part 4 of the Project.
This is also its final phase.



## The premise

Imagine that
you have received a requirement from another team.

---

Requirement:

A data team has asked for an export of the `yellow_trips_enriched` (silver) table, partitioned by «vendor» and «month», delivered as «JSON» into «their» Azure Data Lake Storage account. They cannot accept data outside their account.

Objective:

Deliver a partitioned JSON export of yellow_trips_enriched every month into their ADLS Gen 2 account named `nyctaxistorage (or similar)`, container `nyctaxi-yellow`, under the folder `nyctaxi_yellow_export/`.

What we will build.

1. Azure storage.

   We'll create and ADLS Gen 2 account named `nyctaxistorage (or similar)` with container `nyctaxi-yellow` to simulate the account that the data team would have.

2. Unity Catalog linkage.

   We'll link this location to Databricks via a «Storage Credential» and «External Location» that point to the container.

3. Export schema & objects.

   In our nyctaxi catalog we'll create a new schema `04_export`, and an «external table» over the export part so that our internal Databricks engineers can browser, query, and manage access from within Databricks.

4. Export job/notebook:

   To our project code we'll add a notebook task to our `nyctaxi_job` that will upload the JSON files to the location every time the pipeline runs, which is once a month. We'll register an external table that points to the location so we can append the data to the location each time

5. One off scripts:

   We will also create initial load scripts to load historical data

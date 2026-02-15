# 133-20-overview-of-part-2.md



## Recall

At present, our project can handle an initial upload of data.

Given an input list of dates,
it then overwrites this data in each layer of our data lakehouse.

This is a useful scenario for:

- an initial data loading, or

- performing a full re-write of our data



## The Focus of Part 2 of the Project

To modify our code so we can
process the Yellow Trip Data incrementally
and
apply Slowly Changing Dimensions Type 2 to the Taxi Zone Lookup table.

Specifically,
we are going to make it possible to process 1 month of data at a time, in an incremental fashion.



## IMPORTANT: understand the specifics of the original data source

As noted on [the NYC Taxi and Limousine Commission's website](
    https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
):
> Trip data is published monthly on this website,
> typically with a two-month delay to allow time for full vendor submissions.



## Implication/Requirement for Part 2 of the Project

Pick up the Yellow Taxi Data 2 months prior to the current date
and
load that data file to the landing volume
(at `/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/<yyyy-mm>`)

Overwrite the existing `/Volumes/nyctaxi/00_landing/data_sources/lookup/taxi_zone_lookup.csv`
with the file from the TLC Trip Record data portal
(to ensure that we have the latest mapping available for the bronze-layer processing.)



For the bronze-layer processing,
we will read the latest available month's PARQUET file from `/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/`
and
_append_ that into the `nyctaxi.01_bronze.yellow_trips_raw` table.



We will then take the most recent available month's data from the bronze table,
clean it,
and append it to the `nyctaxi.02_silver.yellow_trips_cleansed` table.

For the `nyctaxi.02_silver.taxi_zone_lookup`,
we will implement SCD Type 2.

... (achieve incremental processing by appending)



## Finally

We'll create a Databricks `Job`.

This will consist of Notebook `Task`s and basic control-flow checks.

- Each of the Notebook `Task`s processes
  one of the tables in the architecture depicted in `133-10-nyctaxi_project_architecture_part_2.drawio`.

- E.g. if we've already processed the data for the most recent available month,
  then the `Job` should not process the same data again.



The `Job` we create will be able to run every month on a schedule.

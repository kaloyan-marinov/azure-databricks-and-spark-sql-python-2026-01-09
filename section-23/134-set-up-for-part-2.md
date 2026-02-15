# 134-set-up-for-part-2.md



## Introduction

The purpose of this lecture is to prepare both the codebase and the data
before [properly] starting the next part of the project [for real].



## Preparation

For the lecturer:
> The current month for me would be August.
> Two months prior to that would be June.
> So I will be incrementally processing the data for June 2025.



1) re-arrange our `/Workspace/Shared/nyctaxi_project/` folder

```shell
# from `100-exploratory-data-analysis.md`

Workspace/
    Shared/
        nyc_taxi_project/
            transformations/        
                notebooks/
                    01_bronze/      
                    02_silver/      
                    03_gold/        
            one_off/                
                                    
                                    
            ad_hoc/                 # this folder is where we can perform basic ad-hoc analysis
```

```shell
# clone

Workspace/
    Shared/
        nyc_taxi_project/
            transformations/        
                notebooks/

# to

Workspace/
    Shared/
        nyc_taxi_project/
            one_off/        
                initial_load/
                    notebooks/
```

Recall that the logic in Part 1 of the Project used `mode="overwrite"` as the basis for its writes.

```shell
Workspace/
    Shared/
        nyc_taxi_project/
            one_off/        
                initial_load/
                    notebooks/
                        00_landing/   # create this folder
                        01_bronze/
                        02_silver/
                        03_gold/
```

Move each of
`/Workspace/Shared/nyctaxi_project/one_off/2026-01-17 16:26:00 backfill_historical_yellow_trips`
and
`/Workspace/Shared/nyctaxi_project/one_off/2026-01-17 16:40:45 load_taxi_zone_lookup`
to
`/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/00_landing/`



At this point, let's summarize that

(a) `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/`
    contains all of the logic we used in Part 1 of the Project
    to process 6 months' worth of data
    into our lakehouse

(b) `/Workspace/Shared/nyctaxi_project/transformations/notebooks/`
    still has the original code as well



2) make preparations in the `/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/`

To demonstrate the full flow again,
delete all subfolders:
```
/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/
    2025-01/
    2025-02/
    2025-03/
    2025-04/
    2025-05/
    2025-06/
```

We will perform an initial fresh load so that
we have 6 months' worth of data, up to 3 months prior to the current date that you're watching this video,
which for the lecturer would be May 2025.

This will allow us to demonstrate
how our updated data pipeline will incrementally process data for 2 months prior to the current date.



3) Update `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/00_landing/2026-01-17 16:26:00 backfill_historical_yellow_trips`

Change the value assigned to the `dates_to_process` variable.
and then
run the notebook.



4) Run each of these notebooks in the indicated order:

```
/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/01_bronze/2026-01-17 16:52:09 yellow_trips_raw

/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/02_silver/2026-01-18 10:33:21 yellow_trips_cleansed
/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/02_silver/2026-01-18 11:37:00 yellow_trips_enriched

/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/03_gold/2026-01-18 11:57:54 daily_trips_summary
```



## Verify whether we have indeed loaded and processed data for 6 months up to 3 months prior the current date

```python
import pyspark.sql.functions as sf

df = (
    spark
    .read
    .table(
        'nyctaxi.02_silver.yellow_trips_cleansed',
    )
    .agg(
        sf.min('tpep_pickup_datetime'),
        sf.max('tpep_pickup_datetime'),
    )
)
```

```python
df.display()

# min(tpep_pickup_datetime)     max(tpep_pickup_datetime)
#
# 2024-12-01T00:00:00.000       2025-05-31T23:59:58.000
```

```python
# fmt: off
'''
May is 3 months prior the current date at the time when the lecturer recorded the video `134-set-up-for-part-2.md`.

We are yet to process the data from 2 months ago (relative to the above-mentioned time).

W
'''
# fmt: on
```



## Conclusion

With this initial load in place for Part 2 of the Project,
we'll create an automated pipeline
which will process 1 month's worth of data per run.

It will always target the dataset from 2 months ago.
(
Relative to the time when the lecturer recorded the video `134-set-up-for-part-2.md`,
that would be the 2025/06 dataset.
)

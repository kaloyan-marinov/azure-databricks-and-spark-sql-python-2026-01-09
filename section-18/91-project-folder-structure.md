# 91-project-folder-structure.md



In this lecture,
we are going to set up the folder structure that we'll use for the course project.

The goal here is
    clarity,
    scalability, and
    clear separation of responsibility -
particularly, as we transition
from notebooks
to production-ready scripts
later on in this course.

Let's start by creating the root project folder:

```shell
Workspace/
    Shared/
        nyc_taxi_project/
            transformations/        # all of the core data-transformation logic
                notebooks/
                    01_bronze/      # ingest the raw files into the bronze layer
                    02_silver/      # clean and enrich the data in the silver layer
                    03_gold/        # perform aggregations & perform business-ready tables in the gold layer
            one_off/                # ad-hoc tasks (e.g. creating our Databricks catalogs, schemas for the project, loading historical files, performing manual backfills);
                                    # the scripts and notebooks in this folder are NOT part of the recurring batch-processing pipeline,
                                    # BUT they're essential during set-up and special operations
```

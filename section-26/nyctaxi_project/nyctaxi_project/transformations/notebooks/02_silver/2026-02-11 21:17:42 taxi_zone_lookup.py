# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC This notebook:
# MAGIC
# MAGIC - aims to implement «Slowly Changing Dimensions Type 2» for the Taxi Zone Lookup table
# MAGIC
# MAGIC - is very similar to `/Workspace/Shared/nyctaxi_project/one_off/initial_load/notebooks/02_silver/2026-01-17 17:01:42 taxi_zone_lookup`

# COMMAND ----------

import datetime

from delta.tables import DeltaTable

# COMMAND ----------

from pyspark.sql.functions import (
    col,
    current_timestamp,
    lit,
)
from pyspark.sql.types import (
    IntegerType,
    TimestampType,
)

# COMMAND ----------

df = spark.read.load(
    '/Volumes/nyctaxi/00_landing/data_sources/lookup/taxi_zone_lookup.csv',
    format='csv',
    header=True,
)

# COMMAND ----------

# Each of the following statements demonstrates that
# all of the columns are of the `string` type.

# df.display()

df.dtypes

# COMMAND ----------

df_1 = df.select(
    col('LocationID').cast(IntegerType()).alias('location_id'),
    col('Borough').alias('borough'),
    col('Zone').alias('zone'),
    col('service_zone'),
    current_timestamp().alias('effective_date'),
    lit(None).cast(TimestampType()).alias('end_date'),
)

# COMMAND ----------

# df_1.display()

# COMMAND ----------

# NB:
# This cell should NOT be included in the final project code.
#
# Q:
# Why is this cell included here then?
#
# A:
# For teaching purposes,
# i.e.
# to demonstrate/prove the correctness of how «Slowly-Changing Dimensions Type 2» is implemented.

from pyspark.sql.functions import (
    when,
)

# fmt: off
'''
# Update the existing record (for `location_id = 1`).
df_1 = df_1.withColumn(
    'borough',
    (
        when(
            col('location_id') == 1,
            'NEWARK AIRPORT',
        )
        .otherwise(
            col('borough')
        )
    )
)

# Insert a new record into the source `DataFrame`.
df_new = (
    spark.createDataFrame(
        [
            (999, 'New Borough', 'New Zone', 'New Service Zone'),
        ],
        schema="location_id INT, borough STRING, zone STRING, service_zone STRING",
    )
    .withColumn('effective_date', current_timestamp())
    .withColumn('end_date', lit(None).cast('timestamp'))
)

df_1 = df_new.union(df_1)
'''
# fmt: on
# Insert new record to the source DataFrame
df_new = spark.createDataFrame(
    [(999, "New Borough", "New Zone", "New Service Zone")],
    schema="location_id int, borough string, zone string, service_zone string"
).withColumn("effective_date", current_timestamp()) \
 .withColumn("end_date", lit(None).cast("timestamp"))

df_1 = df_new.union(df_1)

# Updating record for location_id 1
df_1 = df_1.withColumn("borough", when(col("location_id")==1, "NEWARK AIRPORT").otherwise(col("borough")))

# COMMAND ----------

## df_1.write.saveAsTable(
#     'nyctaxi.02_silver.taxi_zone_lookup',
#     mode='overwrite',
# )

# COMMAND ----------

# # spark.read.table('nyctaxi.02_silver.taxi_zone_lookup').display()

# COMMAND ----------

# Load the current version of the Delta Table.
dt = DeltaTable.forName(
    spark,
    'nyctaxi.02_silver.taxi_zone_lookup',
)

# Fixed point-in-time that will be used to
# [expire/deactivate/]"close" any active records in `dt` which have been updated within `df_1`.
end_timestamp = datetime.datetime.now()

# COMMAND ----------

# Step 1: Expire any active records, whose tracked attributes have changed.

(
    dt.alias('t')
    .merge(
        source = df_1.alias('s'),
        condition = """
            t.location_id = s.location_id
            AND
            t.end_date IS NULL
            AND
            (
                t.borough != s.borough
                OR
                t.zone != s.zone
                OR
                t.service_zone != s.service_zone
            )
        """,
    )
    .whenMatchedUpdate(
        set={
            't.end_date': lit(end_timestamp).cast(TimestampType()),
        }
    )
    .execute()
)

# COMMAND ----------

# Step 2: Insert new current versions.
#
#   keys, which just got expired in Step 1

location_ids_from_source_that_need_to_be_inserted = [
    row.location_id
    for row in (
        dt
        .toDF()
        .filter(f"end_date = '{end_timestamp}'")
        .select('location_id')
        .collect()
    )
]

if len(location_ids_from_source_that_need_to_be_inserted) == 0:
    print("Step 1 didn't expire any records, so Step 2 doesn't have to insert any records")
else:
    comma_separated_list_of_location_ids = ', '.join(
        map(str, location_ids_from_source_that_need_to_be_inserted)
    )

    # The following logic contains a double negative - at least on a conceptual level.
    # The reason for that is that
    # there is no such thing as a `.whenMatchedInsert`.
    (
        dt.alias('t')
        .merge(
            source=df_1.alias('s'),
            condition=f"s.location_id NOT IN ({comma_separated_list_of_location_ids})"
        )
        .whenNotMatchedInsert(
            values={
                't.location_id': 's.location_id',
                't.borough': 's.borough',
                't.zone': 's.zone',
                't.service_zone': 's.service_zone',
                't.effective_date': current_timestamp(),
                't.end_date': lit(None).cast(TimestampType()),
            }
        )
        .execute()
    )

# COMMAND ----------

# Step 3: Insert new current values.
#
#   brand-new keys that are currently absent from the target

# Recall the following fact, which was mentioned in the preceding cell:
# there is no such thing as a `.whenMatchedInsert`.
# Bearing that in mind,
# what the following logic does is
# "If the Target Location ID is different from the Source Location ID, then insert that record from the Source".
(
    dt.alias('t')
    .merge(
        source=df_1.alias('s'),
        condition='t.location_id = s.location_id'
    )
    .whenNotMatchedInsert(
        values={
            't.location_id': 's.location_id',
            't.borough': 's.borough',
            't.zone': 's.zone',
            't.service_zone': 's.service_zone',
            't.effective_date': current_timestamp(),
            't.end_date': lit(None).cast(TimestampType()),
        }
    )
    .execute()
)
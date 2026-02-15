# Databricks notebook source
# Go to `Catalog`
# Click on the cogwheel icon
# Click on `External Locations`
# Click on the External Location (with the same name of your Databricks workspace, which was automatically created)
# Copy the URL

url = "abfss://unity-catalog-storage@dbstoragezytstmqw3xur6.dfs.core.windows.net/7405612818031955"

sql_script = f"""
    CREATE CATALOG IF NOT EXISTS
        nyctaxi
    MANAGED LOCATION
        '{url}'
"""

spark.sql(
    sql_script
)

# COMMAND ----------

# If we don't provide a `MANAGED LOCATION` for each `SCHEMA`,
# the one associated with the targeted `CATALOG` will be used.

spark.sql(
    """
    CREATE SCHEMA IF NOT EXISTS
        nyctaxi.00_landing
    ;
    """
)

spark.sql(
    """
    CREATE SCHEMA IF NOT EXISTS
        nyctaxi.01_bronze
    ;
    """
)

spark.sql(
    """
    CREATE SCHEMA IF NOT EXISTS
        nyctaxi.02_silver
    ;
    """
)

spark.sql(
    """
    CREATE SCHEMA IF NOT EXISTS
        nyctaxi.03_gold
    ;
    """
)

# COMMAND ----------

# By default,
# the `MANAGED LOCATION` of the to-be-created `VOLUME`
# will be the same as
# the one associated with the targeted `CATALOG` will be used.

spark.sql(
    """
    CREATE VOLUME IF NOT EXISTS
        nyctaxi.00_landing.data_sources
    ;
    """
)

# COMMAND ----------


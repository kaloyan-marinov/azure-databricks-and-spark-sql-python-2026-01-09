# 132-spark-configurations.md

Spark exposes hundreds of [configuration options](
    https://spark.apache.org/docs/latest/configuration.html
)
that control everything
from memory allocation,
to shuffle behavior,
to Databricks-specific features like disk cache.



# Main ways to apply those configuration settings

## Way 1

Set them in your notebook:

```python
spark.conf.set(
    "spark.sql.autoBroadcastJoinThreshold",
    104_857_600,  # = 100 MB
)

spark.conf.set(
    "spark.databricks.io.cache.enabled",
    "false",
)
```

## Way 2

Set them directly in your `All-Purpose Compute` or `Job Compute` clusters.

- click on the cluster

- go to `Advanced`

- click on the `Spark` tab

- specify

  ```
  # Spark config

  spark.sql.autoBroadcastJoinThreshold 104857600
  spark.databricks.io.cache.enabled false
  ```

(It won't let you do this on a `Serverless` compute,
because that's managed entirely by Databricks.)

## Way 3

That can be done when creating `Job`s.

```python
spark.conf.getAll
```

```python
spark.conf.get("spark.sql.autoBroadcastJoinThreshold")
```

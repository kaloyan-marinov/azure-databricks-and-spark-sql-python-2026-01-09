from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp


def add_processed_timestamp(df: DataFrame) -> DataFrame:
    """
    Augment the input `df` with a 'processed_timestamp' column.
    """
    return df.withColumn(
        "processed_timestamp",
        current_timestamp(),
    )

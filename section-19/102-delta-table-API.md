# 102-delta-table-API.md

So far in this course, we've
loaded data from a DELTA TABLE to a `DataFrame`
and
performed our operations directly on the `DataFrame`.

Once we've performed those operations on the `DataFrame`,
we're able to use the `pyspark.sql.DataFrameWriter` API
to write the contents of the `DataFrame` back into the DELTA TABLE -
BUT we only have 2 options when writing the data:
    - 'append'
    - 'overwrite'

We DON'T have other available functionality such as:
    - updating individual records
    - deleting individual records
    - combining updates, deletes, and inserts with 'merge' operations
That's where the `DeltaTable` API comes in -

The `DeltaTable` API:
    - enables you to interact directly with the underlying DELTA TABLE
    - provides you with additional [data-manipulation operations](
        https://docs.delta.io/delta-update/
      )

But the first thing we'll need to do is
to be able to create a `DeltaTable` instance
so we can interact with it using the Python API:
    https://docs.delta.io/api/latest/python/spark/index.html

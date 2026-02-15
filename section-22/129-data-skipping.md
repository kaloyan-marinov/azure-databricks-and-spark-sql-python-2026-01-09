# 129-data-skipping.md

In Databricks,
<u>data skipping</u> is a performance optimization technique
that helps the engine avoid reading unnecessary data files during a query.

It works on datasets stored in the `DELTA LAKE` format.

When a `DELTA LAKE` dataset is created or updated,
the following takes place behind the scenes:
statistics like the minimum and maximum values for the columns are
automatically collected
and
stored
at the file level in <u>the Delta Transaction Log</u> (aka in the `_delta_log/` folder).

The essence of <u>data skipping</u> is that
the above-mentioned statistics are utilized:

- to avoid reading files, which are guaranteed not to match your query conditions

- to speed up aggregations



<u>Data skipping</u> works automatically in Delta Lake
and
you don't need to configure anything.

But you can enhance it
by using techniques like `Z Ordering` and `Liquid Clustering`,
which physically re-organizes the data to group similar values together
(improving how effective your <u>data skipping</u> can be).

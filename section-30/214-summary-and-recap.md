# 214-summary-and-recap.md

## Summary

In the landing layer:

- To simulate timestamp-lag-affected temperature readings, vibration readings and tilt readings,
  we spun up 3 continuous «data streams».

- Those remained "alive"
  i.e. they kept on continuously writing data into a «managed volume» called `/Volumes/bridge_monitoring/00_landing/streaming`.



In the bronze layer:

- We ingested the above-mentioned «data streams» from the landing layer
  and
  we created 3 «streaming tables» in the bronze layer.



In the silver layer:

- We `JOIN`ed each of the «data streams» from the bronze layer
  with a «static table» (with bridge metadata),
  whereby we automated the monitoring of value ranges and the dropping of invalid records.
  (Each of those automations was implemented as a «DLT expectation».)



In the gold layer:

- We computed one aggregation for each «data stream» from the silver layer
  over a 10-minute «tumbling windows»
  by applying a 2-minute «watermark».



---



Throughout, «Delta Live Tables» handled:
- the orchestration
- the automatic retries
- the incremental processing
- the data-quality enforcement
without us having to configure it.



---



With our «pipeline» continuously running,
we can:

- query any of these tables using «Databricks SQL»

- build live dashboards

- set alerts on any anomalies



## This section was not an exhaustive tutorial

There is a lot more you can explore with «Delta Live Tabbles»,
from CDC flows;
to custom expectations;
to advanced monitoring.



## Stop incurring costs by taking these "teardown steps"

Before you wrap up, please make sure to:

- manually stop the run of your «pipeline»

- interrupt the execution of the data generator notebook

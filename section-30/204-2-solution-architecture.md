# 204-2-solution-architecture.md



## A medallion architecture

We will be implementing a medallion architecture (on «Unity Catalog») from
«landing» for the source data;
«bronze» for the raw data;
«silver» for the enriched data; all the way through to
«gold» for the aggregated, business-ready data.

Be advised that:

(a) all of the tables, except for the table of bridge metadata, will be streaming tables, and

(b) the entire DLT pipeline will be incremental (= only process new or changed data).



## The «bronze» layer

- each batch of simulated (raw) readings is simply appended into its own «Delta Table»,
  residing within the «bronze» layer

- those «Delta Tables» constitute 3 independent, continuously updating data streams



## The «silver» layer

- we first "materialize" a static table of bridge metadata;
  each record in that table will be
  a mapping from a device ID to its bridge name, location, and other characteristics

- for each data stream from the «bronze» layer,
  we define a streaming table:
  
  - residing within the «silver» layer

  - by applying a stream-to-static `JOIN` against the static table of bridge metadata
    <u>after</u> having applied simple data-quality checks via «DLT expectations»

    any bad rows will trigger a warning or be quarantined



## The «gold» layer

- compute 10-minute aggregates of the readings for each bridge,
  over «tumbling windows»

  - the average temperature in each 10-minute window

  - the maximum vibration in that same window

  - the maximum tilt angle in that same window

- imbue the aggregation logic
  by specifying a «watermark» (= a threshold-of-lateness) of `2 minutes`

- `JOIN` the 3 aggregated streams together on the exact same keys:
  `(bridge_id, window_start, window_end)`

  that operation ensures that
  each output row contains all three metrics for the same bridge and interval period

- The final result is an append-only, production-ready table,
  with one row per bridge-and-ten-minute-window

  That constitues a unified view of temperature, vibration and tilt
  for real-time monitoring.

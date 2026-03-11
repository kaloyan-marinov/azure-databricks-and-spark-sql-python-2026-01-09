## 191-unity-catalog-preparation.md

- create a «catalog» called `streaming_demo`

- therein, create a «schema» called `weather_stream`

- therein, create a «managed volume» called `weather_stream_volume`



- create an «All-Purpose Compute Cluster»
  (b/c «Serverless Compute» does not support default or time-based trigger intervals,
  which will be covered later on in this section)

  - call it `Standard_F4 Single-Node Cluster`

  - uncheck `Photon acceleration`

  - specify 17.0 as the `Databricks runtime`

  - select `Standard_F4` as the `Node type`

  - check `Single Node`

  - check `Terminate after` and specify `10 minutes of inactivity`

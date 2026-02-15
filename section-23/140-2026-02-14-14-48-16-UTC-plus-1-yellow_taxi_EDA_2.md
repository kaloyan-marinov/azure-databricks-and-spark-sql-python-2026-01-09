# 140-2026-02-14-14-48-16-UTC-plus-1-yellow_taxi_EDA_2.md



The lookup table at https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
is NOT expected
to change very frequently.



For teaching purposes,
we are going to force through a change
to demonstrate/prove the correctness of how «Slowly-Changing Dimensions Type 2» is implemented.
(Cf. the relevant cell within `/Workspace/Shared/nyctaxi_project/transformations/notebooks/02_silver/2026-02-11 21:17:42 taxi_zone_lookup`)

# 205-set-things-up-in-unity-catalog.md

Create the following «securable objects» in «Unity Catalog»:

```
bridge_monitoring                   # «catalog»
    00_landing                      # «schema»
        streaming                   # «managed volume»
            bridge_temperature/
            bridge_tilt/
            bridge_vibration/
    01_bronze                       # «schema»
    02_silver                       # «schema»
    03_gold                         # «schema»
```
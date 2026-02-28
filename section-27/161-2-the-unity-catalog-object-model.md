# 161-2-the-unity-catalog-object-model.md

The contents of a «metastore»
are organized in a 3-level hierarchy.


```
metastore

    # non-data «securable objects»
    # for managing access to external data sources
    service credential
    storage credential
    external location
    external metadata

    # data-and-AI «securable objects» (aka "data assets")
    catalog                                 # the top level in the data-isolation scheme

        schema (aka databases)              # organize "data assets" into logical categories
                                            # that are more granular than catalogs
            table
            view
            volume
            function (including models)

    # non-data «securable objects»
    # for managing access to shared assets
    share
    recipient
    provider
    connection
    clean room
```

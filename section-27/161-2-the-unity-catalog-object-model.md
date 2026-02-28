# 161-2-the-unity-catalog-object-model.md

The contents of a «Unity Catalog» «metastore»
are organized in a 3-level hierarchy.

All of the objects in that hierarchy are known as «securable objects» in «Unity Catalog».


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

        schema (aka databases)              # organize data and AI assets into logical categories
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

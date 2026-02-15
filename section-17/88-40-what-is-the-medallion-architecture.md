88-40-what-is-the-medallion-architecture.md



The medallion architecture is
a guiding framework for organizing the data within a [data lakehouse](
    https://www.databricks.com/glossary/data-lakehouse
).

The core idea is

(a) to pre-define several «organizational units»
    which are commonly called «layers» or «zones», and

(b) to make "input data" flow from each layer to the next one
    in such a way that
    incrementally and progressively improves the structure and quality of the data.



```
        landing         ->      bronze                      ->      silver              ->      gold

        preserve                raw data                            validated,                  typically organized
        the original            as ingested from                    cleaned,                    in consumption-ready
        file format             external source systems             deduplicated,               "project-specific"
        of                                                          enriched,                   databases
        the input data          corresponds to the                  quality-checked,
                                source table strucutres "as-is"     more structured
                                along with any additional           data
                                metadata columns
                                that capture                        matched,                    for reporting
                                the load timestamp,                 merged,
                                process ID,                         conformed,                  uses more de-normalized
                                etc.                                cleansed ("just-enough")    and
                                                                    to provide                  read-optimized
                                                                    an "Enterprise view"        data models
                                                                    of all its key              with fewer JOINs
                                                                    business entities,
                                                                    concepts
                                                                    and transactions

```



Just ro re-iterate:
The medallion architecture is a guiding framework, not a fixed rule.

- Not everybody uses the same number of layers

- Not everybody uses the same layer names

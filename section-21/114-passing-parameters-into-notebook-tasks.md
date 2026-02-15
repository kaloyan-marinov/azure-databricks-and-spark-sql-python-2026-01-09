# 114-passing-parameters-into-notebook-tasks.md

## Parameters, which are to be read in by a single `Task`

for the earlier task,
specify `Parameters` equal to
```json
{
  "football_team": "Arsenal FC"
}
```

inside the Notebook itself,
use
```python
dbutils.widgets.get("football_team")
```



The following dynamic value references are supported:
https://docs.databricks.com/aws/en/jobs/dynamic-value-references



## Parameters, which are to be read in by multiple `Task`s

Set `Job parameters` by clicking on `Edit parameters`.
